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
        """
        Constructor for the Heap class.
        
        Args:
            a (list): A list of numeric values to initialize the heap.
        """
        self.h = a  # Initialize the heap with the given list
        self.heap_size = len(a)  # Set the size of the heap
        for i in range(self.heap_size // 2, 0, -1):
            self.max_heapify(i)  # Build the max heap

    def heap_sort(self):
        """
        Method for performing heap sort.
        
        Returns:
            list: A sorted list in ascending order.
        """
        b = [0] * self.heap_size  # Initialize an array for the sorted elements
        for i in range(self.heap_size, 0, -1):
            temp = self.h[0]  # Swap the root (maximum value) with the last element
            self.h[0] = self.h[i - 1]
            self.h[i - 1] = temp
            b[i - 1] = self.h[i - 1]  # Place the maximum element at the end of the sorted array
            self.h.pop()  # Remove the last element
            self.heap_size -= 1  # Decrease the heap size
            self.max_heapify(1)  # Restore the heap property
        return b
    
    def heap_maximum(self):
        """
        Returns the maximum element in the heap.
        
        Returns:
            numeric: The maximum element.
        """
        return self.h[0]  # The maximum element is at the root
    
    def heap_extract_max(self):
        """
        Extracts the maximum value from the heap.
        
        Returns:
            numeric: The maximum value.
        
        Raises:
            Exception: If the heap is empty.
        """
        if self.heap_size < 1:
            raise Exception('heap underflow')
        max_val = self.heap_maximum()  # Get the maximum element
        self.h[0] = self.h[self.heap_size - 1]  # Move the last element to the root
        self.h.pop()  # Remove the last element
        self.heap_size -= 1  # Decrease the heap size
        self.max_heapify(1)  # Restore the heap property
        return max_val
    
    def heap_increase_key(self, i, key):
        """
        Increases the key at position i to a new value.
        
        Args:
            i (int): The index of the element to be increased.
            key (numeric): The new key value.
        
        Raises:
            Exception: If the new key is smaller than the current key.
        """
        if key < self.h[i - 1].key:
            raise Exception('new key is smaller than current key')
        self.h[i - 1].key = key  # Set the new key
        while i > 1 and self.h[self.parent(i) - 1].key < self.h[i - 1].key:
            temp = self.h[i - 1]  # Swap the element with its parent
            self.h[i - 1] = self.h[self.parent(i) - 1]
            self.h[self.parent(i) - 1] = temp
            i = self.parent(i)  # Move up the heap
    
    def max_key_insert(self, obj):
        """
        Inserts a new key into the heap.
        
        Args:
            obj (object): The object with a key attribute to be inserted.
        """
        self.heap_size += 1  # Increase the heap size
        self.h.append(obj)  # Add the new element to the end of the heap
        self.h[self.heap_size - 1].key = -float('inf')  # Initialize the key to negative infinity
        self.heap_increase_key(self.heap_size, obj.key)  # Increase the key to its correct value
    
    def max_heapify(self, i):
        """
        Maintains the max-heap property.
        
        Args:
            i (int): The index to be heapified.
        """
        l = self.left(i)  # Get the left child index
        r = self.right(i)  # Get the right child index
        if l <= self.heap_size and self.h[l - 1].key > self.h[i - 1].key:
            largest = l  # If left child is larger, update largest
        else:
            largest = i  # Else, current node is largest
        if r <= self.heap_size and self.h[r - 1].key > self.h[largest - 1].key:
            largest = r  # If right child is larger, update largest
        if largest != i:
            temp = self.h[i - 1]  # Swap the element with the largest child
            self.h[i - 1] = self.h[largest - 1]
            self.h[largest - 1] = temp
            self.max_heapify(largest)  # Recursively heapify the affected sub-tree
    
    @staticmethod
    def left(i):
        """
        Returns the index of the left child.
        
        Args:
            i (int): The index of the parent.
        
        Returns:
            int: The index of the left child.
        """
        return 2 * i
    
    @staticmethod
    def right(i):
        """
        Returns the index of the right child.
        
        Args:
            i (int): The index of the parent.
        
        Returns:
            int: The index of the right child.
        """
        return 2 * i + 1
    
    @staticmethod
    def parent(i):
        """
        Returns the index of the parent.
        
        Args:
            i (int): The index of the child.
        
        Returns:
            int: The index of the parent.
        """
        return i // 2

if __name__ == "__main__":
    h = Heap([1, 2, 3, 4, 5, 6, 8, 7])
    
    mx = h.heap_maximum()  # Get the maximum value in the heap
    print(f"Maximum: {mx}")
    
    h.heap_extract_max()  # Extract the maximum value
    print(f"Heap after extracting max: {h.h}")
    
    h.heap_increase_key(3, 11)  # Increase the key of the 3rd element to 11
    print(f"Heap after increasing key: {h.h}")
    
    h.max_key_insert(1.5)  # Insert a new key with value 1.5
    print(f"Heap after inserting key: {h.h}")
    
    b = h.heap_sort()  # Perform heap sort
    print(f"Sorted heap: {b}")
