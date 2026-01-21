#MPR - May 2024

#This is a conversion of the algorithm shown on page 354 of the OCR course textbook.
#The textbook is pseudo code, so you need to think carefully how to write this in python.

#The dictionary inside a dictonary can be a bit tricky to access when you have variables involved.
#Check out lines 34 or 36 for examples of how you can access/change the individual colours or neighbours of particular nodes.

#TO DO
#1) Make a verbose version of this that prints the state of the queue and visited after each stage with input() to allow "tracing",etc.

GRAPH = {
"A": {"colour": "White", "neighbours": ["B", "D", "E"]},
"B": {"colour": "White", "neighbours": ["A", "D", "C"]},
"C": {"colour": "White", "neighbours": ["B", "G"]},
"D": {"colour": "White", "neighbours": ["A", "B", "E", "F"]},
"E": {"colour": "White", "neighbours": ["A", "D"]},
"F": {"colour": "White", "neighbours": ["D"]},
"G": {"colour": "White", "neighbours": ["C"]}
}

#white means not visited and black means visited during the graph traversal
#grey means queued, but not yet visted.

def bfs(graph, vertex):
  queue = [] # an empty queue
  visited = [] ## an empty list of visited nodes
  queue.append(vertex)
  
  while len(queue) != 0:
    currentNode = queue.pop()
    #colour it black
    graph[currentNode]["colour"] = "Black"
    visited.append(currentNode)
  
    for neighbour in graph[currentNode]["neighbours"]:
  
      if graph[neighbour]["colour"] == "White":
        queue.append(neighbour)
        graph[neighbour]["colour"] = "Grey"
  
  return visited

## main
visited = bfs(GRAPH, "A")
print ("List of nodes visited: ", visited)
