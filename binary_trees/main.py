from binary_tree import BinaryTree

"""
    Create an array with the numbers to add to the tree

    Fernando Valdeon 
    Marco Toress
    Diego Araque 
    Uriel Aguilar
"""


NUMBERS = [ 11,6,8,19,4,10,5,17,43,49,31 ]

# Iterate through numbers and add the binary tree 
# At the beggining the tree has no nodes
tree = BinaryTree()
for n in NUMBERS:
    tree.insert(n)


#Print tree line by line
print("Line By Line ___________________________________")
print(tree.levelByLevel())