import xml.etree.ElementTree as ET
import sys, json
from Entry import Entry
from csv_writer import CSVWriter

exampleEntry = {
    'title': '',
    'authors': '',
    'abstract': '',
    'affiliations': '',
    'terms': [],
    'pubId': 0,
    'date': 2000
}

tree = ET.parse('data/TVCGPubs1.xml')
root = tree.getroot()
# for child in root:
#	for subchild in child:
for child in root.findall('document'):
	title = child.find('title').text
	author = child.find('authors').text
	abstract=child.find('abstract').text
	#affiliations=child.find('affiliations').text
	print(child.find('controlledterms').findall('term'))
	#print(affiliations)
	#abstract = child.find('abstract')
	#affiliations = child.find('affiliations')
	#for subchild in child:
		#print(subchild)
		#print(subchild.items())
		#title = subchild.find('title')
	#	print(subchild.tag)
	#break


