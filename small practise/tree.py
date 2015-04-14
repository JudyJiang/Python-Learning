class BinaryTree:
	def __init__(self,value):
		self.value = value
		self.left = None
		self.right = None



	def insert(self, value):
		if self.value < value:
			if self.right is None:
				self.right = BinaryTree(value)
			else:
				self.right.insert(value)
		else:
			if self.left is None:
				self.left = BinaryTree(value)
			else:
				self.left.insert(value)

	def traverse(self):
		if self is None:
			return 
		if self.left is None:
			left = '-'
		else:
			left = self.left.traverse()

		if self.right is None:
			right = '-'
		else:
			right = self.right.traverse()

		#return (left, self.value, right)
		curr = (left, str(self.value), right)
		res = ','.join(curr)
		res = '(' + res + ')'
		return res



root = BinaryTree(nodes[0])
for node in nodes[1:]:
	root.insert(node)

res = root.traverse()
print res


















