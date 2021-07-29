import numpy

class DSAStack:
    
    DEFAULT_CAPACITY = 5
    
    def __init__(self):
        self._stack = numpy.empty(self.DEFAULT_CAPACITY, dtype=object)
        self.count = 0
    
    # gets the values/items in the array
    def get_count(self, i):
	    return self._stack[i]

    # checks if the array is empty
    def is_empty(self):
        return self.count == 0

    # checks if the array is full
    def is_full(self):
        return self.count == self.DEFAULT_CAPACITY
    
    def push(self, value):  
        if self.is_full():
            raise Exception('Stack is full.')   
        elif self.count == self.DEFAULT_CAPACITY:
            self.DEFAULT_CAPACITY *= 2
            new_data = numpy.empty(self.DEFAULT_CAPACITY, dtype=object)
            for i in range(self.count):
                new_data[i] = self._stack[i]
            self._stack = new_data
        
        self._stack[self.count] = value
        self.count += 1        
    
    def pop(self):
        top_value = self.top()
        self.count = self.count - 1
        return top_value

    def top(self):  
        if self.is_empty():
            raise Exception('Stack is empty.')
        return self._stack[self.count - 1]
    
    def display(self):
        print('\nThe current state of the queue is:')
        for i in self._stack:
            print(i, end = ' ')
        #  print( i, end = ' ')
        #print('\nThe current top value is: ', self.top())