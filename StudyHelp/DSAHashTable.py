'''
    Author: Kai-Yu L. Yu
    Purpose: Implementation of Hash Table ADT 
    (An older version of this program was submitted for a previous DSA1002 Practical)
    Date: August 31, 2021
'''
import numpy as np
import math

class _DSAHashEntry:
    
    def __init__(self, in_key="", value=None, value_two=None, value_three=None):   
        self._key = in_key
        self._value = value    
        self._value_two = value_two
        self._value_three = value_three
        if self._key != "" and self._value is not None or self._value_two is not None or self._value_three is not None:
            self._state = 1
        else:
            self._state = 0
            
    def get_value(self):
        return str(self._value)

    def _str__(self):
        return ("Key: " + self._key + 
                ", First Value: " + self._value + 
                ", Second Value: " + self._value_two + 
                ", Third Value: " + self._value_three + 
                ", State: " + self._state)
     
class DSAHashTable:
    
    LOWER_THRESHOLD = 0.40
    UPPER_THRESHOLD = 0.70
    MAX_STEP = 5
    
    def __init__(self, tableSize):
        tableSize = self._next_prime(tableSize)
        self.hashArray = np.zeros(tableSize, dtype=object)
        self.count = 0
        
        for i in range(tableSize):        
            self.hashArray[i] = _DSAHashEntry()
    
    def put(self, in_key, value, value_two=None, value_three=None):
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
    
        self.hashArray[hashIdx] = _DSAHashEntry(in_key, value, value_two, value_three)
        self.count += 1
        
        if self.get_load_factor() > self.UPPER_THRESHOLD:
            self._resize(len(self.hashArray) * 2)
    
    def get_key(self, in_key, formatted=True):
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
            raise Exception(in_key + " entry not found.")
        
        if self.hashArray[hashIdx]._value_two is not None: # Unit Details with four tokens
            if formatted: # If printed directly to terminal
                details = ("\n\tUnit Code: " + self.hashArray[hashIdx]._key + "\n" 
                            "\tUnit Name: " + self.hashArray[hashIdx]._value + "\n"
                            "\tUnit Level: " + self.hashArray[hashIdx]._value_two + "\n"
                            "\tCurtin Handbook Link: " + self.hashArray[hashIdx]._value_three + "\n")
            else:   # If called in another method
                details = self.hashArray[hashIdx]._value
        elif self.hashArray[hashIdx]._value_two is None:   # Student Details with two tokens
            if formatted: 
                details = ("\n\tStudent ID: " + self.hashArray[hashIdx]._key + "\n"
                           "\tStudent Name: " + self.hashArray[hashIdx]._value + "\n")
            else:   
                details = self.hashArray[hashIdx]._value
        return details
    
    def get_value(self, in_value):  # Return student details when searched by student name
        for i in range(len(self.hashArray)):
            if self.hashArray[i]._value == in_value:
                details = ("\n\tStudent ID: " + self.hashArray[i]._key + "\n"
                           "\tStudent Name: " + self.hashArray[i]._value + "\n")
        return details
            
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
        self.hashArray[hashIdx]._value_two = None
        self.hashArray[hashIdx]._value_three = None
        self.hashArray[hashIdx]._state = -1
        
        if self.get_load_factor() < self.LOWER_THRESHOLD:
            self._resize(len(self.hashArray) / 2)
     
    def get_load_factor(self):
        return self.count / len(self.hashArray)   
    
    def export(self):
        lines = np.zeros(self.count, dtype=object)
        index = 0 
        
        for i in range(len(self.hashArray)):
            if self.hashArray[i]._state == 1:
                if self.hashArray[i]._value_two is not None:                   # Unit Details with four tokens
                    lines[index] = ("Unit Code: " + self.hashArray[i]._key + 
                                    ", Name: " + self.hashArray[i]._value + 
                                    ", Level: " + self.hashArray[i]._value_two + 
                                    ", Handbook Link: " + self.hashArray[i]._value_three)
                elif self.hashArray[i]._value_two is None:                     # Student Details with two tokens
                    lines[index] = ("Student ID: " + self.hashArray[i]._key + ", Name: " + self.hashArray[i]._value)
                index += 1
        return lines    
    
    def has_key(self, in_key):
        exists = False
        if self.hashArray[self._hash(in_key)]._state == 1:
            exists = True
        return exists
    
    ##### PRIVATE HELPER METHODS #####
                
    def _hash(self, in_key):
        hashIdx = 0
        for i in range(len(in_key)):
            hashIdx = (hashIdx * 33) + ord(in_key[i])
        return abs(hashIdx % len(self.hashArray))
    
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
                self.put(old_array[index]._key, old_array[index]._value, old_array[index]._value_two, old_array[index]._value_three)
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
        return round(int(prime))
    
# Test Harness for Hash Table ADT
if __name__ == '__main__':
    new_table = DSAHashTable(1)
    
    # Print for better sectioned terminal output
    def printDivider():
        print("----------------------------------------------------")  

    # Test load factor, put and resize methods
    print("Created DSAHashTable object with size 1")
    new_table.put("90022619", "GlitteringApricot")
    new_table.put("90022616", "MajesticSeaLion")
    print("Added two items to hash table...\nNo error expected and LF should be less than 0.7\nLF:", new_table.get_load_factor())
    printDivider()

    # Test remove method
    print("Expected error for non-existent key 90022618.")
    new_table.remove("90022618")