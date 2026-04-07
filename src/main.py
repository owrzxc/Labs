class BinaryTree:
    def __init__(self, value, left=None, right=None, parent=None):
        self.value = value
        self.left = left
        self.right = right
        self.parent = parent


def find_successor(tree: BinaryTree, node: BinaryTree) -> BinaryTree | None:
    if node.right is not None:
        cur = node.right
        while cur.left is not None:
            cur = cur.left
        return cur

    cur = node
    parent = cur.parent
    while parent is not None and parent.right is cur:
        cur = parent
        parent = parent.parent

    return parent
