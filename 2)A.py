import heapq

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('E', 1), ('F', 3)],
    'D': [],
    'E': [('F', 2)],
    'F': []
}

h = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 1,
    'E': 2,
    'F': 0
}

def astar(start, goal):
    pq = [(h[start], 0, start, [start])]

    while pq:
        f, g, node, path = heapq.heappop(pq)

        if node == goal:
            return path, g

        for neighbor, cost in graph[node]:
            new_g = g + cost
            new_f = new_g + h[neighbor]

            heapq.heappush(pq, (new_f, new_g,
                                neighbor, path + [neighbor]))

path, cost = astar('A', 'F')

print("Optimal Path:", path)
print("Total Cost:", cost)