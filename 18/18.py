class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __str__(self):
        return f'{self.data}'

class Deque:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def push_front(self, data):
        new = Node(data)
        if self.size == 0:
            self.head = new
            self.tail = new
        else:
            self.head.prev = new
            new.next = self.head
            self.head = new
        print('ok')
        self.size+=1

    def push_back(self, data):
        new = Node(data)
        if self.size == 0:
            self.head = new
            self.tail = new
        else:
            self.tail.next = new
            new.prev = self.tail
            self.tail = new
        print('ok')
        self.size+=1

    def pop_front(self):
        if self.size==0:
            self.error()
        else:
            print(self.head)
            self.head = self.head.next
            self.size-=1

    def pop_back(self):
        if self.size==0:
            self.error()
        else:
            print(self.tail)
            self.tail = self.tail.prev
            self.size-=1

    def front(self):
        if self.size==0:
            self.error()
        else:
            print(self.head)

    def back(self):
        if self.size==0:
            self.error()
        else:
            print(self.tail)

    def print_size(self):
        print(self.size)

    def clear(self):
        self.tail = self.head = None
        self.size = 0
        print('ok')

    def error(self):
        print('error')

deque = Deque()
while True:
    s = input()
    if s == 'exit':
        print('bye')
        break
    if s[:6] == 'push_b':
        deque.push_back(int(s.split()[-1]))
    if s[:6] == 'push_f':
        deque.push_front(int(s.split()[-1]))
    if s == 'pop_front':
        deque.pop_front()
    if s == 'pop_back':
        deque.pop_back()
    if s == 'front':
        deque.front()
    if s == 'back':
        deque.back()
    if s == 'size':
        deque.print_size()
    if s == 'clear':
        deque.clear()
