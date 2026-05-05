class Node:
    def __init__(self, v):
        self.v = v
        self.l = None
        self.r = None

def insert(t, x):
    if t is None:
        return Node(x)
    if x < t.v:
        t.l = insert(t.l, x)
    else:
        t.r = insert(t.r, x)
    return t

def inorder(t):
    return inorder(t.l) + [t.v] + inorder(t.r) if t else []

def print_tree(t, prefix="", is_left=True):
    if t:
        print_tree(t.r, prefix + ("│   " if is_left else "    "), False)
        print(prefix + ("└── " if is_left else "┌── ") + str(t.v))
        print_tree(t.l, prefix + ("    " if is_left else "│   "), True)

nums = [8, 5, 6, 4, 3, 11, 13, 9]
root = None

for n in nums:
    root = insert(root, n)

print("In-order:", inorder(root))
print("\nTree:")
print_tree(root)