class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertBeginning(self, data):
        new_node = Node(data)
        if self.head:
            new_node.next = self.head
            self.head.prev = new_node
        self.head = new_node

    def insertEnd(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node
            new_node.prev = current

    def remove_node(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                return
            current = current.next

    def insertAtIndex(self, data, index):
        new_node = Node(data)
        if index == 0:
            self.insertBeginning(data)
        else:
            current = self.head
            for i in range(index - 1):
                if current:
                    current = current.next
                else:
                    raise IndexError("Index out of range")
            if current:
                new_node.next = current.next
                new_node.prev = current
                if current.next:
                    current.next.prev = new_node
                current.next = new_node
            else:
                raise IndexError("Index out of range")

    def removeAll(self):
        self.head = None

    def traverse(self):
        current = self.head
        while current:
            print(current.data, end=" <-> ")
            current = current.next
        print("None")


# Membuat objek doubly linked list
dllist = DoublyLinkedList()

# Menyisipkan beberapa elemen di awal
dllist.insertBeginning(4)
dllist.insertBeginning(3)
dllist.insertBeginning(2)
dllist.insertBeginning(1)
dllist.traverse()
# Menyisipkan elemen di akhir
dllist.insertEnd(5)

# Menghapus elemen dengan nilai 3
dllist.remove_node(3)
dllist.removeAll()
# Mencetak seluruh elemen doubly linked list
dllist.traverse()  # Output: 1 <-> 2 <-> 4 <-> 5 <-> None
