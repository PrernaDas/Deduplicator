from fuzzywuzzy import fuzz
import os

def doi_check(dictionary_1, dictionary_2):
	"""

	(dictionary_1, dictionary_2) -> boolean

	>>> doi_check(dictionary_1={'DOI': '10.1080/14767058.2018.1452904'}, \
	dictionary_2={'DOI': 'https://dx.doi.org/10.1016/j.jaci.2017.09.030'})
	True

	>>> doi_check(dictionary_1={'DOI': '10.1080/14767058.2018.1452904'}, \
	dictionary_2={'DOI': None})
	False

	>>> doi_check(dictionary_1={'DOI': None}, \
	dictionary_2={'DOI': 'https://dx.doi.org/10.1016/j.jaci.2017.09.030'})
	False


	"""

	if check_key_none(dictionary_1, 'DOI') and check_key_none(dictionary_2, 'DOI'):
		return True
	else:
		return False



def doi_match(dictionary_1, dictionary_2):
	"""

	(dictionary_1, dictionary_2) -> boolean

	>>> doi_match(dictionary_1={'DOI': '10.1080/14767058.2018.1452904'}, \
	dictionary_2={'DOI': 'https://dx.doi.org/10.1016/j.jaci.2017.09.030'})
	False

	>>> doi_match(dictionary_1={'DOI': '10.1080/14767058.2018.1452904'}, \
	dictionary_2={'DOI': '10.1080/14767058.2018.1452904'})
	True

	"""

	if dictionary_1['DOI']==dictionary_2['DOI']:
		return True
	else:
		return False




def issn_check(dictionary_1, dictionary_2):

	"""
	
	(dictionary_1, dictionary_2) -> boolean

	"""
	
	if check_key_none(dictionary_1, 'ISSN') and check_key_none(dictionary_2, 'ISSN'):
		return True
	else:
		return False


def issn_match(dictionary_1, dictionary_2):

	"""
	
	(dictionary_1, dictionary_2) -> boolean
	
	"""


	if dictionary_1['ISSN']==dictionary_2['ISSN']:
		return True
	else:
		return False

 	

def check_key_none(dictionary, k):
	if k in dictionary and dictionary[k] is not None: 
		return True
	else:
		return False


# PAGE match
def page_match(dictionary_1, dictionary_2):

	"""
	# dictionary_1['PAGES']		dictionary_2['PAGES']	RESULT 
# None 						None                    False
# None                      45                      False
# 45                        None                    False
# 45                        45                      True
# 45-46						45-46					True
# 45-46                     45-6                    True
# 45                        45-6                    True
# 45-46                     45                      True
# 45-46						45-8					False ******


# Is the SP for both the records present?
# If SP for either records is missing, return False
# If SP for both the records is present, and does not match return False
# If SP for both the records is present and matches, then check if EP for both the records is present.
# If SP for both the records is present and matches, and if the EP for either of the records is missing, return True
# If SP for both the records is present and matches, and if the EP for both records is present, but EP don't match, return False
# If SP for both the records is present and matches, and if the EP for both records is present and matches, return


	"""


	if check_key_none(dictionary_1, 'Start_P') and check_key_none(dictionary_2, 'Start_P'): 
		#print(dictionary_1['Start_P'])
		#print(dictionary_2['Start_P'])
		if dictionary_1['Start_P'] != dictionary_2['Start_P']:
			return False
		else:
			endp1 = check_key_none(dictionary_1, 'End_P')
			endp2 = check_key_none(dictionary_2, 'End_P')
			if endp1 and endp2: 
				if dictionary_1['End_P'] == dictionary_2['End_P']:
					return True
				else:
					return False
			else:	
				return True

	else:
		return False



# VOLUME match
def volume_match(dictionary_1, dictionary_2):
	if check_key_none(dictionary_1, 'VOLUME') and check_key_none(dictionary_2, 'VOLUME'): 
		if dictionary_1['VOLUME'] != dictionary_2['VOLUME']:
			return False
		else:
			return True
	else:
		return False



# ISSUE MATCH
def issue_match(dictionary_1, dictionary_2):
	if check_key_none(dictionary_1, 'ISSUE') and check_key_none(dictionary_2, 'ISSUE'): 
		if dictionary_1['ISSUE'] != dictionary_2['ISSUE']:
			return False
		else:
			return True
	else:
		return False


# 
def volume_issue_page_match(dictionary_1, dictionary_2):
	if volume_match(dictionary_1, dictionary_2) and issue_match(dictionary_1, dictionary_2) and page_match(dictionary_1, dictionary_2):
		return True
	else:
		return False	


# replace this code with 

#JOURNAL_ABBREVIATION_DX = {
#	'J Invest Dermatol' : 'The Journal of investigative dermatology',
#}
####/Users/dasp/Desktop/PYTHON_DEDUPLICATOR/J_Medline.txt

# load module level global abbreviation table.
JOURNAL_ABBREVIATION_DX = None
def generate_JOURNAL_ABBREVIATION_DX(medline_catalogue_text_file):
	dx = {}
	with open(medline_catalogue_text_file, 'r') as f:
		for line in f:
			if line.startswith('JournalTitle'):
				v = line.split(':', 1)[1].replace('"', '').lstrip().rstrip().strip('\n')
			if line.startswith('MedAbbr'):
				k = line.split(':', 1)[1].lstrip().rstrip().strip('\n')
				dx[k] = v

	return dx
