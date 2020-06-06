# -*- coding: utf-8 -*-
"""
This little script identifies HIV drugs mentioned in a text and brings up the product information webpage for
the HIV drugs that are that are identified.
Note that you will need spacy and selenium libraries for full functionality
@author: Andrew
"""

import spacy
from spacy.tokens import Span
from spacy.matcher import PhraseMatcher
from selenium import webdriver

# load small english model and create a PhraseMatcher object
nlp = spacy.load('en_core_web_sm')
matcher = PhraseMatcher(nlp.vocab)

# Customize the matcher with the drug list
drug_list = ['abacavir',
             'emtricitabine',
             'lamivudine',
             'tenofovir',
             'zidovudine',
             'doravirine',
             'efavirenz',
             'etravirine',
             'nevirapine',
             'rilpivirine',
             'atazanavir',
             'darunavir',
             'fosamprenavir',
             'ritonavir',
             'saquinavir',
             'tipranavir',
             'enfuvirtide',
             'maraviroc',
             'dolutegravir',
             'raltegravir',
             'ibalizumab-uiyk',
             'cobicistat']

# Create empty list to add list of websites that will be populated with urls for downloading pdfs of PIs
web_list = []

# Turn a list of drugs (strings) into a list of Spacy doc objects for matching
patterns = list(nlp.pipe(drug_list))
# Give the matcher a name and add the patterns of interest for matching
matcher.add('drug', None, *patterns)


def drug_component(doc):
    """Create an entity Span with the label 'DRUG' for all matches"""
    doc.ents = [Span(doc, start, end, label='DRUG')
                for match_id, start, end in matcher(doc)]
    return doc


def get_pi_url(span):
    """Get a URL for PI if the span has one of the labels"""
    if span.label_ in 'DRUG':
        entity_text = span.text.replace(' ', '_')
        url = "https://www.ebs.tga.gov.au/ebs/picmi/picmirepository.nsf/PICMI?OpenForm&t=pi&q=" + entity_text
        web_list.append(url)
        return url


# Set the Span extension pi_url using get getter get_pi_url
Span.set_extension('PI_url', getter=get_pi_url, force=True)

# Add the component to the pipeline
nlp.add_pipe(drug_component)
print(nlp.pipe_names)

# Enter your text of interest into the sentence variable
sentence = "Raltegravir and lamivudine are common HIV medications used in the clinic. Raltegravir has now been superseded by tenofovir"

# Make the sentence lowercase, process the text and print the entity text, label and capital attributes
doc = nlp(sentence.lower())
print([(ent.text, ent.label_, ent._.PI_url) for ent in doc.ents])


for web in list(set(web_list)):
    # Note that I used 'set' here so that there are no repeats of urls
    # (e.g. when drugs are mentioned more than once in the text) in the 'web_list' list
    try:
        # Get the chrome driver location
        chrome_path = r"C:\Users\Andrew\path_to\chromedriver.exe"
        # add chrome_path to webdriver
        driver = webdriver.Chrome(chrome_path)
        # Open chrome browser and navigate to the website of interest
        driver.get(web)
    except ValueError:
        # Print website name if there is an error
        print("Error with webpage: {}".format(str(web)))
