GRAPH = {
    "A":["B","D","E"],
    "B":["A","C","D"],
    "C":["B","G"],
    "D":["A","B","E","F"],
    "E":["A","D"],
    "F":["D"],
    "G":["C"]
}
visited_list = []  # an empty list of visited nodes

def dfs(graph, current_vertex, visited):
    visited.append(current_vertex)
    for vertex in graph[current_vertex]: # check neighbours
        if vertex not in visited:
            dfs(graph, vertex, visited)  # recursive call
            # stack will store return address, parameters
            # and local variables
    return visited

# main program
traversal = dfs(GRAPH, 'A', visited_list)
print('Nodes visited in this order:', traversal)
