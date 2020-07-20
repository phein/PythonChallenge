import pickle

def save_dict(dict_to_save,file_path):
	with open(file_path,'wb') as file:
		pickle.dump(dict_to_save,file)

def load	_dict(file_path):
	with open(file_path,'rb') as file:
		return pickle.load(file)


# td = {1:'a', 2:'b', 3:'c'}
# save_dict(td,'td.pickle')
# recovered = load_dict('td.pickle')
# print(recovered)