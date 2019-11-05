## python dict to list
def dict_to_ris(python_dictionary):
	line_list = []
	for k in python_dictionary.keys():
		#print(k, '-', python_dictionary[k])
		if len(python_dictionary[k]) == 1:
			line = k+' - '+python_dictionary[k][0]
			line_list.append(line)
		else:
			for l in python_dictionary[k]:
				line = k+' - '+l
				line_list.append(line)
	return line_list
		