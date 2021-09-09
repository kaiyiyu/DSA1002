'''
    Author: Kai-Yu L. Yu
    Purpose: Program to handle file input and output of all data files
    (Older versions of this program were submitted for previous DSA1002 Practicals)
    Date: August 31, 2021
'''
import DSAHashTable
import DSAGraph
import pickle
import os.path

class FileIO:
    def __init__(self):
        self.student_hash = DSAHashTable.DSAHashTable(3500)
        self.unit_hash = DSAHashTable.DSAHashTable(139)
        self.network_graph = DSAGraph.DSAGraph()
        self._unit_count = 1
        
    # Read data from file then load to assigned ADT    
    def read_file(self, filename, load_option):
        try:
            fileObj = open(filename) 
            lineNum = 0
            line = fileObj.readline() 
            
            while line:
                lineNum += lineNum
                if load_option == "A":
                    self.process_student(line.rstrip('\n'))
                elif load_option == "B":
                    self.process_unit(line.rstrip('\n'))
                elif load_option == "C":
                    self.process_network(line.rstrip('\n'))
                line = fileObj.readline()
            fileObj.close() 
        except IOError: 
            raise IOError("\033[91mError in file processing\033[0m")
    
    # Load student data to hash table
    def process_student(self, line):
        try:
            token = line.split(",")
            self.student_hash.put(token[0], token[1])      
        except TypeError:
            raise TypeError("Line row had invalid format.")
        
    # Load unit data to hash table
    def process_unit(self, line):
        try:
            token = line.split(",")
            self.unit_hash.put(token[0], token[1], token[2], token[3])
        except TypeError:
            raise TypeError("Line row had invalid format.")
        
    # Load network data to graph     
    def process_network(self, line):
        try:
            token = line.split(",")    
            tutor_name = self.student_hash.get_key(token[0], False)
            student_name = self.student_hash.get_key(token[2], False)
            unit_name = self.unit_hash.get_key(token[1], False)

            if not self.network_graph.has_vertex(tutor_name):
                self.network_graph.add_vertex(tutor_name, token[0])
            
            if not self.network_graph.has_vertex(student_name):
                self.network_graph.add_vertex(student_name, token[2])
            
            # All edges will be inserted since the uniqueness is not important other than counting the number of
            # units which is done here directly.
            if not self.network_graph.has_edge(unit_name):
                self._unit_count += 1
            self.network_graph.add_edge(tutor_name, student_name, unit_name, token[1])
    
        except TypeError:
            raise TypeError("Line row had invalid format.")
                      
    # Load .dat files 
    def load_serialized(self):
        try:
            # Check if serialized student data exists or is loaded
            if os.path.isfile("student.dat") and self.student_hash.count == 0:
                with open("student.dat", "rb") as dataFile:
                    self.student_hash = pickle.load(dataFile)
                    print("\033[92mSuccessfully deserialized student data.\033[0m")
            else:
                print("\033[93mStudent file already loaded!\033[0m")

            # Check if serialized unit data exists or is loaded
            if os.path.isfile("unit.dat") and self.unit_hash.count == 0:
                with open("unit.dat", "rb") as dataFile:
                    self.unit_hash = pickle.load(dataFile)
                    print("\033[92mSuccessfully deserialized unit data.\033[0m")
            else:
                print("\033[93mUnit file already loaded!\033[0m")

            # Check if serialized network data exists or is loaded
            if os.path.isfile("network.dat") and self.network_graph._vertices.is_empty():
                with open("network.dat", "rb") as dataFile:
                    self.network_graph = pickle.load(dataFile)
                    print("\033[92mSuccessfully deserialized network data.\033[0m")
            else:
                print("\033[93mNetwork file already loaded!\033[0m")
                    
        except FileNotFoundError:
            raise FileNotFoundError("\033[91mFile does not exist in current directory.\033[0m")

    def serialize_data(self):
        try:
            # Check if student data is already serialized
            if os.path.isfile("student.dat"):
                print("\033[93mStudent serialized file already exists!\033[0m")
            else:
                with open("student.dat", "wb") as dataFile:
                    pickle.dump(self.student_hash, dataFile)
                    print( "\033[92mSuccessfully serialized student data.\033[0m")
                    
            # Check if unit data is already serialized
            if os.path.isfile("unit.dat"):
                print("\033[93mUnit serialized file already exists!\033[0m")
            else:
                with open("unit.dat", "wb") as dataFile:
                    pickle.dump(self.unit_hash, dataFile)
                    print( "\033[92mSuccessfully serialized unit data.\033[0m")
            
            # Check if network data is already serialized 
            if os.path.isfile("network.dat"):
                print("\033[93mNetwork serialized file already exists!\033[0m")
            else:
                with open("network.dat", "wb") as dataFile:
                    pickle.dump(self.network_graph, dataFile)
                    print("\033[92mSuccessfully serialized network data.\033[0m")      
        
        except IOError: 
            raise IOError("\033[91mError in file processing\033[0m")          

# Test Harness for FileIO class       
if __name__ == '__main__':
    new_file = FileIO()
    
    # Print for better sectioned terminal output
    def printDivider():
        print("----------------------------------------------------")
    
    # Load given CSV files  
    print("Loading student, unit, and network CSV files.")    
    new_file.read_file("students.csv", "A")
    new_file.read_file("units.csv", "B")
    new_file.read_file("network.csv", "C")
    printDivider()
    
    # Test ADT class method for initialized object (called method should work if data are successfully loaded)
    print("Calling get_key method for student hash table...\nExpected output: 14341618, Robby Hasko\n" +
          "Formatted Program Output:", new_file.student_hash.get_key("14341618"))
    printDivider()
    
    print("Calling get_key method for unit hash table...\nExpected output: ISEC6001, Intrusion Detection, Postgraduate Unit" +
          ", https://handbook.curtin.edu.au/units/unit-pg-secure-devops--isec6000v1\nFormatted Program Output:", new_file.unit_hash.get_key("ISEC6001"))
    printDivider()
    
    print("Calling is_adjacent method for network graph...\nExpected output: True\nProgram Output:", new_file.network_graph.is_adjacent("Giovanni Mcclammy", "Robbie Sherick"))
    printDivider()
    
    
    ##### The rest of the methods can be tested with the main StudyHelp program. Serializing and deserializing files
    ##### can affect some functionality of the main program since .dat files will already be created.