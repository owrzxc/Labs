from red_black_priority_queue import RedBlackPriorityQueue


if __name__ == "__main__":
    queue = RedBlackPriorityQueue()
    queue.insert("A", 4)
    queue.insert("B", 9)
    queue.insert("C", 2)
    queue.insert("D", 7)

    print("Черга:", queue.to_list())
    print("Найвищий пріоритет:", queue.peek())
    print("Видалено:", queue.extract_max())
    print("Після видалення:", queue.to_list())