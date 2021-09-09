'''
    Author: Kai-Yu L. Yu
    Purpose: Implementation of Queue ADT
    (An older version of this program was submitted for a previous DSA1002 Practical)
    Date: August 31, 2021
'''
import DSALinkedList

# Implementation of DSALinkedList in DSAQueue
class DSAQueue:
    
    def __init__(self):
        self._queue = DSALinkedList.DSALinkedList()
    
    def __iter__(self):
        return self._queue.__iter__()

    def is_empty(self):
        return self._queue.is_empty()

    def peek(self):  
        return self._queue.peek_first()
    
    def enqueue(self, item):
        self._queue.insert_last(item)
    
    def dequeue(self):
        return self._queue.remove_first()

# Test Harness for Queue ADT
if __name__ == "__main__":
    l_queue = DSAQueue()

    # Test enqueue method
    print("After enqueue()...")
    l_queue.enqueue("First")
    l_queue.enqueue(2)
    l_queue.enqueue(3.0)
    l_queue.enqueue("Fourth")
    for element in l_queue:
        print(element)
        
    # Test dequeue method
    print("\nAfter dequeue()...")
    l_queue.dequeue()
    l_queue.dequeue()
    for element in l_queue:
        print(element)
    
    # Test peek method
    print("\nThe top element is:", l_queue.peek())