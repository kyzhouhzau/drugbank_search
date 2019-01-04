# Use Elasticsearch to store drugbank datas
These codes help us to localize the drugbank data so that we can easily and conveniently search for drug information.


The most important: ```./bin/elasticsearch``` 

### get_pmid.py
This code help us get pmidlist from pubmed if we give a gene list. Not completely related to the content below.

### config.py 
We are all familiar with the storage framework of es. The structure of the mapping is provided in this code.
These include:id,title,text,denotations

### index.py

This code is used to store data downloaded from drugbank into the ES.
Of course, before the data is stored, the XML data downloaded directly from the drugbank needs to be preprocessed and save one record per line(save in \pubtator29 ), and the format is as follows:

{'id': '15902255', 'title': 'Direct dating of Early Upper Palaeolithic human remains from Mladec.', 'text': 'The human fossil assemblage from the Mladec Caves in Moravia (Czech Republic) has been considered to derive from a middle or later phase of the Central European Aurignacian period on the basis of archaeological remains (a few stone artefacts and organic items such as bone points, awls, perforated teeth), despite questions of association between the human fossils and the archaeological materials and concerning the chronological implications of the limited archaeological remains. The morphological variability in the human assemblage, the presence of apparently archaic features in some specimens, and the assumed early date of the remains have made this fossil assemblage pivotal in assessments of modern human emergence within Europe. We present here the first successful direct accelerator mass spectrometry radiocarbon dating of five representative human fossils from the site. We selected sample materials from teeth and from one bone for 14C dating. The four tooth samples yielded uncalibrated ages of approximately 31,000 14C years before present, and the bone sample (an ulna) provided an uncertain more-recent age. These data are sufficient to confirm that the Mladec human assemblage is the oldest cranial, dental and postcranial assemblage of early modern humans in Europe and is therefore central to discussions of modern human emergence in the northwestern Old World and the fate of the Neanderthals.', 'denotations': 'Species & 42 & 47 & human, Species & 73 & 78 & human, Species & 420 & 425 & human, Species & 589 & 594 & human, Species & 778 & 783 & human, Species & 925 & 930 & human, Species & 1249 & 1254 & human, Species & 1339 & 1345 & humans, Species & 1406 & 1411 & human, Species & 1472 & 1484 & Neanderthals'}

### delete.py
if you want to delete this base ,you could run.

### search.py
Customize your own search plan and store it.


