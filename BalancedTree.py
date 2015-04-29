import random
class BTree(object):
    def __init__(self, data):
        self.key=data
        self.left=None
        self.right=None
        # -1 means the value is not yet set
        self.depth=-1

    def __str__(self):
        return "( " + str(self.key) + " ( " + str(self.left) + " | " + str(self.right) + "))"


def is_balanced_binary_tree(btree):
    if btree is None:
        return True
    else:
        return (abs(depth(btree.left) - depth(btree.right)) <= 1)\
         and is_balanced_binary_tree(btree.left) and is_balanced_binary_tree(btree.right)




def depth(btree):
    if btree==None:
        return 0
    elif btree.depth != -1:
        return btree.depth
    else:
        btree.depth=1+max(depth(btree.left),depth(btree.right))
        return btree.depth
        

#effcient algorithm, get heights of subtrees and check subtrees if balanced at the same time
def is_balanced_binary_tree2(btree):
    return check_balanced(btree)[0]
    
def check_balanced(btree):
    if btree is None: return True, 0
    left_balanced, left_depth = check_balanced(btree.left)
    right_balanced, right_depth = check_balanced(btree.right)
    btree.depth = 1 + max(left_depth, right_depth)
    return left_balanced and right_balanced and \
        (abs(depth(btree.left) - depth(btree.right)) <= 1), btree.depth


#Testing

#building testcase 1
bt = BTree(random.randint(0, 100))
for c1 in xrange(0,5):
    if c1%2:
        bt2 = BTree(random.randint(0, 100))
        bt2.left = bt
        bt=bt2
    else:
        bt2 = BTree(random.randint(0, 100))
        bt2.right = bt
        bt=bt2
#print bt
print is_balanced_binary_tree(bt)
def make_random_balanced_tree(depth):
    if depth>0:
        tree = BTree(random.randint(0, 100))
        tree.left=make_random_balanced_tree(depth-1)
        tree.right=make_random_balanced_tree(depth-1)
        return tree
    else:
        return None

balanced_tree = make_random_balanced_tree(5)

print is_balanced_binary_tree(balanced_tree)

