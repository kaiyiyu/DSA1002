import DSALinkedList
import DSAQueue

class _DSAGraphVertex:
    def __init__(self, in_label):
        self._label = in_label
        self._links = DSALinkedList.DSALinkedList()
        self._visited = False
    
    def get_adjacent(self):
        return self._links
    
    def get_label(self):
        return self._label
    
    def get_visited(self):
        return self._visited
    
    def to_string(self):
        return self._label
    
    def add_edge(self, in_vertex):
        self._links.insert_last(in_vertex)
        
    def set_visited(self):
        self._visited = True
    
    def clear_visited(self):
        self._visited = False
        
class DSAGraph:
    def __init__(self):
        self._vertices = DSALinkedList.DSALinkedList()
        
    def get_vertex(self, in_label):
        vertex = None
        if self.has_vertex(in_label) == False:
            raise Exception("Vertex " + in_label + " not found.")
        
        for object in self._vertices:
            if object.get_label() == in_label:
                vertex = object
        return vertex
    
    def has_vertex(self, in_label):
        found = False
        for object in self._vertices:
            if object.get_label() == in_label:
                found = True
        return found
    
    def add_vertex(self, in_label):
        if self.has_vertex(in_label):
            raise Exception("Vertex", in_label, " already exists.")
        self._vertices.insert_last(_DSAGraphVertex(in_label))      
    
    def add_edge(self, label1, label2):
        _DSAGraphVertex.add_edge(self.get_vertex(label1), self.get_vertex(label2))
        _DSAGraphVertex.add_edge(self.get_vertex(label2), self.get_vertex(label1)) 
    
    def get_vertex_count(self):
        count = 0
        for object in self._vertices:
            count += 1
        return count
    
    def get_edge_count(self):
        count = 0
        for object in self._vertices:
            for object2 in object.get_adjacent():
                count += 1
        return count/2
    
    def get_adjacent(self, in_label):
        return self.get_vertex(in_label).get_adjacent()
    
    def clear_visited(self):
        for object in self._vertices:
            object.clear_visited()
    
    def is_adjacent(self, label1, label2):
        adjacent = False
        vertex1 = self.get_vertex(label1)
        vertex2 = self.get_vertex(label2)
        for object in vertex1.get_adjacent():
            if object == vertex2:
                adjacent = True
        return adjacent
    
    def display_list(self):
        for object in self._vertices:
            print(object.get_label(), "|", end=" ")
            for object2 in object.get_adjacent():
                print(object2.get_label(), end=" ")
            print("\n")
            
    ##### GRAPH TRAVERSALS #####
    def DFS(self):
        self.clear_visited()
        return self._DFS(self._vertices.peek_first())
    
    def _DFS(self, vertex):
        traversal = ""
        vertex.set_visited()
        for object in vertex.get_adjacent():
            curr_vertex = object
            if not curr_vertex.get_visited():
                traversal += ("(" + vertex.to_string() + ", " + curr_vertex.to_string() + ") " + self._DFS(curr_vertex))
        return traversal
    
    def BFS(self):
        queue = DSAQueue.DSAQueue()
        self.clear_visited()
        queue.enqueue(self._vertices.peek_first())
        self._vertices.peek_first().set_visited()
        return self._BFS(queue)
        
    def _BFS(self, queue):
        vertex = queue.dequeue()
        traversal = ""
        for object in vertex.get_adjacent():
            curr_vertex = object
            if not curr_vertex.get_visited():
                queue.enqueue(curr_vertex)
                curr_vertex.set_visited()
                traversal += ("(" + vertex.to_string() + ", " + curr_vertex.to_string() + ") ")
        if not queue.is_empty():
            traversal += self._BFS(queue)
        return traversal