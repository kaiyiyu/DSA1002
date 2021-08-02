import DSALinkedList
import pickle

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

# Driver code
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
    
    # Serialization
    print("\nSaving object to file...")
    try:
        with open("queue.dat", "wb") as dataFile:
            pickle.dump(l_queue, dataFile)
    except:
        print("\nError: Problem pickling object!")

    #Deserialization
    with open("queue.dat", "rb") as dataFile:
        elements = pickle.load(dataFile)

        print("\nLoading list in file...")
        for element in elements:
            print(f"An element is: {element}")