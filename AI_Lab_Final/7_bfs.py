from collections import deque

n = int(input("Enter number of vertices: "))
graph = {}
for i in range(n):
    v = input("Enter vertex: ")
    graph[v] = input("Enter adjacent vertices: ").split()

start = input("Enter starting vertex: ")
q = deque([start])
visited = {start}
print("BFS:", end=" ")
while q:
    v = q.popleft()
    print(v, end=" ")
    for x in graph.get(v, []):
        if x not in visited:
            visited.add(x)
            q.append(x)
print()
