import numpy
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