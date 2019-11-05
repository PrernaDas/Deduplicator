from collections import defaultdict

def partitition_on_year(list_of_dicts):
	"""
	Partitions the dictionaries in a list based on if there a year value or not
	"""

	year_pool = [] # list of dictionaries with some year value, l['YEAR'] ='2019'
	
	no_year_pool = [] # list of dictionaries with no year value, l['YEAR']=''
	
	for l in list_of_dicts:
		if l['YEAR'] is not None:
				year_pool.append(l)
		else:	
			no_year_pool.append(l)

	
	#print(len(year_pool))
	#print(len(no_year_pool))
	
	# get all the unique year values in the year_pool	
	years = []
	for m in year_pool:
		if not m['YEAR'] in years:
			years.append(m['YEAR'])

	#print(len(years))

	years_sorted = sorted(years) 
	


	return years_sorted, no_year_pool, year_pool

		













	