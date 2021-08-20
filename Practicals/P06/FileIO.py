import DSAGraph
import DSALinkedList

class FileIO:
    def __init__(self):
        self.lines = DSALinkedList.DSALinkedList()
        self.graph = DSAGraph.DSAGraph()

    def readFile(self, filename):
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
    
    def processLine(self):
        for object in self.lines:
            vertices = object.split()
            for string in vertices:
                if not self.graph.has_vertex(string):
                    self.graph.add_vertex(string)
                    
            if not self.graph.is_adjacent(vertices[0], vertices[1]):
                self.graph.add_edge(vertices[0], vertices[1])
        
if __name__ == "__main__":
    ##### FIRST FILE #####
    file = FileIO()
    print("Testing file 1...")
    file.readFile("prac6_1.al")
    file.processLine()
    file.graph.display_list()
    
    ##### TRAVERSALS #####
    print("Depth First Search")
    print(file.graph.DFS() + "\n")
    print("Breadth First Search")
    print(file.graph.BFS())
    
    print("-----------------------------------------------------------")
    
    ##### SECOND FILE #####
    file1 = FileIO()
    print("Testing file 2...")
    file1.readFile("prac6_2.al")
    file1.processLine()
    file1.graph.display_list()
    
    ##### TRAVERSALS #####
    print("Depth First Search")
    print(file1.graph.DFS() + "\n")
    print("Breadth First Search")
    print(file1.graph.BFS())