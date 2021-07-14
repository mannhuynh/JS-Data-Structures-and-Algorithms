class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        self.value = value
        new_node = Node(self.value)

        self.head = new_node
        self.tail = self.head
        self.length = 1

    def push(self, value):
        new_node = Node(value)
        if not(self.head):
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        return self

    def pop(self):
        if not(self.head):
            return None

        temp = self.head
        pre = self.head

        while temp.next:
            pre = temp
            temp = temp.next

        self.tail = pre
        self.tail.next = None
        self.length -= 1

        if self.length == 0:
            self.head = None
            self.tail = None

        return temp


first_node = LinkedList(4)
print(first_node.value)
print(first_node.head.value)
first_node.push(5)
print('-------')
print(first_node.value)
print(first_node.head.value)
print(first_node.tail.value)
print(first_node.tail.next)
first_node.push(6)
print('-------')
print(first_node.value)
print(first_node.head.value)
print(first_node.head.next.value)
print(first_node.tail.value)
print(first_node.tail.next)
print(first_node.length)
print('===========')
first_node.pop()
print(first_node.value)
print(first_node.head.value)
print(first_node.head.next.value)
print(first_node.tail.value)
print(first_node.tail.next)
print(first_node.length)