JOURNAL_ABBREVIATION_DX = generate_JOURNAL_ABBREVIATION_DX('MEDLINE_FILE/J_Medline.txt')

def expand_journal_abbreviation(abbreviation):
	return JOURNAL_ABBREVIATION_DX.get(abbreviation, None)

# JOURNAL NAME MATCH
def journal_match(dictionary_1, dictionary_2):	
	if check_key_none(dictionary_1, 'JOURNAL_FULL') and check_key_none(dictionary_2, 'JOURNAL_FULL'):
		fuzzy_score = fuzz.token_set_ratio(dictionary_1['JOURNAL_FULL'], dictionary_2['JOURNAL_FULL'])
		if fuzzy_score > 80:
			return True

	if check_key_none(dictionary_1, 'JOURNAL_AB') and check_key_none(dictionary_2, 'JOURNAL_AB'):
		fuzzy_score = fuzz.token_set_ratio(dictionary_1['JOURNAL_AB'], dictionary_2['JOURNAL_AB'])
		if fuzzy_score > 80:
			return True
			

	if check_key_none(dictionary_1, 'JOURNAL_FULL') and check_key_none(dictionary_2, 'JOURNAL_AB'):
		fuzzy_score = fuzz.token_set_ratio(dictionary_1['JOURNAL_FULL'], dictionary_2['JOURNAL_AB'])
		if fuzzy_score > 80:
			return True
		else:
			expanded_abbreviation = expand_journal_abbreviation(dictionary_2['JOURNAL_AB'])
			fuzzy_score = fuzz.token_set_ratio(dictionary_1['JOURNAL_FULL'], expanded_abbreviation)
			if fuzzy_score > 80:
				return True
	
	
	if check_key_none(dictionary_1, 'JOURNAL_AB') and check_key_none(dictionary_2, 'JOURNAL_FULL'):
		fuzzy_score = fuzz.token_set_ratio(dictionary_1['JOURNAL_AB'], dictionary_2['JOURNAL_FULL'])
		if fuzzy_score > 80:
			return True
		else:
			expanded_abbreviation = expand_journal_abbreviation(dictionary_1['JOURNAL_AB'])
			fuzzy_score = fuzz.token_set_ratio(dictionary_2['JOURNAL_FULL'], expanded_abbreviation)
			if fuzzy_score > 80:
				return True

	return False
									
	



# FIRST AUTHOR NAME MATCH
def first_author_match(dictionary_1, dictionary_2):
	if check_key_none(dictionary_1, 'FIRST_AUTHOR') and check_key_none(dictionary_2, 'FIRST_AUTHOR'):
		fuzzy_score = fuzz.partial_ratio(dictionary_1['FIRST_AUTHOR'], dictionary_2['FIRST_AUTHOR'])
		if fuzzy_score > 80:
			return True
		else:
			return False
	
	else:
		return False		



# TITLE MATCH
def title_match(dictionary_1, dictionary_2):
	if check_key_none(dictionary_1, 'TITLE') and check_key_none(dictionary_2, 'TITLE'):
		fuzzy_score = fuzz.token_set_ratio(dictionary_1['TITLE'], dictionary_2['TITLE'])
		if fuzzy_score > 80:
			return True
		else:
			return False	
	
	else:
		return False		




def are_these_duplicates(dictionary_1, dictionary_2):
	if doi_check(dictionary_1, dictionary_2) and not doi_match(dictionary_1, dictionary_2):
		return False

	if issn_check(dictionary_1, dictionary_2) and not issn_match(dictionary_1, dictionary_2):
		return False

	if doi_check(dictionary_1, dictionary_2) and doi_match(dictionary_1, dictionary_2):
		# print(' ')
		# print('DOI MATCH!')
		# print('D1_TITLE', dictionary_1['TITLE'])
		# print('D2_TITLE', dictionary_2['TITLE'])
		# print('D1_ID', dictionary_1['DB_ID'])
		# print('D2_ID', dictionary_2['DB_ID'])
		# print(' ')
		return True		

	if journal_match(dictionary_1, dictionary_2) and volume_issue_page_match(dictionary_1, dictionary_2):
		# print(' ')
		# print('JOURNAL and VOLUME_ISSUE_PAGE MATCH!')
		# print('D1_TITLE', dictionary_1['TITLE'])
		# print('D2_TITLE', dictionary_2['TITLE'])
		# print('D1_ID', dictionary_1['DB_ID'])
		# print('D2_ID', dictionary_2['DB_ID'])
		# print(' ')
		return True	

	if journal_match(dictionary_1, dictionary_2) and title_match(dictionary_1, dictionary_2) and first_author_match(dictionary_1, dictionary_2) and page_match(dictionary_1, dictionary_2):
		# print(' ')
		# print('JOURNAL, TITLE, FIRST_AUTHOR, and PAGE MATCH!')
		# print('D1_TITLE', dictionary_1['TITLE'])
		# print('D2_TITLE', dictionary_2['TITLE'])
		# print('D1_ID', dictionary_1['DB_ID'])
		# print('D2_ID', dictionary_2['DB_ID'])
		# print(' ')
		return True 				
	
	return False	


