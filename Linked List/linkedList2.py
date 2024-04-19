class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBegin(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node

    def insertAtIndex(self, data, index):
        new_node = Node(data)
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            for i in range(index - 1):
                if current is None:
                    raise IndexError("Index out of range")
                current = current.next
            new_node.next = current.next
            current.next = new_node

    def insertAtEnd(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def remove_node(self, data):
        current = self.head
        if current is None:
            raise ValueError("List is empty")
        if current.data == data:
            self.head = current.next
            return
        while current.next:
            if current.next.data == data:
                current.next = current.next.next
                return
            current = current.next
        raise ValueError(f"Data {data} not found in the list")

    def sizeOfLL(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def printLL(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def search(self, target_data):
        current = self.head
        index = 0
        while current:
            if current.data == target_data:
                return index
            current = current.next
            index += 1
        return -1

    def remove_all(self):
        """
        Removes all nodes from the linked list.
        """
        self.head = None


# Contoh penggunaan
ll = LinkedList()
ll.insertAtBegin(10)
ll.printLL()
ll.insertAtBegin(20)
ll.printLL()
ll.insertAtEnd(30)
ll.printLL()
ll.insertAtIndex(25, 1)
ll.printLL()
# ll.remove_node(20)


# print("Linked list sebelum penghapusan:")
# ll.printLL()
# # Hapus semua simpul
# ll.remove_all()
# print("\nLinked list setelah penghapusan:")
# ll.printLL()

# # Cari data 20
# index = ll.search(20)
# if index != -1:
#     print(f"Data 20 ditemukan pada indeks {index}")
# else:
#     print("Data 20 tidak ditemukan dalam daftar")

# print("Linked list sebelum penghapusan:")
# ll.printLL()
# # Hapus simpul dengan nilai data 20
# ll.remove_node()
# print("\nLinked list setelah penghapusan:")
# ll.printLL()
