
import argparse
import subprocess
import sys
from os import remove
from os import listdir # get everything in a directory - files and directory
from os.path import isfile, join
import unidecode
# import re
from collections import defaultdict
from itertools import combinations
from  itertools import chain

from deduplicator.XML_to_RIS import xml_to_ris_using_bibutils
from deduplicator.count_records import ris_file_num_records, xml_file_num_records
from deduplicator.RIS_to_DICT import ris_to_dict_list
from deduplicator.adding_comparison_keys import add_comparison_keys
from deduplicator.database_identifier import add_database_identifier
from deduplicator.year_based_partition import partitition_on_year
from deduplicator.match_dictionaries import are_these_duplicates
from deduplicator.score_dictionary import score_dictionary
from deduplicator.DICT_to_RIS import dict_to_ris

def dictionary_year_key_records_value(year_list, list_of_dicts):
	dictionary_by_year = defaultdict(list) 
	for y in year_list:
		for d in list_of_dicts:
			if y==d['YEAR']:
				dictionary_by_year[y].append(d)

	return dictionary_by_year			


def python_deduplicator_main_function(input_file_names, output_file_name):
		ris_input_files = [f for f in input_file_names if f.endswith('.ris')]

		xml_input_files = [f for f in input_file_names if f.endswith('.xml')]


		print(' ')
		sys.stdout.write('**** Output from the PYTHON_DEDUPLICATOR ***\n')
		print(' ')

		if len(ris_input_files) !=0:
			sys.stdout.write('Found %s input .ris files %s\n' % (len(ris_input_files), ris_input_files))
			for h in ris_input_files:
				sys.stdout.write('%s has %s records\n' % (h, ris_file_num_records(h)))
				print(' ')



		if len(xml_input_files) != 0:
			sys.stdout.write('Found %s input .xml files %s\n' % (len(xml_input_files), xml_input_files))	
			sys.stdout.write ('This/These will be converted to .ris file(s).\n')
		

		# Convert .xml to .ris 
		xml_to_ris_converted_files = []
		if len(xml_input_files) !=0:
			sys.stdout.write('Converting the .xml file(s) to .ris file(s)...\n')
			sys.stdout.write('Note: This may take some time!!\n')
			for xml_f in xml_input_files:
				xml_ris_f = xml_to_ris_using_bibutils(xml_f)
				xml_to_ris_converted_files.append(xml_ris_f)
				sys.stdout.write('Converted %s to %s\n' % (xml_f, xml_f.rsplit('.', 1)[0]+'.ris'))
				sys.stdout.write('Done!\n')
				print(' ')
		
		for x in xml_input_files:
			sys.stdout.write('%s had %s records\n' % (x, xml_file_num_records(x)))
		for y in xml_to_ris_converted_files:
			sys.stdout.write('%s has %s records\n' % (y, ris_file_num_records(y)))
			print(' ')



		all_ris_files = ris_input_files + xml_to_ris_converted_files
		all_ris_list_of_dicts = []
		for rf in all_ris_files:
			rfd = ris_to_dict_list(rf) # Each .ris gets converted into a list of dictionaries
			for d in rfd:
				all_ris_list_of_dicts.append(d)

		sys.stdout.write('Total number of records to be deduplicated is %s.\n' % (len(all_ris_list_of_dicts)))
		print(' ')


		all_ris_list_of_dicts_fields_added = add_comparison_keys(all_ris_list_of_dicts) # add the fields to be compared to each dictionary
		all_ris_list_of_dicts_db_added = add_database_identifier(all_ris_list_of_dicts_fields_added) # add the database identifier to each dictionary
		years_sorted, no_year_pool, year_pool = partitition_on_year(all_ris_list_of_dicts_db_added) # divide the dictionaries based on presence/absence of year


		sys.stdout.write('Starting deduplication...\n')

		 

		# years_sorted and year_pool
		dictionary_by_year = dictionary_year_key_records_value(years_sorted, year_pool)
		single_records = []
		unique_records = []
		duplicate_records = []

		
		for y in years_sorted:
			records_to_be_compared = dictionary_by_year[y]
			# print(y, len(records_to_be_compared))
			if len(records_to_be_compared) == 1:
				single_records.append(records_to_be_compared[0]) 
			else:
				while len(records_to_be_compared) !=0:
					unique_records.append(records_to_be_compared.pop(0))
					records_to_be_compared_next = []
					for r in records_to_be_compared:
						if are_these_duplicates(r, unique_records[-1]):
							score_u = score_dictionary(unique_records[-1])
							score_r = score_dictionary(r)
							if score_u >= score_r:
								duplicate_records.append(r)
							else:
								duplicate_records.append(unique_records[-1])
								unique_records[-1] = r
						else:
							records_to_be_compared_next.append(r)
					records_to_be_compared = records_to_be_compared_next



		# no_year_pool
		unique_records_nyp = []
		duplicate_records_nyp = []
		if len(no_year_pool) != 0:
			#print('Number of records with no year', len(no_year_pool))
			while len(no_year_pool) !=0:
				unique_records_nyp.append(no_year_pool.pop(0))
				records_to_be_compared_next_nyp = []
				for y in no_year_pool:
						if are_these_duplicates(nyp, unique_records_nyp[-1]):
							score_u_nyp = score_dictionary(unique_records_nyp[-1])
							score_y = score_dictionary(y)
							if score_u_nyp >= score_y:
								duplicate_records_nyp.append(y)
							else:
								duplicate_records_nyp.append(unique_records_nyp[-1])
								unique_records_nyp[-1] = y
						else:
							records_to_be_compared_next_nyp.append(y)
			

		sys.stdout.write('Deduplication Done!!\n')
		print(' ')


		unique_records = unique_records + single_records + unique_records_nyp
		duplicate_records = duplicate_records + duplicate_records_nyp



		# Drop the add_comparison_keys: YEAR, DOI, JOURNAL_FULL, JOURNAL_AB, PAGES, TITLE, ISSN and FIRST_AUTHOR
		drop_keys = ['YEAR', 'DOI', 'JOURNAL_FULL', 'JOURNAL_AB', 'Start_P', 'End_P', 'TITLE', 'ISSN', 'FIRST_AUTHOR', 'VOLUME', 'ISSUE']
		for k in drop_keys:
			for urs in unique_records:
				if k in urs.keys():
					urs.pop(k)

		for k in drop_keys:
			for drs in duplicate_records:
				if k in drs.keys():
					drs.pop(k)


			

		sys.stdout.write('Number of unique records is %s.\n' % (len(unique_records)))
		sys.stdout.write('Number of duplicate records is %s.\n' % (len(duplicate_records)))
		print(' ')

		output_file_unique_records = output_file_name + '.unique_records.ris'
		output_file_duplicate_records = output_file_name + '.duplicate_records.ris'


		with open(output_file_unique_records, 'w') as ofur:
			for ur in unique_records:
				line_list = dict_to_ris(ur)
				ofur.write('TY - JOUR'+'\n')
				for l in line_list:
					ofur.write(l+'\n')
				ofur.write(' '+'\n')
		 				

		with open(output_file_duplicate_records, 'w') as ofdr:
			for dr in duplicate_records:
				line_list = dict_to_ris(dr)
				ofdr.write('TY - JOUR'+'\n')
				for l in line_list:
					ofdr.write(l+'\n')
				ofdr.write(' '+'\n')



		sys.stdout.write('Unique records have been written out to %s (%s records)\n' % (output_file_unique_records, ris_file_num_records(output_file_unique_records)))
		sys.stdout.write('Duplicate records have been written out to %s (%s records)\n' % (output_file_duplicate_records, ris_file_num_records(output_file_duplicate_records)))

		if len(xml_input_files) !=0:
			for xif in xml_input_files:
				corresponding_ris_file = xif.rsplit('.', 1)[0]+'.ris'
				remove(corresponding_ris_file)


if __name__ == '__main__':

	parser = argparse.ArgumentParser()
	parser.add_argument('-input_file', nargs='*', help='input filename(s) in .ris, .xml formats to be deduplicated \
		as -input_file a.ris b.bib c.ris d.xml ....')
	parser.add_argument('-output_file', help='name of the file containing the output from the Deduplicator')
	args = parser.parse_args()

	
	python_deduplicator_main_function(input_file_names=args.input_file, output_file_name=args.output_file)	




