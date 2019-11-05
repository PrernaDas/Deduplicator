# Copyright 2019, University of Illinois at Chicago and Oregon Health & Science University
# This file is part of the deduplicator project.
# See the ReadMe.txt file for licensing information.

def score_dictionary(dx):
	PUBMED_SCORE = 1000
	EMBASE_SCORE = 0
	CINAHL_SCORE = 500
	CCRCT_SCORE = 600
	OVID_SCORE = 400
	OTHER_DB_SCORE = 200
	HAS_DOI = 50
	HAS_ABSTRACT = 50

	s = 0	
	
	if dx['DB_ID'][0].startswith('PMID'):
		s += PUBMED_SCORE
	elif dx['DB_ID'][0].startswith('CINAHL'):
		s += CINAHL_SCORE
	elif dx['DB_ID'][0].startswith('OVID'):
		s += OVID_SCORE
	elif dx['DB_ID'][0].startswith('CCRCT'):
		s += CCRCT_SCORE		
	else:
		s += EMBASE_SCORE
	
	if 'DO' in dx.keys():
		s += 10

	if 'AB' in dx.keys():
		s += 10		
	


	s += len(dx)
	

	return s
