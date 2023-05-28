from collections import defaultdict, deque

class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs_recursive(self, vertex, visited):
        visited.add(vertex)
        print(vertex, end=" ")

        for neighbor in self.graph[vertex]:
            if neighbor not in visited:
                self.dfs_recursive(neighbor, visited)

    def dfs(self, start):
        visited = set()
        self.dfs_recursive(start, visited)
        print()

    def bfs(self, start):
        visited = set()
        queue = deque([start])
        visited.add(start)

        while queue:
            vertex = queue.popleft()
            print(vertex, end=" ")

            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)
        print()

# Example usage
if __name__ == "__main__":
    graph = Graph()
    num_edges = int(input("Enter the number of edges: "))

    for _ in range(num_edges):
        u, v = map(int, input("Enter edge (u v): ").split())
        graph.add_edge(u, v)

    start_vertex = int(input("Enter the starting vertex: "))

    print("DFS Traversal:")
    graph.dfs(start_vertex)

    print("BFS Traversal:")
    graph.bfs(start_vertex)
