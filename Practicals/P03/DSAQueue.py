import numpy

# Implementation of parent class queue (change index)
class DSAQueue:
    
    DEFAULT_CAPACITY = 100
    
    def __init__(self):
        self._queue = numpy.zeros(self.DEFAULT_CAPACITY, dtype=object)
        self.size = 0
        self.front = 0
    
    def __len__(self):
	    return self.size

    def is_empty(self):
        return self.size == 0

    # Not really needed, but in included in pseudocode
    def is_full(self):
        return self.size == self.DEFAULT_CAPACITY

    def peek(self):  
        if self.is_empty():
            raise Exception('Queue is empty.')
        return self._queue[self.front]
    
    def enqueue(self, item):
        if self.is_full():
            raise Exception('Queue is full.')   
        elif self.size == self.DEFAULT_CAPACITY:
            self._shift(2 * self.DEFAULT_CAPACITY)
        empty = (self.front + self.size) % self.DEFAULT_CAPACITY
        self._queue[empty] = item
        self.size += 1
              
    def _shift(self, capacity):
        old_array = self._queue
        self._queue = numpy.zeros(capacity, dtype=object)
        move_index = self.front
        
        for i in range(self.size):
            self._queue[i] = old_array[move_index]
            move_index = (1 + move_index) % len(old_array)
        self.front = 0
    
    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty.')
        data = self._queue[self.front]
        self._queue[self.front] = '-'
        self.front = (self.front + 1) % self.DEFAULT_CAPACITY
        self.size -= 1
        return data
        
    def display(self):
        print('\nThe current state of the queue is:')
        for i in self._queue:
            print('[', i, ']', end = ' ')
        print('\nThe current top value is: ', self.peek())
        
# Implementation of shuffling queue
class ShufflingQueue(DSAQueue):
    
    DEFAULT_CAPACITY = 5
    
    def __init__(self):
        self._queue = numpy.zeros(self.DEFAULT_CAPACITY, dtype=object)
        self.front = 0
        self.rear = -1

    def is_empty(self):
        return self.rear == -1

    def is_full(self):
        return self.rear == self.DEFAULT_CAPACITY - 1

    def enqueue(self, item):
        if self.is_full():
            raise Exception('Queue is full.') 
        self.rear += 1
        self._queue[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue is empty.')
        data = self._queue[0]
        self._shuffle()
        return data
    
    def _shuffle(self):
        for i in range(1,self.DEFAULT_CAPACITY):
            self._queue[i - 1] = self._queue[i]
        self._queue[self.rear] = '-' 
        self.rear -= 1
        
# Implementation of circular queue
class CircularQueue(DSAQueue):
    
    DEFAULT_CAPACITY = 5

    def __init__(self):
        self._queue = numpy.zeros(self.DEFAULT_CAPACITY, dtype=object)
        self.front = 0 
        self.rear = 0
        self.size = 0

    def enqueue(self, item):
        if self.is_full():
            raise Exception("Queue is full.")

        self._queue[self.rear] = item
        self.rear = (self.rear + 1) % self.DEFAULT_CAPACITY
        self.size += 1
        return self

    def dequeue(self):
        if self.is_empty():
            raise Exception("Queue is empty.")

        temp = self._queue[self.front]
        self._queue[self.front] = '-'
        self.front = (self.front + 1) % self.DEFAULT_CAPACITY
        self.size -= 1
        return temp

    