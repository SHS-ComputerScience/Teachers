class BinaryTree():
	# constructor
	def __init__(self,rootid):
		# attributes
		self.left = None
		self.right = None
		self.rootid = rootid

	# methods
	def get_left_child(self):
		return self.left

	def get_right_child(self):
		return self.right

	def set_node_value(self,value):
		self.rootid = value

	def get_node_value(self):
		return self.rootid

	def insert_right(self,new_node):
		if self.right == None:
			self.right = BinaryTree(new_node)
		else:
			tree = BinaryTree(new_node)
			tree.right = self.right
			self.right = tree

	def insert_left(self,new_node):
		if self.left == None:
			self.left = BinaryTree(new_node)
		else:
			tree = BinaryTree(new_node)
			self.left = tree
			tree.left = self.left


def print_tree(tree):
	if tree != None:
		print(tree.get_left_child())
		print(tree.get_node_value())
		print(tree.get_right_child())

# test tree
def test_tree():
	my_tree = BinaryTree("Maud")
	my_tree.insert_left("Bob")
	my_tree.insert_right("Tony")
	my_tree.insert_right("Steven")
	print_tree(my_tree)

test_tree()