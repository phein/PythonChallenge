def sort_a_string(s):
	words = s.split()
	words = [w.lower() + w for w in words]
	words.sort()
	#cut in half to get the orginal strings
	words = [w[len(w)//2:] for w in words]
	print(words)
	return ' '.join(words)

	
#print(sort_a_string("oranges apple banana"))
#rint(sort_a_string("table Chair whiteboard"))
