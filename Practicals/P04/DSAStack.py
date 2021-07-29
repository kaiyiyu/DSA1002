import DSALinkedList
import pickle

# Implementation of DSALinkedList in DSAStack
class DSAStack:
    
    def __init__(self):
        self._stack = DSALinkedList.DSALinkedList()    

    def __iter__(self):
        return self._stack.__iter__()

    def is_empty(self):
        return self._stack.is_empty()
    
    def push(self, item):  
        self._stack.insert_first(item)        
    
    def pop(self):
        return self._stack.remove_first()

    def top(self):  
        if self.is_empty():
            raise Exception('Stack is empty.')
        return self._stack.peek_first()

# Driver code
if __name__ == '__main__':
    l_stack = DSAStack()
    
    # Test push method
    print("After push()...")
    l_stack.push('First')
    l_stack.push(2)
    l_stack.push(3.0)
    l_stack.push("Fourth")
    for element in l_stack:
        print(element)
    
    # Test pop method
    print("\nAfter pop()...")
    l_stack.pop()
    l_stack.pop()
    for element in l_stack:
        print(element)
        
    # Test top method
    print("\nThe top element is:", l_stack.top())
    
    # Serialization
    print("\nSaving object to file...")
    try:
        with open("stack.dat", "wb") as dataFile:
            pickle.dump(l_stack, dataFile)
    except:
        print("\nError: Problem pickling object!")

    #Deserialization
    with open("stack.dat", "rb") as dataFile:
        elements = pickle.load(dataFile)

        print("\nLoading list in file...")
        for element in elements:
            print(f"An element is: {element}")
    
    
    