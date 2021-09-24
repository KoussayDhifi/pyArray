import random
import string

def create_array(type,length):
	T=[]
	for i in range(length):
		if type == 'int':
			T.append(random.randint(0,999))
		elif type == 'str':
			letters = list(string.ascii_letters)
			T.append(letters[random.randint(0,51)])
		elif type == 'bool':
			boolea = [True,False]
			T.append(boolea[random.randint(0,1)])
		elif type == 'float':
			T.append(random.uniform(0,90))
		else:
			print("Please add a valid datatype between a '' ")
			return 0
	return T


M = create_array('float',5)
for i in range(5):
	M[i] = str(input(f"M[{i}] = "))

print(M)

