class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        if(index == 0):
            return
        
        parent = (index - 1) // 2
        if(self.heap[index] < self.heap[parent]):
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            self.heapify_up(parent)

    def extract_min(self):
        if not self.heap:
            return None

        root = self.heap[0]
        val = self.heap.pop()

        if self.heap:
            self.heap[0] = val
            self.heapify_down(0)

        return root

    def heapify_down(self, index):
        left = index * 2 + 1
        right = index * 2 + 2
        smallest = index
        
        if(left < len(self.heap) and self.heap[left] < self.heap[smallest]):
            smallest = left

        if(right < len(self.heap) and self.heap[right] < self.heap[smallest]):
            smallest = right

        if(smallest != index):
            self.heap[smallest], self.heap[index] = self.heap[index], self.heap[smallest]
            self.heapify_down(smallest)

    def is_empty(self):
        return len(self.heap) == 0