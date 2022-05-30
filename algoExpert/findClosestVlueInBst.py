class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

a = BST(10)
b = BST(5)
c = BST(15)
d = BST(2)
e = BST(1)
f = BST(5)
g = BST(13)
h = BST(22)
j = BST(14)

a.left = b
a.right = c
b.left = d
b.right = f
d.left = e
c.left = g
c.right = h
g.left = j



def findClosesValueInBts(tree, target):
    return findClosesValueBstHelper(tree, target, tree.value)

def findClosesValueBstHelper(tree,target,closest):
    if tree is None:
        return closest
    if(abs(target - closest) > abs(target - tree.value)):
        closest = tree.value
    if(target < tree.value):
        return findClosesValueBstHelper(tree.left, target, closest)
    elif target > tree.value:
        return findClosesValueBstHelper(tree.right,target,closest)
    else: return closest



print(findClosesValueInBts(a, 12))
