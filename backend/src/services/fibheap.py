import math

class Node:
    def __init__(self, val):
        self.val = val
        self.children = []
        self.size = 0

    def add(self, val):
        self.children.append(val)
        self.size += 1

class FibonacciHeap:
    def __init__(self):
        self.min = None
        self.size = 0
        self.nodes = []

    def insert(self, val):
        node = Node(val)
        
        if self.min is None or val < self.min.val:
            self.min = node

        self.nodes.append(node)
        self.size += 1

    def heapify(self):
        if self.size <= 1:
            return

        max = math.frexp(self.size)[1]
        temp = [None] * max

        while self.nodes != []:
            x = self.nodes.pop(0)
            size = x.size
            while temp[size] is not None:
                y = temp[size]
                if x.val > y.val:
                    x, y = y, x
                x.add(y)
                temp[size] = None
                size += 1
            temp[size] = x
        
        self.min = None
        self.nodes = []
        for node in temp:
            if node is not None:
                self.nodes.append(node)
                if self.min is None or node.val < self.min.val:
                    self.min = node


    def extract_min(self):
        if self.min is None:
            return None

        smallest = self.min
        if smallest is not None:
            for child in smallest.children:
                self.nodes.append(child)
            
            self.nodes.remove(smallest)

            if self.nodes:
                self.min = self.nodes[0]
                self.heapify()
            else:
                self.min = None
            
            self.size -= 1
        return smallest.val
    
    def is_empty(self):
        return self.size == 0