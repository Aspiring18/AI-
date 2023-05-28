class GraphColoring:
    def __init__(self, graph, colors):
        self.graph = graph
        self.colors = colors
        self.num_vertices = len(graph)
        self.solution = [-1] * self.num_vertices

    def solve(self):
        if self.solve_backtracking(0):
            self.print_solution()
        else:
            print("No solution found!")

    def solve_backtracking(self, vertex):
        if vertex == self.num_vertices:
            return True

        for color in self.colors:
            if self.is_safe(vertex, color):
                self.solution[vertex] = color
                if self.solve_backtracking(vertex + 1):
                    return True
                self.solution[vertex] = -1

        return False

    def is_safe(self, vertex, color):
        for i in range(self.num_vertices):
            if self.graph[vertex][i] == 1 and self.solution[i] == color:
                return False
        return True

    def print_solution(self):
        print("Solution:")
        for i in range(self.num_vertices):
            print(f"Vertex {i}: Color {self.solution[i]}")

# User input
num_vertices = int(input("Enter the number of vertices: "))
graph = []
for i in range(num_vertices):
    row = list(map(int, input(f"Enter the adjacency matrix row for vertex {i}: ").split()))
    graph.append(row)

num_colors = int(input("Enter the number of colors: "))
colors = []
for i in range(num_colors):
    color = input(f"Enter color {i}: ")
    colors.append(color)

coloring = GraphColoring(graph, colors)
coloring.solve()
