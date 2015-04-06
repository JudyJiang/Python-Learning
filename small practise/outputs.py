#TODO:
#Don't have a unified way to do it..

def replace_output(input, **kwargs):
	try:
		if input is True:
			return 'Y'
		elif input is False:
			return 'N'
		else:
			return kwargs[input]
	except ValueError:
		return None #dictinoary non value


#TODO: maybe can use closure here
def output_formats(return_type):
	def fun1():
		pass

	def func2():
		pass

	#return based on return_type


def add_to_tree(root, value_string):
	for value in value_string:
		root = root.setdefault(value, {})
#this is interesting, 
#everytime inside the for loop, loop is actuall a dictionary which gets updated
#example, value_string='abc'
#in the first run 'root' is an empty dictionary, {}, then root = {a:{}}
#in the second run 'root' is {a:{}} and put 'b' as its children's key-value

my_string = 'abc'
tree = {}
add_to_tree(tree, my_string)
print (tree)