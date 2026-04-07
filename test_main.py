from main import BinaryTree, find_successor

def build_example_tree():

    root = BinaryTree(10)
    node5 = BinaryTree(5, parent=root)
    node15 = BinaryTree(15, parent=root)
    root.left = node5
    root.right = node15

    node3 = BinaryTree(3, parent=node5)
    node7 = BinaryTree(7, parent=node5)
    node5.left = node3
    node5.right = node7

    node20 = BinaryTree(20, parent=node15)
    node15.right = node20

    node12 = BinaryTree(12, parent=node20)
    node20.left = node12

    return root, node7

if __name__ == "__main__":
    root, node7 = build_example_tree()
    succ = find_successor(root, node7)
    if succ is not None:
        print("Successor of 7 is:", succ.value)
    else:
        print("Successor of 7 does not exist")