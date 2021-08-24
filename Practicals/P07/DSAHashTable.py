import numpy as np
import math

class _DSAHashEntry:
    
    def __init__(self, in_key="", in_value=None):   
        self._key = in_key
        self._value = in_value    
        if in_value is not None:
            self._state = 1
        else:
            self._state = 0

    def to_str(self):
        return ("Key: " + self._key + ", Value: " + self._value + ", State: " + self._state)
     
class DSAHashTable:
    
    LOWER_THRESHOLD = 0.4
    UPPER_THRESHOLD = 0.7
    MAX_STEP = 5
    
    def __init__(self, tableSize):
        tableSize = self._next_prime(tableSize)
        self.hashArray = np.zeros(tableSize, dtype=object)
        self.count = 0
        
        for i in range(tableSize):        
            self.hashArray[i] = _DSAHashEntry()
    
    def put(self, in_key, in_value):
        hashIdx = self._hash(in_key)
        origIdx = hashIdx 
        found = False
        giveUp = False
        
        while not found and not giveUp:
            if self.hashArray[hashIdx]._state == 0 or self.hashArray[hashIdx]._state == -1:
                found = True
            elif self.hashArray[hashIdx]._state == 1:
                # Double Hashing
                hashIdx = (hashIdx + self._step_hash(origIdx)) % len(self.hashArray)
                if hashIdx == origIdx:
                    giveUp = True
                
        if not found:
            raise Exception("No space found for key.")
    
        self.hashArray[hashIdx] = _DSAHashEntry(in_key, in_value)
        self.count += 1
        
        if self.get_load_factor() > self.UPPER_THRESHOLD:
            self._resize(len(self.hashArray) * 2)
    
    def get(self, in_key):
        hashIdx = self._hash(in_key)
        origIdx = hashIdx 
        found = False
        giveUp = False
        
        while not found and not giveUp:
            if self.hashArray[hashIdx]._state == 0:
                giveUp = True
            elif self.hashArray[hashIdx]._key.__eq__(in_key):
                found = True
            else:   # Double hashing
                hashIdx = (hashIdx + self._step_hash(origIdx) % len(self.hashArray))
                if hashIdx == origIdx:
                    giveUp = True
                    
        if not found:
            raise Exception(in_key + " key entry not found.")
        return self.hashArray[hashIdx]._value
    
    def remove(self, in_key):
        hashIdx = self._hash(in_key)
        origIdx = hashIdx 
        found = False
        giveUp = False
        
        while not found and not giveUp:
            if self.hashArray[hashIdx]._state == 0:
                giveUp = True
            elif self.hashArray[hashIdx]._key == in_key:
                found = True
                self.count -= 1
            else:   # Double Hashing
                hashIdx = (hashIdx + self._step_hash(origIdx) % len(self.hashArray))
                if hashIdx == origIdx:
                    giveUp = True
                    
        if not found:
            raise Exception(in_key + " key entry not found.")
    
        self.hashArray[hashIdx]._key = ""
        self.hashArray[hashIdx]._value = None
        self.hashArray[hashIdx]._state = -1
        
        if self.get_load_factor() < self.LOWER_THRESHOLD:
            self._resize(int(round(len(self.hashArray) / 2)))
     
    def get_load_factor(self):
        return self.count / len(self.hashArray)   
    
    def export(self):
        lines = np.zeros(self.count, dtype=object)
        index = 0 
        
        for i in range(len(self.hashArray)):
            if self.hashArray[i]._state == 1:
                lines[index] = (self.hashArray[i]._key + ", " + self.hashArray[i]._value)
                index += 1
        return lines    
                
    def _hash(self, in_key):
        a = 63689
        b = 378551
        hashIdx = 0
        for i in range(len(in_key)):
            hashIdx = (hashIdx * a) + ord(in_key[i])
            a *= b
        return abs(hashIdx % len(self.hashArray))
    
    def has_key(self, in_key):
        exists = False
        if self.hashArray[self._hash(in_key)]._state == 1:
            exists = True
        return exists
    
    def _step_hash(self, index):
        return self.MAX_STEP - (index % self.MAX_STEP)
    
    def _resize(self, size):
        old_array = self.hashArray
        size = self._next_prime(size)
        new_count = 0
        
        self.hashArray = np.zeros(size, dtype=object)
        for i in range(size):
            self.hashArray[i] = _DSAHashEntry()
            
        for index in range(len(old_array)):
            if old_array[index]._state == 1:
                self.put(old_array[index]._key, old_array[index]._value)
                new_count += 1
        
        self.count = new_count
        
    def _next_prime(self, in_num):     
        if in_num % 2 == 0:
            prime = in_num - 1
        else:
            prime = in_num 

        is_prime = False

        while not is_prime:
            if in_num == 1:
                prime += 1
                is_prime = True
            else:
                prime += 2
                ii = 3
                is_prime = True
                root_val = math.sqrt(prime) 

                while ii <= root_val and is_prime:
                    if prime % ii == 0:
                        is_prime = False
                    else:
                        ii += 2          
        return prime