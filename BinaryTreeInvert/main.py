class Tree:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

top_tree = Tree(0, None, None)

tree_left = Tree(1, None, None)
top_tree.left = tree_left

tree_right = Tree(2, None, None)
top_tree.right = tree_right

tree_left_left = Tree(3, None, None)
tree_left_right = Tree(4, None, None)
tree_left.left = tree_left_left
tree_left.right = tree_left_right

tree_right_left = Tree(5, None, None)
tree_right_right = Tree(6, None, None)
tree_right.left = tree_right_left
tree_right.right = tree_right_right

def invert_tree(tree_left: Tree, tree_right: Tree):
    if not tree_left or not tree_right:
        return
    
    invert_tree(tree_left.left, tree_right.left)
    invert_tree(tree_left.right, tree_right.right)

    tmp = tree_left.value
    tree_left.value = tree_right.value
    tree_right.value = tmp

invert_tree(top_tree.left, top_tree.right)

print(top_tree.value)
print("L: " + str(top_tree.left.value))
print("R: " + str(top_tree.right.value))
print("LL: " + str(tree_left.left.value))
print("LR: " + str(tree_left.right.value))
print("RL: " + str(tree_right.left.value))
print("RR: " + str(tree_right.right.value))