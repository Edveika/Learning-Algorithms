# 👨‍💻 Learning-Algorithms

Spending some extra time to better understand algorithms.

# 📑 Courses taken

* [freeCodeCamp's Algorithms and Data Structures](https://github.com/Edveika/Learning-Algorithms/blob/main/freeCodeCamp/freeCodeCamp.md)

# 🌳 Inverted a binary tree!

Inverted a binary tree using a recursive function for fun🤷‍♂️

```
def invert_tree(tree_left: Tree, tree_right: Tree):
    if not tree_left or not tree_right:
        return
    
    invert_tree(tree_left.left, tree_right.left)
    invert_tree(tree_left.right, tree_right.right)

    tmp = tree_left.value
    tree_left.value = tree_right.value
    tree_right.value = tmp
```
