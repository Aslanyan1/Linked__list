class Node:
    def __init__(self, value, next=None, prev=None):
        self.value = value
        self.next = next
        self.prev = prev


class Double_Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, element):
        new_node = Node(element)
        if self.head is None:
            self.head = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
        self.tail = new_node

    def insert(self, index, element):
        new_node = Node(element)
        if index == 0:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            if self.tail is None:
                self.tail = new_node
            return
        current = self.head
        pos = 0
        while current and pos < index - 1:
            current = current.next
            pos += 1
        if current is None:
            print("Index out of bounds")
            return
        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node
        if new_node.next is None:
            self.tail = new_node

    def print_list(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

    def remove(self, value):
        if self.head is None:
            print("List is empty")
            return
        if self.head.value == value:
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            return
        current = self.head
        while current:
            if current.value == value:
                if current.next:
                    current.next.prev = current.prev
                if current.prev:
                    current.prev.next = current.next
                if current == self.tail:
                    self.tail = current.prev
                return
            current = current.next
        print("Value not found in the list")

    def pop(self, index=None):
        if self.head is None:
            print("List is empty")
            return None
        if index is None:
            if self.tail == self.head:
                value = self.head.value
                self.head = None
                self.tail = None
                return value
            value = self.tail.value
            self.tail = self.tail.prev
            self.tail.next = None
            return value
        if index == 0:
            value = self.head.value
            self.head = self.head.next
            if self.head:
                self.head.prev = None
            else:
                self.tail = None
            return value
        current = self.head
        pos = 0
        while current and pos < index:
            current = current.next
            pos += 1
        if current is None:
            print("Index out of bounds")
            return None
        value = current.value
        if current.prev:
            current.prev.next = current.next
        if current.next:
            current.next.prev = current.prev
        if current == self.tail:
            self.tail = current.prev
        return value

    def count(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def clear(self):
        self.head = None
        self.tail = None

    def sort(self):
        n = self.count()
        for _ in range(n):
            current = self.head
            while current and current.next:
                if current.value > current.next.value:
                    current.value, current.next.value = current.next.value, current.value
                current = current.next

    def index(self, value):
        current = self.head
        index1 = 0
        while current:
            if current.value == value:
                return index1
            index1 += 1
            current = current.next

    def extend(self, other_list):
        current = other_list.head
        while current:
            self.append(current.value)
            current = current.next

    def copy(self):
        new_list = Double_Linked_List()
        current = self.head
        while current:
            new_list.append(current.value)
            current = current.next
        return new_list

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
            return
        self.tail.next = new_node
        new_node.prev = self.tail
        self.tail = new_node


ll = Double_Linked_List()
ll.append(555)
ll.append(2)
ll.append(5)
ll.insert(1, 100)
ll2 = Double_Linked_List()
ll2.append(7)
ll2.append(8)
ll.clear()
print(ll.count())
ll2.extend(ll)
ll2.print_list()
print(ll.sort())
print(ll.index(5))
ll2 = ll.copy()
ll2.print_list()
ll.print_list()
