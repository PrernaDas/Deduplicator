import unittest
from ..adding_comparison_keys import add_comparison_keys


class TestYEAR(unittest.TestCase):
	def test_add_year_example_1(self):
		l = [{'Y1': ['1974//']}]
		actual = add_comparison_keys(l)[0]['YEAR']
		expected = '1974'
		self.assertEqual(actual, expected)


	def test_add_year_example_2(self):
		l = [{'Y1': ['1973/09//1973 Sep']}]
		actual = add_comparison_keys(l)[0]['YEAR']
		expected = '1973'
		self.assertEqual(actual, expected)



	def test_add_year_example_3(self):
		l = [{'PY': ['2015']}]
		actual = add_comparison_keys(l)[0]['YEAR']
		expected = '2015'
		self.assertEqual(actual, expected)


	def test_add_year_example_4(self):
		l = [{'N2': ['2015']}]
		actual = add_comparison_keys(l)[0]['YEAR']
		expected = None
		self.assertIsNone(expected)	


class TestDOI(unittest.TestCase):
	def test_add_doi_example_1(self):
		l = [{'DO': ['10.1073/pnas.1401880112']}]
		actual = add_comparison_keys(l)[0]['DOI']
		expected = '10.1073/pnas.1401880112'
		self.assertEqual(actual, expected)


	def test_add_doi_example_2(self):
		l = [{'DO': ['http://dx.doi.org/10.1037/h0042466']}]
		actual = add_comparison_keys(l)[0]['DOI']
		expected = '10.1037/h0042466'
		self.assertEqual(actual, expected)


	def test_add_doi_example_3(self):
		l = [{'DO': ['http://dx.doi.org/10.1037/h0042466', 'http://dx.doi.org/10.1037/h0042466']}]
		actual = add_comparison_keys(l)[0]['DOI']
		expected = '10.1037/h0042466'
		self.assertEqual(actual, expected)	


	def test_add_doi_example_4(self):	
		l = [{'N2': ['2015']}]
		actual = add_comparison_keys(l)[0]['DOI']
		expected = None
		self.assertIsNone(expected)


class TestISSN(unittest.TestCase):	
	def test_add_issn_example_1(self):
		l = [{'SN': ['0146-8693']}]
		actual = add_comparison_keys(l)[0]['ISSN']
		expected = '0146-8693'
		self.assertEqual(actual, expected)	


	def test_add_issn_example_2(self):	
		l = [{'N2': ['2015']}]
		actual = add_comparison_keys(l)[0]['ISSN']
		expected = None
		self.assertIsNone(expected)


class TestJOURNAL(unittest.TestCase):	
	def test_add_journal_example_1(self):
		l = [{'JF': ['Stem cell research & therapy'], 'JA': ['Stem Cell Res Ther']}]
		jf = add_comparison_keys(l)[0]['JOURNAL_FULL']
		ja = add_comparison_keys(l)[0]['JOURNAL_AB']
		actual = [jf, ja]
		expected = ['Stem cell research & therapy', 'Stem Cell Res Ther']
		self.assertEqual(actual, expected)	



	def test_add_journal_example_2(self):	
		l = [{'JO': ['Health Magazine'], 'JF': ['Health Magazine'], 'JA': ['HEALTH MAG']}]
		jf = add_comparison_keys(l)[0]['JOURNAL_FULL']
		ja = add_comparison_keys(l)[0]['JOURNAL_AB']
		actual = [jf, ja]
		expected = ['Health Magazine', 'HEALTH MAG']
		self.assertEqual(actual, expected)	


	def test_add_journal_example_3(self):	
		l = [{'N2': ['2015']}]
		jf = add_comparison_keys(l)[0]['JOURNAL_FULL']
		ja = add_comparison_keys(l)[0]['JOURNAL_AB']
		actual = [jf, ja]
		expected = [None, None]
		self.assertEqual(actual, expected)	


