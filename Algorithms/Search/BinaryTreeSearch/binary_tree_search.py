# Binary Tree Search Algorithm

def binary_tree_search(item_sought, current_node):

	if current_node == None:
		return False
	else:
		if item_sought == current_node:
			return True
		else:
			if item_sought < current_node:
				if current_node.left != None:
					return binary_tree_search(item_sought, current_node.left)
				else:
					return False

				if current_node.right != None:
					return binary_tree_search(item_sought, current_node.right)
				else:
					return False

# test
import binary_tree