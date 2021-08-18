import DSAGraph

graph = DSAGraph.DSAGraph()

graph.add_vertex("A")
graph.add_vertex("B")
graph.add_vertex("C")
graph.add_vertex("D")
graph.add_vertex("E")
graph.add_vertex("F")
graph.add_vertex("G")

graph.add_edge("A", "B" )
graph.add_edge("A", "E" )
graph.add_edge("A", "D" )
graph.add_edge("A", "C" )
graph.add_edge("B", "E" )
graph.add_edge("C", "D" )
graph.add_edge("D", "F" )
graph.add_edge("E", "F" )
graph.add_edge("E", "G" )
graph.add_edge("F", "G" )

graph.display_list()

print("Depth First Search")
print(graph.DFS() + "\n")

print("Breadth First Search")
print(graph.BFS())