def dfs(v):
    if v not in visited:
        print(v, end=" ")
        visited.add(v)
        for x in graph.get(v, []):
            dfs(x)

n = int(input("Enter number of vertices: "))
graph = {}
for i in range(n):
    v = input("Enter vertex: ")
    graph[v] = input("Enter adjacent vertices: ").split()

start = input("Enter starting vertex: ")
visited = set()
print("DFS:", end=" ")
dfs(start)
print()
