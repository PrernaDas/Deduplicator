# Copyright 2019, University of Illinois at Chicago and Oregon Health & Science University
# This file is part of the deduplicator project.
# See the ReadMe.txt file for licensing information.


from collections import defaultdict


def ris_to_dict_list(ris_file):
	"""
	Convert a .ris file to list of dictionaries with each record being a dictionary
	"""
	d=None
	list_of_ris_record_dicts = []
	#print(ris_file)
	with open(ris_file, 'r', encoding="utf_8_sig") as ris_file:
		for line in ris_file:
			if line.strip().startswith('TY'):
				d = defaultdict(list)
				# print('Dictionary made')

			elif d is None and line.strip().startswith('ID'):
				d = defaultdict(list) 

			elif ' - ' in line:
				k = line.split('-', 1)[0].lstrip().rstrip().strip('\n')
				v = line.split('-', 1)[1].lstrip().rstrip().strip('\n')
				d[k].append(v)

			if 	line.strip().startswith('ER'):
				list_of_ris_record_dicts.append(d)

	return list_of_ris_record_dicts			
				


