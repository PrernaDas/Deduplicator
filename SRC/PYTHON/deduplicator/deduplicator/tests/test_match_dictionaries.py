import unittest
from ..match_dictionaries import doi_check, doi_match
from ..match_dictionaries import issn_check, issn_match
from ..match_dictionaries import check_key_none
from ..match_dictionaries import page_match
from ..match_dictionaries import volume_match
from ..match_dictionaries import issue_match
from ..match_dictionaries import journal_match
from ..match_dictionaries import first_author_match
from ..match_dictionaries import title_match

class TestDOI(unittest.TestCase):
	def test_doi_check_match_example_1(self):
		dictionary_1 = {'DOI': '10.1080/14767058.2018.1452904'}
		dictionary_2 = {'DOI': '10.1080/14767058.2018.1452904'}

		actual = doi_check(dictionary_1, dictionary_2) and doi_match(dictionary_1, dictionary_2)
		self.assertTrue(actual)


	def test_doi_check_match_example_2(self):
		dictionary_1 = {'DOI': '10.1080/14767058.2018.1452904'}
		dictionary_2={'DOI': 'https://dx.doi.org/10.1016/j.jaci.2017.09.030'}

		actual = doi_check(dictionary_1, dictionary_2) and doi_match(dictionary_1, dictionary_2)
		self.assertFalse(actual)


	def test_doi_check_match_example_3(self):
		dictionary_1 = {'DOI': None}
		dictionary_2={'DOI': 'https://dx.doi.org/10.1016/j.jaci.2017.09.030'}

		actual = doi_check(dictionary_1, dictionary_2) and doi_match(dictionary_1, dictionary_2)
		self.assertFalse(actual)



class TestISSN(unittest.TestCase):
	def test_issn_check_match_example_1(self):
		dictionary_1 = {'ISSN': '1073-449X'}
		dictionary_2 = {'ISSN': '1073-449X'}

		actual = issn_check(dictionary_1, dictionary_2) and issn_match(dictionary_1, dictionary_2)
		self.assertTrue(actual)


	def test_issn_check_match_example_2(self):
		dictionary_1 = {'ISSN': '1081-1206'}
		dictionary_2={'ISSN': '0031-4005'}

		actual = issn_check(dictionary_1, dictionary_2) and issn_match(dictionary_1, dictionary_2)
		self.assertFalse(actual)


	def test_issn_check_match_example_3(self):
		dictionary_1 = {'ISSN': None}
		dictionary_2={'ISSN': '1073-449X'}

		actual = issn_check(dictionary_1, dictionary_2) and issn_match(dictionary_1, dictionary_2)
		self.assertFalse(actual)		


class TestPAGE(unittest.TestCase):
	def test_page_check_match_example_1(self):
		dictionary_1 = {'Start_P': None}
		dictionary_2={'Start_P': None}

		actual = page_match(dictionary_1, dictionary_2) 
		self.assertFalse(actual)


	def test_page_check_match_example_2(self):
		dictionary_1 = {'Start_P': None}
		dictionary_2={'Start_P': '45'}

		actual = page_match(dictionary_1, dictionary_2) 
		self.assertFalse(actual)	

		
	def test_page_check_match_example_3(self):
		dictionary_1 = {'Start_P': '45'}
		dictionary_2={'Start_P': None}

		actual = page_match(dictionary_1, dictionary_2)
		self.assertFalse(actual)	


	def test_page_check_match_example_4(self):
		dictionary_1 = {'Start_P': '45'}
		dictionary_2={'Start_P': '65'}

		actual = page_match(dictionary_1, dictionary_2) 
		self.assertFalse(actual)		


	def test_page_check_match_example_5(self):
		dictionary_1 = {'Start_P': '45', 'End_P': None}
		dictionary_2={'Start_P': '45', 'End_P': '52'}

		actual = page_match(dictionary_1, dictionary_2) 
		self.assertTrue(actual)


	def test_page_check_match_example_6(self):
		dictionary_1 = {'Start_P': '45', 'End_P': '52'}
		dictionary_2={'Start_P': '45', 'End_P': None}

		actual = page_match(dictionary_1, dictionary_2) 
		self.assertTrue(actual)	


	def test_page_check_match_example_6(self):
		dictionary_1 = {'Start_P': '45', 'End_P': None}
		dictionary_2={'Start_P': '45', 'End_P': None}

		actual = page_match(dictionary_1, dictionary_2) 
		self.assertTrue(actual)			


	def test_page_check_match_example_6(self):
		dictionary_1 = {'Start_P': '45', 'End_P': '52'}
		dictionary_2={'Start_P': '45', 'End_P': '51'}

		actual = page_match(dictionary_1, dictionary_2) 
		self.assertFalse(actual)


	def test_page_check_match_example_6(self):
		dictionary_1 = {'Start_P': '45', 'End_P': '52'}
		dictionary_2={'Start_P': '45', 'End_P': '52'}

		actual = page_match(dictionary_1, dictionary_2) 
		self.assertTrue(actual)	


