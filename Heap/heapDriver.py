class Heap:
    """
    Heap is a class for representing heap data types.
    Implements heap data type.
    
    Properties:
        h - a list in which the data is stored
        heap_size - the size of the heap
    
    Methods:
        __init__ - constructor for the Heap class, accepts numeric arrays as an input
        heap_sort - method for performing sorting, runtime O(nlogn)
        heap_maximum - returns maximum in the heap
        heap_extract_max - extracts maximum value from the heap
        heap_increase_key - increases the key in the position i
        max_key_insert - inserts a key in the heap
    """
    
    def __init__(self, a):
        self.h = a
        self.heap_size = len(a)
        for i in range(self.heap_size // 2, 0, -1):
            self.max_heapify(i)
    
    def heap_sort(self):
        b = [0] * self.heap_size
        for i in range(self.heap_size, 0, -1):
            temp = self.h[0]
            self.h[0] = self.h[i - 1]
            self.h[i - 1] = temp
            b[i - 1] = self.h[i - 1]
            self.h.pop()
            self.heap_size -= 1
            self.max_heapify(1)
        return b
    
    def heap_maximum(self):
        return self.h[0]
    
    def heap_extract_max(self):
        if self.heap_size < 1:
            raise Exception('heap underflow')
        max_val = self.heap_maximum()
        self.h[0] = self.h[self.heap_size - 1]
        self.h.pop()
        self.heap_size -= 1
        self.max_heapify(1)
        return max_val
    
    def heap_increase_key(self, i, key):
        if key < self.h[i - 1].key:
            raise Exception('new key is smaller than current key')
        self.h[i - 1].key = key
        while i > 1 and self.h[self.parent(i) - 1].key < self.h[i - 1].key:
            temp = self.h[i - 1]
            self.h[i - 1] = self.h[self.parent(i) - 1]
            self.h[self.parent(i) - 1] = temp
            i = self.parent(i)
    
    def max_key_insert(self, obj):
        self.heap_size += 1
        self.h.append(obj)
        self.h[self.heap_size - 1].key = -float('inf')
        self.heap_increase_key(self.heap_size, obj.key)
    
    def max_heapify(self, i):
        l = self.left(i)
        r = self.right(i)
        if l <= self.heap_size and self.h[l - 1].key > self.h[i - 1].key:
            largest = l
        else:
            largest = i
        if r <= self.heap_size and self.h[r - 1].key > self.h[largest - 1].key:
            largest = r
        if largest != i:
            temp = self.h[i - 1]
            self.h[i - 1] = self.h[largest - 1]
            self.h[largest - 1] = temp
            self.max_heapify(largest)
    
    @staticmethod
    def left(i):
        return 2 * i
    
    @staticmethod
    def right(i):
        return 2 * i + 1
    
    @staticmethod
    def parent(i):
        return i // 2

if __name__ == "__main__":
    h = Heap([1, 2, 3, 4, 5, 6, 8, 7])
    
    mx = h.heap_maximum()
    print(f"Maximum: {mx}")
    
    h.heap_extract_max()
    print(f"Heap after extracting max: {h.h}")
    
    h.heap_increase_key(3, 11)
    print(f"Heap after increasing key: {h.h}")
    
    h.max_key_insert(1.5)
    print(f"Heap after inserting key: {h.h}")
    
    b = h.heap_sort()
    print(f"Sorted heap: {b}")
