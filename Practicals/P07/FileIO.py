import DSALinkedList
import DSAHashTable

class FileIO:
    def __init__(self):
        self.lines = DSALinkedList.DSALinkedList()
        self.table = DSAHashTable.DSAHashTable(7000)
        self.table2 = DSAHashTable.DSAHashTable(7000)
        self.duplicates = 0
        
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
            
            try:
                self.table.put(token[0], token[1])
            except IOError:
                self.duplicates += 1
        
        if self.duplicates != 0:
            print("Duplicate keys found in file.")
                
    def saveCSV(self, filename):
        try:
            fileObj = open(filename, 'w')
            
            for line in self.table.export():
                fileObj.write(line)
            fileObj.close()
            
        except IOError as e:
            print("Error in file processing: " + str(e))
        
if __name__ == "__main__":
    f = FileIO()
    f.loadCSV("RandomNames7000.csv")
    print(f.table.get_load_factor())
    
    f.table.put("90022616", "Kai")
    print(f.table.get_load_factor())
    
    f.table.remove("90022616")
    print(f.table.get_load_factor())
    f.saveCSV("save.csv")
    
    print(f.table.get("14495655"))
    print(f.table.get("90022616"))
    
    
    
    
    