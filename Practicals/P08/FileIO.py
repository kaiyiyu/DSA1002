import DSALinkedList
import DSAHeap
import numpy as np

class HeapFileIO:
    def __init__(self):
        self.lines = DSALinkedList.DSALinkedList()
        
    def loadCSV(self, heap, filename):
        try:
            fileObj = open(filename) 
            lineNum = 0
            line = fileObj.readline() 
            
            while line:
                lineNum += lineNum
                self.lines.insert_last(line)
                line = fileObj.readline()
            fileObj.close() 
            
        except IOError as e: 
            print("Error in file processing: " + str(e))
            
        for object in self.lines:
            token = object.split(",")
            heap.add(int(token[0]), token[1])
            
    def testHeapSort(self, heap, filename):
        arr = np.zeros((7000, 2), dtype=object)
        index = 0
        try:
            fileObj = open(filename) 
            lineNum = 0
            line = fileObj.readline() 
            
            while line:
                lineNum += lineNum
                arr[index][0] = int(line.split(",")[0])
                arr[index][1] = line.split(",")[1]
                index += 1
                line = fileObj.readline()
            fileObj.close() 
            
        except IOError as e: 
            print("Error in file processing: " + str(e))
            
        sorted_arr = heap.heap_sort(arr)
        return sorted_arr
    
    def saveCSV(self, array, filename):
        try:
            fileObj = open(filename, 'w')
            
            for line in array:
                fileObj.write(str(line))
            fileObj.close()
            
        except IOError as e:
            print("Error in file processing: " + str(e))
            
    def printDivider(self):
        print("----------------------------------------------------")  

# Driver code          
if __name__ == "__main__":
    heap = DSAHeap.DSAHeap(7005)
    
    # Read data from CSV
    print("Loading data from CSV file...")
    f = HeapFileIO()
    f.loadCSV(heap, "RandomNames7000.csv")
    
    # Check count of heap entries
    print("Expected initial count of heap entries: 7000\nProgram output:", heap.get_count())
    f.printDivider()
    
    # Add new highest priority entry
    print("Adding new priority entry (90022616, \"Kai-Yu\") ...")
    heap.add(90022616, "Kai-Yu")
    print("Expected count: 7001\nProgram output:", heap.get_count())
    f.printDivider()
    
    # Remove an entry -> should remove the recently added entry
    print("Removing highest priority in heap...")
    print("Expected priority entry: Kai-Yu\nProgram output:", heap.remove())
    print("Expected count: 7000\nProgram output:", heap.get_count())
    f.printDivider()
    
    # Max heap sort implemented in reverse order
    print("Sorting heap array...\n")
    array = f.testHeapSort(heap, "RandomNames7000.csv")
    print("First five elements(max heap reverse order):")
    for i in range(5):
        print(array[i], end="")
    print("\nLast five elements(max heap reverse order):")
    for i in range(6995, 7000):
        print(array[i], end="")
   
    # Save to CSV file
    f.saveCSV(array, "SortedHeap.csv")