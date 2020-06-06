# NER-tagger-for-HIV-medications
Uses the spaCy library to identify any HIV medications mentioned in a text. It then uses the selenium library to open the TGA webpage with a link to the pdf containing the product information (PI) of the particular drug. 

This tagger can be used with text data where identifying HIV drugs and gathering the respective PI is important. Note that the HIV drug list used in the spaCy matcher is not exhaustive and does not include combination therapies.
