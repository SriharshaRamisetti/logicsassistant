from collections import defaultdict
 
# Function to DFS Traversal of graph with given vertex and color
def DFS(graph, visited, vertex, color):
    visited[vertex] = True
    for neighbor in graph[vertex]:
        if not visited[neighbor] and colors[neighbor] == color:
            DFS(graph, visited, neighbor, color)
 
 
# Function to check if the given graph is connected with the given color
def isColorConnected(graph, colors, color):
    visited = [False] * len(graph)
    for vertex in range(len(graph)):
        if colors[vertex] == color:
            DFS(graph, visited, vertex, color)
            break
 
    # Check if all vertices with the given color are visited
    for vertex in range(len(graph)):
        if colors[vertex] == color and not visited[vertex]:
            return False
    return True
 
 
# Main function to find the minimum number of operations required to color the required graph
if __name__ == '__main__':
    N, M, K = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(M)]
    colors = list(map(int, input().split()))
    
    # Creating a dictionary to denote graph
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
 
    count = 0
    for color in range(K):
        # Check if vertices with same color are not connected
        if not isColorConnected(graph, colors, color):
            # We need to connect all vertices of same color
            # Find a unvisited vertex with the given color
            for vertex in range(N):
                if colors[vertex] == color:
                    visited = [False] * len(graph)
                    DFS(graph, visited, vertex, color)
                    # Connect all unvisited vertices with the given color
                    for v in range(N):
                        if colors[v] == color and not visited[v]:
                            count += 1
                            graph[vertex].append(v)
                            graph[v].append(vertex)
 
    print(count)
