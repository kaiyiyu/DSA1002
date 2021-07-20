import numpy

class DSAStack:
    def __init__(self):
        self._data = numpy.zeros(100, dtype=object)
        self.count = 0
        self._default_capacity = 100
    
    # gets the values/items in the array
    def get_count(self, i):
	    return self._data[i]

    # checks if the array is empty
    def is_empty(self):
        if self.count == 0:
            return True

    # checks if the array is full
    def is_full(self):
        if self.count == self._default_capacity:
            return True
    
    def push(self, value):  
        if self.is_full():
            raise Exception('Stack is full.')   
        elif self.count == self._default_capacity:
            self._default_capacity *= 2
            new_data = numpy.zeros(self._default_capacity, dtype=object)
            for i in range(self.count):
                new_data[i] = self._data[i]
            self._data = new_data
        
        self._data[self.count] = value
        self.count += 1        
    
    def pop(self):
        top_value = self.top()
        self.count = self.count - 1
        return top_value

    def top(self):  
        if self.is_empty():
            raise Exception('Stack is empty.')
        else:
            return self._data[self.count - 1]

