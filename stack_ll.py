class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, element):
        new_node = Node(element)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def insert(self, index, element):
        new_node = Node(element)
        if index == 0:
            new_node.next = self.head
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
            if self.head is None:
                self.tail = None
            return

        current = self.head
        while current.next:
            if current.next.value == value:
                if current.next == self.tail:
                    self.tail = current
                current.next = current.next.next
                return
            current = current.next

        print("Value not found in the list")

    def pop(self, index=None):
        if self.head is None:
            print("List is empty")
            return None
        if index is None:
            check = True
        else:
            check = False
        if check is True:
            if self.head == self.tail:
                value = self.head.value
                self.head = None
                self.tail = None
                return value

            current = self.head
            while current.next != self.tail:
                current = current.next

            value = self.tail.value
            current.next = None
            self.tail = current
            return value

        elif check is False:
           if index == 0:
            value = self.head.value
            self.head = self.head.next
            if self.head is None:
                self.tail = None
            return value

        current = self.head
        pos = 0
        while current.next and pos < index - 1:
            current = current.next
            pos += 1

        if current.next is None:
            print("Index out of bounds")
            return None

        value = current.next.value
        current.next = current.next.next
        if current.next is None:
            self.tail = current
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
            while current.next:
                if current.value > current.next.value:
                    current.value, current.next.value = current.next.value, current.value
                current = current.next
        return
    
    def index(self, value):
        current = self.head
        index1 = 0
        while current != None:
            if current.value == value:
                return index1
            index1 +=1
            current = current.next

    def extend(self, other_list):
        current = other_list.head
        while current:
            self.append(current.value)
            current = current.next
    
    def copy(self):
        new_list = Linked_List()
        current = self.head
        while current != None:
            new_list.append(current.value)
            current = current.next
        return new_list
    
    def __len__(self):
        return self.count()
    
class Stack:
    def __init__(self):
        self.__items = Linked_List()

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        return self.__items.pop()

    def is_empty(self):
        if len(self.__items) == 0:
            return True
        return False

    def size(self):
        return len(self.__items)

s = Stack()
s.push(10)
s.push(20)
s.push(30)
print(s.pop())
print(s.size())
print(s.is_empty())
