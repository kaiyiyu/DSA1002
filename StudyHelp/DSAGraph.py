'''
    Author: Kai-Yu L. Yu
    Purpose: Implementation of Graph ADT
    (An older version of this program was submitted for a previous DSA1002 Practical)
    Date: September 2, 2021
'''
import DSALinkedList
import DSAQueue

class _DSAGraphVertex:
    def __init__(self, in_label, in_value):
        self._label = in_label
        self._value = in_value
        self._links = DSALinkedList.DSALinkedList()
        self._visited = False
    
    def get_label(self):
        return self._label
    
    def get_value(self):
        return self._value
    
    def get_adjacent(self):
        return self._links
    
    def add_edge(self, in_vertex):
        self._links.insert_last(in_vertex)
    
    def set_visited(self):
        self._visited = True
    
    def clear_visited(self):
        self._visited = False
    
    def get_visited(self):
        return self._visited
    
    def to_string(self):
        return str(self._label) + " (" + str(self._value) + ")"

class _DSAGraphEdge:
    def __init__(self, from_vertex, to_vertex, in_label, in_value):
        self._from = from_vertex
        self._to = to_vertex
        self._label = in_label
        self._value = in_value
        
    def get_label(self):
        return self._label
    
    def get_value(self):
        return self._value
    
    def get_from(self):
        return self._from
    
    def get_to(self):
        return self._to

class DSAGraph:
    def __init__(self):
        self._vertices = DSALinkedList.DSALinkedList()
        self._edges = DSALinkedList.DSALinkedList()
        self._BFS_count = 0
        self._DFS_count = 0
        
    def add_vertex(self, in_label, in_value):
        if self.has_vertex(in_label):
            raise Exception("Vertex", in_label, " already exists.")
        self._vertices.insert_last(_DSAGraphVertex(in_label, in_value))      
    
    def add_edge(self, label_one, label_two, edge_label, edge_value):
        _DSAGraphVertex.add_edge(self.get_vertex(label_one), self.get_vertex(label_two))
        self._edges.insert_last(_DSAGraphEdge(label_one, label_two, edge_label, edge_value))
    
    def has_vertex(self, in_label):
        found = False
        for object in self._vertices:
            if object.get_label() == in_label:
                found = True
        return found
    
    def has_edge(self, in_label):
        found = False
        for object in self._edges:
            if object.get_label() == in_label:
                found = True
        return found
    
    def get_vertex(self, in_label):
        vertex = None
        if self.has_vertex(in_label) == False:
            raise Exception("Vertex " + in_label + " not found.")
        
        for object in self._vertices:
            if object.get_label() == in_label:
                vertex = object
        return vertex
    
    def get_adjacent(self, in_label):
        return self.get_vertex(in_label).get_adjacent()
    
    def is_adjacent(self, label_one, label_two):
        adjacent = False
        vertex1 = self.get_vertex(label_one)
        vertex2 = self.get_vertex(label_two)
        for object in vertex1.get_adjacent():
            if object == vertex2:
                adjacent = True
        return adjacent
    
    def clear_visited(self):
        for object in self._vertices:
            object.clear_visited()
            
    ##### STATISTICS OPTION METHODS #####
    
    # Given a unit code, display students tutored in the unit
    def students_in_unit(self, unit_code):
        tutored_students = ""
        for object in self._edges:
            if object.get_label() == unit_code:
                tutored_students += ("\t> " + object.get_to() + "\n")
        return tutored_students
    
    # Additional detail to display the tutors in a given unit code
    def tutors_in_unit(self, unit_code):
        tutors = ""
        for object in self._edges:
            if object.get_label() == unit_code:
                tutors += ("\t> " + object.get_from() + "\n")
        return tutors
    
    # Count number of tutors (can be strictly a tutor or is also tutored by another)
    def tutor_count(self):
        count = 0
        for object in self._vertices:
            if not object.get_adjacent().is_empty():
                count += 1
        return count
    
    # Count number of student with no "links" (strictly students only)
    def student_only_count(self):
        count = 0
        for object in self._vertices:
            if object.get_adjacent().is_empty():
                count += 1
        return count

    # Count number of all students in the tutoring system (duplicates already filtered in insertion)
    def network_count(self):
        count = 0
        for object in self._vertices:
            count += 1
        return count
            
    ##### GRAPH TRAVERSALS #####
    
    def network_DFS(self):
        for vertex in self._vertices:
            start_vertex = vertex
            self.clear_visited()
            self._network_DFS(start_vertex, vertex)
            
    def _network_DFS(self, start_vertex, vertex):
        vertex.set_visited()
        for object in vertex.get_adjacent():
            curr_vertex = object
            if curr_vertex.get_visited() and start_vertex.get_label() == curr_vertex.get_label(): 
                self._DFS_count += 1
            elif not curr_vertex.get_visited():
                self._network_DFS(start_vertex, curr_vertex)
    
    def network_BFS(self, student):
        for object in self._vertices:
            if object.get_value() == student:
                start_vertex = object
                
        queue = DSAQueue.DSAQueue()
        self.clear_visited()
        queue.enqueue(start_vertex)
        start_vertex.set_visited()
        return self._network_BFS(queue)
        
    def _network_BFS(self, queue):
        vertex = queue.dequeue()
        traversal = ""
        space = "\033[95m|\033[0m" * self._BFS_count
        
        for object in vertex.get_adjacent():
            curr_vertex = object
            if not curr_vertex.get_visited():
                queue.enqueue(curr_vertex)
                curr_vertex.set_visited()
                for element in self._edges:
                    if element.get_from() == vertex.get_label() and element.get_to() == curr_vertex.get_label():
                        unit = element.get_value()
                
                traversal += (space + vertex.to_string() + " tutors " + curr_vertex.to_string() + 
                              " in " + unit + "\n")
                self._BFS_count += 2        
            
        if not queue.is_empty():
            traversal += self._network_BFS(queue)
        
        return traversal
    
# Test Harness for Graph ADT
if __name__ == '__main__':
        
    new_graph = DSAGraph()
    def print_divider():
        print("------------------------------------------------------------------") 

    # Add vertices to graph
    print("Adding student IDs and names to the network...\n")
    new_graph.add_vertex("Student One", "001")
    new_graph.add_vertex("Student Two", "002")
    new_graph.add_vertex("Student Three", "003")
    new_graph.add_vertex("Student Four", "004")

    # Add tutor to student details
    print("Setting tutoring details...\n")
    new_graph.add_edge("Student One", "Student Three", "Unix and C", "UCP1000")
    new_graph.add_edge("Student Four", "Student Three", "Security Concepts", "FCDS2001")
    new_graph.add_edge("Student Three", "Student Two", "Linear Algebra", "EMTH1019")
    new_graph.add_edge("Student Four", "Student One", "Data Structures", "DSA1002")
    
    # Add this edge to create three cycles
    new_graph.add_edge("Student Two", "Student One", "Computer Systems", "CS2000")
    
    # Display Unit Details
    print_divider()
    unit = "DSA1002"
    unit_name = "Data Structures"
    print("Students tutored in " + unit_name + " (" + unit + ")\n" + 
              new_graph.students_in_unit(unit_name) + "\nTutors\n" +
              new_graph.tutors_in_unit(unit_name))
    
    # Number of cycles
    print_divider()
    print("DEPTH FIRST SEARCH CYCLE COUNT")
    new_graph.network_DFS()
    print(new_graph._DFS_count)

    # Display graph BFS Student Details
    print_divider()
    print("\nBREADTH FIRST SEARCH")
    print(new_graph.network_BFS("001"))