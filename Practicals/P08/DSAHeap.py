import numpy as np

class _DSAHeapEntry:
    def __init__(self, priority, value):
        self._priority = priority
        self._value = value
    
    def __str__(self):
        return str(self._priority) + ", " + self._value
    
class DSAHeap:  # Max Heap
    def __init__(self, max_size):
        self.heap = np.zeros(max_size, dtype=object)
        self.count = 0
    
    def add(self, priority, value):
        self.heap[self.count] = _DSAHeapEntry(priority, value)
        self.trickle_up(self.count)
        self.count += 1
        
    def remove(self):
        return_value = self.heap[0]._value
        self.count -= 1
        
        self.heap[0] = self.heap[self.count]
        self.heap[self.count] = None
        self.trickle_down(0)
        
        return return_value
    
    # Reversed Order
    def heap_sort(self, array):
        self.count = len(array)
        self.heap = np.zeros(self.count, dtype=object)
        
        if isinstance(array[0][0], int):
            for i in range(self.count):
                self.heap[i] = _DSAHeapEntry(int(array[i][0]), array[i][1])
        else:
            raise Exception("Invalid array import for heap sort method.")
        
        for i in range(int((self.count / 2)) - 1, -1, -1):
            self.trickle_down(i)
            
        for i in range(self.count - 1, 0, -1):
            temp = self.heap[0]
            self.heap[0] = self.heap[i]
            self.heap[i] = temp
            
            self.count = i
            self.trickle_down(0)
            
        self.count = len(array)
        return self.heap
    
    def trickle_up(self, index):
        parent_index = self._get_parent_idx(index)
        
        if index > 0 and self.heap[index]._priority > self.heap[parent_index]._priority:
            temp = self.heap[parent_index]
            self.heap[parent_index] = self.heap[index]
            self.heap[index] = temp
            
            self.trickle_up(parent_index)
    
    def trickle_down(self, index):
        left_index = self._get_left_child_idx(index)
        right_index = self._get_right_child_idx(index)
        
        if left_index < self.count:
            large_index = left_index
            if right_index < self.count:
                if self.heap[left_index]._priority < self.heap[right_index]._priority:
                    large_index = right_index
        
            if self.heap[large_index]._priority > self.heap[index]._priority:
                temp = self.heap[large_index]
                self.heap[large_index] = self.heap[index]
                self.heap[index] = temp
                
                self.trickle_down(large_index)
     
    def get_count(self):
        return self.count
    
    def _get_parent_idx(self, index):
        return int((index - 1) / 2)
    
    def _get_right_child_idx(self, index):
        return int((index * 2) + 2)
    
    def _get_left_child_idx(self, index):
        return int((index * 2) + 1)
        