class TestVOLUME(unittest.TestCase):
	def test_volume_check_match_example_1(self):
		dictionary_1 = {'VOLUME': None}
		dictionary_2={'VOLUME': '67'}

		actual = volume_match(dictionary_1, dictionary_2) 
		self.assertFalse(actual)


	def test_volume_check_match_example_2(self):
		dictionary_1 = {'VOLUME': '89'}
		dictionary_2={'VOLUME': '67'}

		actual = volume_match(dictionary_1, dictionary_2) 
		self.assertFalse(actual)


	def test_volume_check_match_example_3(self):
		dictionary_1 = {'VOLUME': '67'}
		dictionary_2={'VOLUME': '67'}

		actual = volume_match(dictionary_1, dictionary_2) 
		self.assertTrue(actual)		



class TestISSUE(unittest.TestCase):
	def test_issue_check_match_example_1(self):
		dictionary_1 = {'ISSUE': None}
		dictionary_2={'ISSUE': '6'}

		actual = issue_match(dictionary_1, dictionary_2) 
		self.assertFalse(actual)


	def test_issue_check_match_example_2(self):
		dictionary_1 = {'ISSUE': '9'}
		dictionary_2={'ISSUE': '6'}

		actual = issue_match(dictionary_1, dictionary_2) 
		self.assertFalse(actual)


	def test_issue_check_match_example_3(self):
		dictionary_1 = {'ISSUE': '6'}
		dictionary_2={'ISSUE': '6'}

		actual = issue_match(dictionary_1, dictionary_2) 
		self.assertTrue(actual)		



class TestJOURNAL(unittest.TestCase):
	"""

	"""
	def test_journal_check_match_example_1(self):
		dictionary_1 = {'JOURNAL_FULL': None, \
						'JOURNAL_AB': None}

		dictionary_2 = {'JOURNAL_FULL': None, \
						'JOURNAL_AB': None}

		actual = journal_match(dictionary_1, dictionary_2) 
		self.assertFalse(actual)



	def test_journal_check_match_example_2(self):
		dictionary_1 = {'JOURNAL_FULL': 'The Journal of investigative dermatology', \
					'JOURNAL_AB': None}

		dictionary_2 = {'JOURNAL_FULL': None, \
					'JOURNAL_AB': None}

		actual = journal_match(dictionary_1, dictionary_2) 
		self.assertFalse(actual)


	def test_journal_check_match_example_3(self):
		dictionary_1 = {'JOURNAL_FULL': 'The Journal of investigative dermatology', \
					'JOURNAL_AB': None}

		dictionary_2 = {'JOURNAL_FULL': 'The Journal of Investigative Dermatology', \
					'JOURNAL_AB': None}

		actual = journal_match(dictionary_1, dictionary_2) 
		self.assertTrue(actual)	
	


	def test_journal_check_match_example_4(self):
		dictionary_1 = {'JOURNAL_FULL': 'The Journal of investigative dermatology', \
					'JOURNAL_AB': None}

		dictionary_2 = {'JOURNAL_FULL': None, \
					'JOURNAL_AB': 'J Invest Dermatol'}

		actual = journal_match(dictionary_1, dictionary_2) 
		self.assertTrue(actual)	


	def test_journal_check_match_example_5(self):
		dictionary_1 = {'JOURNAL_FULL': 'The Journal of investigative dermatology', \
					'JOURNAL_AB': 'J Invest Dermatol'}

		dictionary_2 = {'JOURNAL_FULL': None, \
					'JOURNAL_AB': 'J Invest Dermatol'}

		actual = journal_match(dictionary_1, dictionary_2) 
		self.assertTrue(actual)		


	def test_journal_check_match_example_6(self):
		dictionary_1 = {'JOURNAL_FULL': 'The Journal of investigative dermatology', \
					'JOURNAL_AB': 'J Invest Dermatol'}

		dictionary_2 = {'JOURNAL_FULL': None, \
					'JOURNAL_AB': 'The Journal of investigative dermatology'}

		actual = journal_match(dictionary_1, dictionary_2) 
		self.assertTrue(actual)			


	def test_journal_check_match_example_7(self):
		dictionary_1 = {'JOURNAL_FULL': 'The Journal of Clinical Dermatological Practice', \
					'JOURNAL_AB': None}

		dictionary_2 = {'JOURNAL_FULL': 'The Journal of Investigative Dermatology', \
					'JOURNAL_AB': None}

		actual = journal_match(dictionary_1, dictionary_2) 
		self.assertFalse(actual)	


