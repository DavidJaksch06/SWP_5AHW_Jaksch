import random


class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
        self.length += 1

    def __len__(self):
        return self.length

    def __iter__(self):
        current = self.head
        while current:
            yield current.value
            current = current.next

    def print_list(self):
        print(" - ".join(map(str, self)))

def main():
    linked_list = LinkedList()
    for _ in range(10):
        linked_list.append(random.randint(1, 100))

    print("Länge der Liste:", len(linked_list))
    linked_list.print_list()

if __name__ == "__main__":
    main()