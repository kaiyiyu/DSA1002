import DSALinkedList
import DSAHashTable

class FileIO:
    def __init__(self):
        self.lines = DSALinkedList.DSALinkedList()
        self.table = DSAHashTable.DSAHashTable(7000)
        
    def loadCSV(self, filename):
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
            self.table.put(token[0], token[1])
                
    def saveCSV(self, filename):
        try:
            fileObj = open(filename, 'w')
            
            for line in self.table.export():
                fileObj.write(line)
            fileObj.close()
            
        except IOError as e:
            print("Error in file processing: " + str(e))
    
    def printDivider(self):
        print("----------------------------------------------------")  

# Driver code
if __name__ == "__main__":
    f = FileIO()
    
    # Read data from CSV
    print("Loading data from CSV file and calculating initial load factor...")
    f.loadCSV("RandomNames7000.csv")
    print("Program output:", f.table.get_load_factor())
    f.printDivider()
    
    # Add element and check new LF
    f.table.put("90022616", "Kai")
    print("Program output:", f.table.get_load_factor())
    f.printDivider()
    
    # Remove an element and check LF > should go back to initial LF
    f.table.remove("90022616")
    print("Program output:", f.table.get_load_factor())
    f.printDivider()
    
    # Save to CSV
    f.saveCSV("hash.csv")
    
    # Look up existing and unexisting elements
    print("Expected value for 14495655: Sofia Bonfiglio\nProgram output:", f.table.get("14495655"))
    print("Expected an error for previously removed key 90022616.")
    f.table.get("90022616")