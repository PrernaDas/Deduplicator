def add_database_identifier(list_of_dicts):
	"""
	ID is source database: unique identifier for that database/accession number

	"""	
	list_of_ris_record_dicts = list_of_dicts		
	for record_dicts in list_of_ris_record_dicts:
		if 'UR' in record_dicts.keys():
			pubmed_ur = [ur for ur in record_dicts['UR'] if 'http://www.ncbi.nlm.nih.gov/pubmed/' in ur]
			if len(pubmed_ur)!=0:
				pubmed_url = pubmed_ur[0]
				pmid = pubmed_url.split('/')[-1]
				record_dicts['DB_ID'] = ['PMID'+':'+pmid]
				#print record_dicts['ID']

		if 'UR' in record_dicts.keys():
			if 'https://www.cochranelibrary.com/central' in record_dicts['UR'][0]:
				ccrct_url = record_dicts['UR'][0]
				ccrct_id = [c for c in ccrct_url.split('/') if c.startswith('CN')][0]
				if len(ccrct_id) !=0:
					record_dicts['DB_ID'] = ['CCRCT'+':'+ccrct_id]
					#print record_dicts['ID']

		
		if 'UR' in record_dicts.keys():
			if 'search.ebscohost.com' in record_dicts['UR'][0]:
				cinahl_url = record_dicts['UR'][0]
				# print cinahl_url
				cinahl_id = [c for c in cinahl_url.split('&') if c.startswith('AN')][0]
				if len(cinahl_id) !=0:
					record_dicts['DB_ID'] = ['CINAHL'+':'+cinahl_id]
					#print record_dicts['ID']

				
		
		if 'L2' in record_dicts.keys():		
			if 'http://ovidsp.ovid.com/ovidweb' in record_dicts['L2'][0]:
				if 'psyc' in record_dicts['L2'][0]:
					psycinfo_url = record_dicts['L2']
					# print psycinfo_url
					if len(psycinfo_url) !=0:
						psycinfo_id = psycinfo_url[0].split('=')[-1]
						if len(psycinfo_id) !=0:
							record_dicts['DB_ID'] = ['PSYCINFO'+':'+psycinfo_id]
							#print record_dicts['ID']


		if 'L2' in record_dicts.keys():		
			if 'http://ovidsp.ovid.com/ovidweb' in record_dicts['L2'][0]:
				if not 'psyc' in record_dicts['L2'][0]:
					ovid_url = record_dicts['L2']
					#print ovid_url
					if len(ovid_url) !=0:
						ovid_id = ovid_url[0].split('=')[-1]
						#print ovid_id
						if len(ovid_id) !=0:
							record_dicts['DB_ID'] = ['OVID'+':'+ovid_id]
							#print record_dicts['ID']





	return list_of_ris_record_dicts				