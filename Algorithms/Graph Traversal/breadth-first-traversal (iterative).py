GRAPH = {
    "A": ["B","D","E"],
    "B": ["A","C","D"],
    "C": ["B","G"],
    "D": ["A","B","E","F"],
    "E": ["A","D"],
    "F": ["D"],
    "G": ["C"]
}

def bfs(graph, current_vertex):

    queue = []      # an empty queue
    visited = []    # an empty list of visited nodes

    queue.append(current_vertex)        # enqueue

    while len(queue) > 0:               # while queue not empty
        current_vertex = queue.pop(0)   # dequeue
        visited.append(current_vertex)
        for neighbour in graph[current_vertex]:
            if neighbour not in visited and \
               neighbour not in queue:
                queue.append(neighbour)

    return visited

# main program
traversal = bfs(GRAPH, 'A')
print('Nodes visited in this order:', traversal)

