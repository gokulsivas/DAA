MAX = 20
COLORS = 4
color_names = ["Red", "Green", "Violet", "Blue"]

graph = [[0]* MAX for _ in range(MAX)]
colors = [-1]* MAX

V = int(input("Enter the number of vertices: "))

print("Enter the adjacency matrix: ")
graph = [list(map(int, input().split())) for _ in range(V)]

def is_safe(v, c, V):
    for i in range(V):
        if graph[v][i] == 1 and colors[i] == c:
            return False
    return True

def graph_coloring(v, V):
    if (v == V):
        return True
    
    for c in range(COLORS):
        if is_safe(v, c, V):
            colors[v] = c
            if graph_coloring(v+1, V):
                return True
            colors[v] = -1
    return False

def print_solution(V):
    print("Solution using minimum colours: ")
    for i in range(V):
        print(f"Vertex {i} -> {color_names[colors[i]]}")

if graph_coloring(0, V):
    print_solution(V)
else:
    print("Solution cannot be obtained using the 4 given colours")
    

              