class TestFIRSTAUTHOR(unittest.TestCase):
	"""

	"""
	def test_firstauthor_check_match_example_1(self):
		dictionary_1 = {'FIRST_AUTHOR': None}
		dictionary_2 = {'FIRST_AUTHOR': 'Lafyatis, R'}

		actual = first_author_match(dictionary_1, dictionary_2) 
		self.assertFalse(actual)



	def test_firstauthor_check_match_example_3(self):
		dictionary_1 = {'FIRST_AUTHOR': 'Lafyatis, Robert'}
		dictionary_2 = {'FIRST_AUTHOR': 'Lafyatis, R'}

		actual = first_author_match(dictionary_1, dictionary_2) 
		self.assertTrue(actual)


	def test_firstauthor_check_match_example_4(self):
		dictionary_1 = {'FIRST_AUTHOR': 'Kim, Young Mee'}
		dictionary_2 = {'FIRST_AUTHOR': 'Kim, YM'}

		actual = first_author_match(dictionary_1, dictionary_2) 
		self.assertTrue(actual)		

		

class TestTITLE(unittest.TestCase):
	"""

	"""
	def test_title_check_match_example_1(self):
		dictionary_1 = {'TITLE': None}
		dictionary_2 = {'TITLE': 'Expression and shedding of CD44 in the endometrium of women with endometriosis and modulating effects of vitamin D: a randomized exploratory trial'}

		actual = title_match(dictionary_1, dictionary_2) 
		self.assertFalse(actual)


	def test_title_check_match_example_2(self):
		dictionary_1 = {'TITLE': 'Expression and shedding of CD44 in the endometrium of women with endometriosis and modulating effects of vitamin D: a randomized exploratory trial'}
		dictionary_2 = {'TITLE': 'Expression and shedding of CD44 in the endometrium of women with endometriosis and modulating effects of vitamin D: a randomized exploratory trial'}

		actual = title_match(dictionary_1, dictionary_2) 
		self.assertTrue(actual)	


	def test_title_check_match_example_2(self):
		dictionary_1 = {'TITLE': 'Expression and shedding of CD44 in the endometrium of women with endometriosis and modulating effects of vitamin D: a randomized exploratory trial'}
		dictionary_2 = {'TITLE': 'ASPirin Intervention for the REDuction of colorectal cancer risk (ASPIRED): a study protocol for a randomized controlled trial'}

		actual = title_match(dictionary_1, dictionary_2) 
		self.assertFalse(actual)	


	def test_title_check_match_example_4(self):
		dictionary_1 = {'TITLE': 'Assessment of health-related quality of life in a 52-week, phase 2, randomized, controlled trial of a novel, intra-articular, WNT pathway inhibitor (SM04690) for treatment of knee osteoarthritis'}
		dictionary_2 = {'TITLE': "Treatment of knee osteoarthritis with SM04690 improved WOMAC a1 'pain on walking'-results from a 52-week, randomized, double-blind, placebo-controlled, phase 2 study of a novel, intra-articular, WNT pathway inhibitor"}

		actual = title_match(dictionary_1, dictionary_2) 
		self.assertTrue(actual)				