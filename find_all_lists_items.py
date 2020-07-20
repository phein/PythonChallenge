def index_all(search_list,item):
	indices = list()
	for i in range(len(search_list)):
		if (search_list[i] == item):
			indices.append([i])
		elif isinstance(search_list[i],list):
			for index in index_all(search_list[i],item):
				indices.append([i]+index)
	return indices


list1 = [1,2,3]
list2 = [[[1,2,3],2,[1,2]],[1,2,3]]

print(index_all(list1,2))
print(index_all(list2,2))