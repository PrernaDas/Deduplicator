# Copyright 2019, University of Illinois at Chicago and Oregon Health & Science University
# This file is part of the deduplicator project.
# See the ReadMe.txt file for licensing information.



import subprocess
import os
import tempfile


def xml_to_ris_using_bibutils(xml_file):
	"""
	Converts a .xml file to a .ris file
	"""


	xml_file_path = os.path.split(xml_file)[0]
	xml_file_name  = os.path.split(xml_file)[1]


	

	med2xml_file_name = xml_file_name.rsplit('.', 1)[0]+'_mod'+'.xml'
	xml2ris_file_name = xml_file_name.rsplit('.', 1)[0]+'.ris'



	if len(xml_file_path) != 0:
		med2xml_file = xml_file_path+'/'+med2xml_file_name
		xml2ris_file = xml_file_path+'/'+xml2ris_file_name
	else:
		med2xml_file = 	med2xml_file_name
		xml2ris_file = xml2ris_file_name


	with open(med2xml_file, 'w', encoding="utf_8") as f1, tempfile.TemporaryFile() as tmp1:
		p1 = subprocess.Popen(['med2xml', xml_file], stdout=f1, stderr=tmp1)
		p1.wait()
		#print('p1 process Done!!')


	if os.path.isfile(med2xml_file):
		with open(xml2ris_file, 'w', encoding="utf_8") as f2, tempfile.TemporaryFile() as tmp2:
			p2 = subprocess.Popen(['xml2ris', med2xml_file], stdout=f2, stderr=tmp2)
			p2.wait()
			#print('p2 process Done!!')
			

	os.remove(med2xml_file)		
	return  xml2ris_file		