class TestPAGE(unittest.TestCase):
	def test_add_page_example_1(self):
		l = [{'SP': ['1'], 'EP': ['16']}]
		sp = add_comparison_keys(l)[0]['Start_P']
		ep = add_comparison_keys(l)[0]['End_P']
		actual = [sp, ep]
		expected = ['1', '16']
		self.assertEqual(actual, expected)	


	def test_add_page_example_2(self):
		l = [{'N2': ['2015']}]
		sp = add_comparison_keys(l)[0]['Start_P']
		ep = add_comparison_keys(l)[0]['End_P']
		actual = [sp, ep]
		expected = [None, None]
		self.assertEqual(actual, expected)


	def test_add_page_example_3(self):	
		l = [{'SP': ['219s']}]
		sp = add_comparison_keys(l)[0]['Start_P']
		ep = add_comparison_keys(l)[0]['End_P']
		actual = [sp, ep]
		expected = ['219s', None]
		self.assertEqual(actual, expected)	


	def test_add_page_example_4(self):	
		l = [{'SP': ['325-328']}]
		sp = add_comparison_keys(l)[0]['Start_P']
		ep = add_comparison_keys(l)[0]['End_P']
		actual = [sp, ep]
		expected = ['325', '328']	
		self.assertEqual(actual, expected)


	def test_add_page_example_5(self):	
		l = [{'SP': ['260-']}]
		sp = add_comparison_keys(l)[0]['Start_P']
		ep = add_comparison_keys(l)[0]['End_P']
		actual = [sp, ep]
		expected = ['260', None]	
		self.assertEqual(actual, expected)	


	def test_add_page_example_6(self):	
		l = [{'SP': ['229s‐30s']}]	
		sp = add_comparison_keys(l)[0]['Start_P']
		ep = add_comparison_keys(l)[0]['End_P']
		actual = [sp, ep]
		expected = ['229s', '230s']
		self.assertEqual(actual, expected)


	def test_add_page_example_7(self):	
		l = [{'SP': ['1501'], 'EP': ['7']}]	
		sp = add_comparison_keys(l)[0]['Start_P']
		ep = add_comparison_keys(l)[0]['End_P']
		actual = [sp, ep]
		expected = ['1501', '1507']
		self.assertEqual(actual, expected)	


	def test_add_page_example_8(self):	
		l = [{'SP': ['S1'], 'EP': ['7']}]	
		sp = add_comparison_keys(l)[0]['Start_P']
		ep = add_comparison_keys(l)[0]['End_P']
		actual = [sp, ep]
		expected = ['S1', 'S7']
		self.assertEqual(actual, expected)	


	def test_add_page_example_9(self):	
		l = [{'SP': ['N.PAG'], 'EP': ['N.PAG']}]	
		sp = add_comparison_keys(l)[0]['Start_P']
		ep = add_comparison_keys(l)[0]['End_P']
		actual = [sp, ep]
		expected = [None, None]
		self.assertEqual(actual, expected)


	def test_add_page_example_10(self):	
		l = [{'SP': ['No'], 'EP': ['Specified']}]	
		sp = add_comparison_keys(l)[0]['Start_P']
		ep = add_comparison_keys(l)[0]['End_P']
		actual = [sp, ep]
		expected = [None, None]
		self.assertEqual(actual, expected)					


class TestTITLE(unittest.TestCase):
	def test_add_title_example_1(self):		
		l = [{'T1': ["Perceptual modes and asthmatic symptoms: An application of Witkin's hypothesis."]}]		
		actual = add_comparison_keys(l)[0]['TITLE']
		expected = "Perceptual modes and asthmatic symptoms: An application of Witkin's hypothesis."
		self.assertEqual(actual, expected)


	def test_add_title_example_2(self):		
		l = [{'TI': ["Perceptual modes and asthmatic symptoms: An application of Witkin's hypothesis."]}]		
		actual = add_comparison_keys(l)[0]['TITLE']
		expected = "Perceptual modes and asthmatic symptoms: An application of Witkin's hypothesis."
		self.assertEqual(actual, expected)	


	def test_add_title_example_3(self):	
		l = [{'N2': ['2015']}]	
		actual = add_comparison_keys(l)[0]['TITLE']
		expected = None
		self.assertIsNone(expected)


class TestFIRSTAUTHOR(unittest.TestCase):
	def test_add_firstauthor_example_1(self):	
		l = [{'A1': ['Redlich, Nicole', 'Prior, Margot']}]
		actual = add_comparison_keys(l)[0]['FIRST_AUTHOR']
		expected = 'Redlich Nicole'
		self.assertEqual(actual, expected)	

	def test_add_firstauthor_example_2(self):		
		l = [{'AU': ['Friday, G. A', 'Khine, H', 'Lin, M. S', 'Caliguiri, L. A']}]
		actual = add_comparison_keys(l)[0]['FIRST_AUTHOR']
		expected = 'Friday G A'
		self.assertEqual(actual, expected)	


	def test_add_firstauthor_example_3(self):	
		l = [{'A1': ['Chong, Yuen-yu', 'Mak, Yim-wah', 'Leung, Sui-ping', 'Lam, Shu-yan', 'Loke, Alice Yuen']}]	
		actual = add_comparison_keys(l)[0]['FIRST_AUTHOR']
		expected = 'Chong Yuen-yu'
		self.assertEqual(actual, expected)	


	def test_add_firstauthor_example_4(self):
		l = [{'N2': ['2015']}]	
		actual = add_comparison_keys(l)[0]['FIRST_AUTHOR']
		expected = None
		self.assertIsNone(expected)	


class TestVOLUME(unittest.TestCase):	
	def test_add_volume_example_1(self):
		l = [{'VL': ['143']}]
		actual = add_comparison_keys(l)[0]['VOLUME']
		expected = '143'
		self.assertEqual(actual, expected)	


	def test_add_volume_example_2(self):
		l = [{'N2': ['2015']}]	
		actual = add_comparison_keys(l)[0]['VOLUME']
		expected = None
		self.assertIsNone(expected)	


class TestISSUE(unittest.TestCase):
	def test_add_issue_example_1(self):
		l = [{'IS': ['143']}]
		actual = add_comparison_keys(l)[0]['ISSUE']
		expected = '143'
		self.assertEqual(actual, expected)	


	def test_add_volume_example_2(self):
		l = [{'N2': ['2015']}]	
		actual = add_comparison_keys(l)[0]['ISSUE']
		expected = None
		self.assertIsNone(expected)		





								





								
				
