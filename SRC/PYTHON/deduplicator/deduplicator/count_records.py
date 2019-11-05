# Copyright 2019, University of Illinois at Chicago and Oregon Health & Science University
# This file is part of the deduplicator project.
# See the ReadMe.txt file for licensing information.

import xml.etree.ElementTree as ET
import unidecode

def ris_file_num_records(input_ris_file):
	"""
	Counts the number of record in a .ris file
	"""
	
	with open(input_ris_file,'r', encoding="utf_8") as infile:
		num_records_ris = [line.strip() for line in infile if line.startswith('ER')]
				
	return len(num_records_ris)


def xml_file_num_records(input_xml_file):
	"""
	Counts the number of records in a .xml file

	"""
	tree = ET.parse(input_xml_file)
	root = tree.getroot()
	child_tag_list = []
	for child in root:
		if child.tag not in child_tag_list:
			child_tag_list.append(child.tag)

	child_tag_list = ['<'+t+'>' for t in child_tag_list]
	#print child_tag_list

	num_records_xml = []
	with open(input_xml_file) as xml_f:
		for tag in child_tag_list:
			for line in xml_f:
				if tag in line:
					#print line
					num_records_xml.append(line.strip())

	return len(num_records_xml)		


