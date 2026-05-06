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
    result = []
    def traverse(node):
        if node is None:
            return
        traverse(node.l)
        result.append(node.v)
        traverse(node.r)
    traverse(t)
    return result



def _build_right(t, prefix="", is_left=True, first_edge=False):
    if t is None:
        return []

    lines = []
    lines += _build_right(t.r, prefix + ("│   " if is_left else "    "),
                          False, False)

    if first_edge:
        text = prefix + "─── " + str(t.v)
    else:
        text = prefix + ("└── " if is_left else "┌── ") + str(t.v)
    lines.append((text, first_edge))

    lines += _build_right(t.l, prefix + ("    " if is_left else "│   "),
                          True, False)
    return lines


def _build_left(t, prefix="", is_right=True, first_edge=False):
    if t is None:
        return []

    lines = []
    lines += _build_left(t.l, prefix + ("    " if is_right else "   │"),
                         False, False)

    if first_edge:
        text = str(t.v) + " ───" + prefix
    else:
        text = str(t.v) + (" ──┘" if is_right else " ──┐") + prefix
    lines.append((text, first_edge))

    lines += _build_left(t.r, prefix + ("   │" if is_right else "    "),
                         True, False)
    return lines


def _clean_bars(s: str) -> str:
    return s.replace("│", " ")


def print_tree(t: Node) -> None:
    if t is None:
        return

    left_lines = _build_left(t.l, first_edge=True)
    right_lines = _build_right(t.r, first_edge=True)
    root_text = f"[ {t.v} ]"

    left_width = max((len(s) for s, _ in left_lines), default=0)
    total_rows = max(len(left_lines), len(right_lines), 1)

    left_lines = [("", False)] * (total_rows - len(left_lines)) + left_lines
    right_lines = [("", False)] * (total_rows - len(right_lines)) + right_lines

    center_row = total_rows // 2

    for i in range(total_rows):
        left_text, left_first = left_lines[i]
        right_text, right_first = right_lines[i]

        left_text = _clean_bars(left_text)
        right_text = _clean_bars(right_text)

        left_part = left_text.rjust(left_width)
        right_part = right_text

        if i == center_row:
            left_join = " " if left_first else " ─── "
            right_join = " " if right_first else " ─── "
            print(left_part + left_join + root_text + right_join + right_part)
        else:
            print(left_part + "   " + " " * len(root_text) + "   " + right_part)



nums = [8, 5, 6, 4, 3, 11, 13, 9]
root = None
for n in nums:
    root = insert(root, n)

print("In-order:", inorder(root))
print("\nTree:")
print_tree(root)