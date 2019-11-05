import re
import unidecode



# from RIS_to_DICT import ris_to_dict_list

# test_file = input('Enter the name of the .ris file:')


def add_comparison_keys(list_of_dicts):
	all_ris_list_of_dicts=list_of_dicts
	for arlod in all_ris_list_of_dicts:
		
		# add YEAR key
		if 'PY' in arlod.keys():
			y = re.search(r'(\d{4})', arlod['PY'][0])	
			if y:
				year = y.group()
				arlod['YEAR']=year
				#print(arlod['YEAR'])
			else:
				year =None
				# print(year)
				arlod['YEAR']=year	
				#print(arlod['YEAR'])

		elif 'Y1' in arlod.keys():
			y = re.search(r'(\d{4})', arlod['Y1'][0])	
			if y:
				year = y.group()
				arlod['YEAR']=year
				#print((arlod['YEAR'])
			else:
				year =None
				arlod['YEAR']=year
				#print(arlod['YEAR'])
		else:
			arlod['YEAR']=None	
				

		# add DOI key
		if 'DO' in arlod.keys():
			DOI=arlod['DO'][0].replace('https://dx.doi.org/', '').replace('http://dx.doi.org/', '')
			arlod['DOI']=DOI
		else:
			arlod['DOI']=None	


		# add ISSN key
		if 'SN' in arlod.keys():
			ISSN=arlod['SN'][0]
			arlod['ISSN']=ISSN
		else:
			arlod['ISSN']=None


		# add JOURNAL_FULL key	
		if 'J0' in arlod.keys():
			journal_full=arlod['JO'][0]
			arlod['JOURNAL_FULL']=journal_full
		elif 'JF' in arlod.keys():
			journal_full=arlod['JF'][0]
			arlod['JOURNAL_FULL']=journal_full
		else:
			arlod['JOURNAL_FULL']=None	

		#print('journal_full', arlod['JOURNAL_FULL'])	


		# add JOURNAL_AB key	
		if 'J1' in arlod.keys():
			journal_ab=arlod['J1'][0]
			arlod['JOURNAL_AB']=journal_ab
		elif 'JA' in arlod.keys():
			journal_ab=arlod['JA'][0]
			arlod['JOURNAL_AB']=journal_ab
		else:
			arlod['JOURNAL_AB']=None

		#print('journal_ab', arlod['JOURNAL_AB'])	

		# add PAGES key
		if 'SP' in arlod.keys():
			SP=unidecode.unidecode(arlod['SP'][0])
			#print('SP', SP)
			if '-' in SP:
				Start_P = SP.split('-')[0].strip()
				End_P = SP.split('-')[1].strip()
				if Start_P.isalnum() and not Start_P.isalpha():
					arlod['Start_P'] = Start_P
				else:
					arlod['Start_P'] = None
				
				if End_P.isalnum() and not End_P.isalpha():
					arlod['End_P'] = End_P	
					if len(arlod['Start_P'])>len(arlod['End_P']):
						diff=len(arlod['Start_P'])-len(arlod['End_P'])
						arlod['End_P']=arlod['Start_P'][:diff]+arlod['End_P']
				else:
					arlod['End_P'] = None					
			



			else:
				if SP.isalnum() and not SP.isalpha():
					arlod['Start_P'] = SP
				else:
					arlod['Start_P'] = None						
		else:
			arlod['Start_P']=None
			
						

		if 'EP' in arlod.keys() and arlod['EP'][0].isalnum() and not arlod['EP'][0].isalpha():
				arlod['End_P']=arlod['EP'][0]
				#print('EP', arlod['EP'][0])
				if arlod['Start_P'] is not None:
					if len(arlod['Start_P'])>len(arlod['End_P']):
						diff=len(arlod['Start_P'])-len(arlod['End_P'])
						arlod['End_P']=arlod['Start_P'][:diff]+arlod['End_P']
						
		elif 'End_P' in arlod:
			pass
		else:
			arlod['End_P']=None	
				
		


		#print('Start_P', arlod['Start_P'])			
		#print('End_P', arlod['End_P'])					


		# add TITLE key
		if 'TI' in arlod.keys():
			title=arlod['TI'][0]
			arlod['TITLE']=title
			#print(arlod['TITLE'])
		elif 'T1' in arlod.keys():
			title=arlod['T1'][0]
			arlod['TITLE']=title
			#print(arlod['TITLE'])	
		else:
			arlod['TITLE']=None
			#print(arlod['TITLE'])	

		#print('title', arlod['TITLE'])
			
		# add FIRST_AUTHOR key
		if 'AU' in arlod.keys():
			all_author_list=arlod['AU']
			first_author=all_author_list[0].replace(',', '').replace('.', '')
			arlod['FIRST_AUTHOR']=first_author
			#print(arlod['FIRST_AUTHOR'])
		elif 'A1' in arlod.keys():
			all_author_list=arlod['A1']
			first_author=all_author_list[0].replace(',', '').replace('.', '')
			arlod['FIRST_AUTHOR']=first_author
			#print(arlod['FIRST_AUTHOR'])
		else:
			arlod['FIRST_AUTHOR']=None	
			


		# add VOLUME key
		if 'VL' in arlod.keys():
			volume = arlod['VL'][0]
			arlod['VOLUME'] = volume
		else:
			arlod['VOLUME'] = None			


		# add ISSUE key
		if 'IS' in arlod.keys():
			issue = arlod['IS'][0]
			arlod['ISSUE'] = issue	
		else:
			arlod['ISSUE'] = None	
			
	
	return all_ris_list_of_dicts	





