# Basic-NER-tagger-for-HIV-medications

Background: A Product Information document (PI) provides health professionals with a summary of the scientific information relevant to the safe and effective use of a prescription medicine. Clients would often require PDFs of the PIs to be saved whenever specific medicines are mentioned in a text (manuscript or transcript). Identifying common medications in a text and manually downloading the PDFs from the Therapeutic Goods Administration (TGA) website can be time consuming.

Results: I used Python libraries to identify common HIV medications mentioned in a text and automatically download PDFs of the PIs from the TGA website. This saved alot of my time and reduced the risk of 'missing' PIs.  Note that the HIV drug list used in the spaCy matcher is not exhaustive and does not include combination therapies.

Libraries/tools used: SpaCy, Selenium 
