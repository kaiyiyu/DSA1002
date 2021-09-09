'''
    Author: Kai-Yu L. Yu
    Purpose: Implementation of Doubly Linked List ADT
    (An older version of this program was submitted for a previous DSA1002 Practical)
    Date: August 31, 2021
'''

class _DSAListNode:
    def __init__(self, in_value):
        self._value = in_value
        self._next = None
        self._prev = None

    def get_value(self):
        return self._value

    def set_value(self, in_value):
        self._value = in_value

    def get_next(self):
        return self._next

    def set_next(self, next_value):
        self._next = next_value

    def get_prev(self):
        return self._prev

    def set_prev(self, prev_value):
        self._prev = prev_value
        
class DSALinkedList:
    def __init__(self):
        self._head = None
        self._tail = None
    
    def __iter__(self):
        curr_nd = self._head
        while curr_nd is not None:
            yield curr_nd._value
            curr_nd = curr_nd._next
        
    def is_empty(self):
        empty = False
        empty = self._head == None
        return empty
    
    def insert_first(self, in_value):
        new_nd = _DSAListNode(in_value)
        
        if self.is_empty():
            self._head = new_nd
            self._tail = new_nd
        else:
            new_nd.set_next(self._head)
            self._head.set_prev(new_nd)
            self._head = new_nd
            
    def insert_last(self, next_value):
        new_nd = _DSAListNode(next_value)
        
        if self.is_empty():
            self._head = new_nd
            self._tail = new_nd
            
        else:
            self._tail.set_next(new_nd)
            new_nd.set_prev(self._tail)
            self._tail = new_nd
    
    def peek_first(self):
        if self.is_empty():
            raise Exception("List is empty")
        else:
            node_value = self._head.get_value()
        return node_value
    
    def peek_last(self):
        if self.is_empty():
            raise Exception("List is empty")
        else:
            node_value = self._tail.get_value()
        return node_value
        
    def remove_first(self):
        if self.is_empty():
            raise Exception("List is empty")
        else:
            node_value = self._head.get_value()
            self._head = self._head.get_next()
        return node_value
    
    def remove_last(self):
        if self.is_empty():
            raise Exception("List is empty")
        elif self._tail.get_prev() == None:
            node_value = self._tail.get_value()
            self._head = None
            self._tail = None
        else:
            node_value = self._tail.get_value()
            self._tail.get_prev().set_next(None)
            self._tail = self._tail.get_prev()
        return node_value 
    
# Test Harness for Linked List ADT
if __name__ == '__main__':
    new_list = DSALinkedList()
    
    # Print for better sectioned terminal output
    def printDivider():
        print("----------------------------------------------------")  

    # Test insert_first method
    print("Inserting items to front...")
    new_list.insert_first("UCP")
    new_list.insert_first("DSA")
    for item in new_list:
        print(item)
    printDivider()

    # Test insert_last method
    print("Inserting items to last...")
    new_list.insert_last(1000)
    new_list.insert_last(1002)
    for item in new_list:
        print(item)
    printDivider()

    # Test remove_first method
    print("Removing first item...")
    new_list.remove_first()
    for item in new_list:
        print(item)
    printDivider()

    # Test remove_last method
    print("Removing last item...")
    new_list.remove_last()
    for item in new_list:
        print(item)
    printDivider()

    # Test peek_first method
    print("Expected first item: UCP\nProgram Output:", new_list.peek_first())
    printDivider()

    # Test peek_last method
    print("Expected last item: 1000\nProgram Output:", new_list.peek_last())
    printDivider()