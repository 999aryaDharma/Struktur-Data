class Node:
    def __init__(self, value, nextNode=None):
        self.value = value
        self.nextNode = nextNode

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)

    def append(self, data):
        new_node = Node(data)
        cur = self.head
        while cur.nextNode is not None:
            cur = cur.nextNode
        cur.nextNode = new_node

    def length(self):
        cur = self.head
        total = 1  # Mulai dengan 1 karena head sudah ada
        while cur.nextNode is not None:
            total += 1
            cur = cur.nextNode
        return total

    def display(self):
        elems = []
        cur_node = self.head
        while cur_node.nextNode is not None:
            cur_node = cur_node.nextNode
            elems.append(cur_node.value)
        print(elems)

    def get(self, index):
        if index >= self.length():
            print("ERROR: 'Get' Index out of range")
            return None
        cur_idx = 0
        cur_node = self.head.nextNode
        while cur_node is not None:
            if cur_idx == index:
                return cur_node.value
            cur_node = cur_node.nextNode
            cur_idx += 1

    def erase(self, index):
        if index >= self.length():
            print("ERROR: 'Erase' Index out of range")
            return None
        cur_idx = 0
        cur_node = self.head
        while True:
            last_node = cur_node
            cur_node = cur_node.nextNode
            if cur_idx == index:
                last_node.nextNode = cur_node.nextNode
                return None
            cur_idx += 1


# Contoh penggunaan
my_list = LinkedList(0)  # Inisialisasi linked list dengan nilai 0
my_list.display()  # Akan mencetak []

my_list.append(1)
my_list.append(2)
my_list.append(3)
my_list.append(4)

my_list.display()

my_list.erase(1)

my_list.display()
# print("Element at 2nd index : %d" % my_list.get(2))
