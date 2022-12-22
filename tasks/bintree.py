class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        
class BinaryTree:
    def __init__(self, root):
        self.root = Node(root)
        
    def print_tree(self, traversal_type):
        if traversal_type == "preorder":
            return self.preorder_print(self.root, "")
        elif traversal_type == "inorder":
            return self.inorder_print(self.root, "")
        elif traversal_type == "postorder":
            return self.postorder_print(self.root, "")
        else:
            print("Traversal type " + str(traversal_type) + " is not supported.")
            return False
        
    def preorder_print(self, start, traversal):
        """Root->Left->Right"""
        if start:
            traversal += (str(start.value) + "->")
            traversal = self.preorder_print(start.left, traversal)
            traversal = self.preorder_print(start.right, traversal)
        return traversal
    
    def inorder_print(self, start, traversal):
        """Left->Root->Right"""
        if start:
            traversal = self.inorder_print(start.left, traversal)
            traversal += (str(start.value) + "->")
            traversal = self.inorder_print(start.right, traversal)
        return traversal
    
    def postorder_print(self, start, traversal):
        """Left->Right->Root"""
        if start:
            traversal = self.postorder_print(start.left, traversal)
            traversal = self.postorder_print(start.right, traversal)
            traversal += (str(start.value) + "->")
        return traversal

    def insert(self, value):
        self.insert_helper(self.root, value)

    def insert_helper(self, current_node, value):
        if value < current_node.value:
            if current_node.left:
                self.insert_helper(current_node.left, value)
            else:
                current_node.left = Node(value)
        else:
            if current_node.right:
                self.insert_helper(current_node.right, value)
            else:
                current_node.right = Node(value)
                
# populate treed

tree = BinaryTree(1)

def populate_tree(tree, num_elems = 10, max_int = 100):
    from random import randint
    for _ in range(num_elems):
        current_elem = randint(0, max_int)
        tree.insert(current_elem)
    return tree

populate_tree(tree, 200**10, 100000)

# print tree

print(tree.print_tree("inorder"))


# reverse tree

def reverse_tree(tree):
    def reverse_helper(node):
        if node:
            node.left, node.right = node.right, node.left
            reverse_helper(node.left)
            reverse_helper(node.right)
    reverse_helper(tree.root)
    return tree

