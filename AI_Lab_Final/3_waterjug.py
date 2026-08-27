from collections import deque

def water_jug(a, b, target):
    q = deque([((0,0), [])])
    visited = set()
    while q:
        (x, y), path = q.popleft()
        if (x, y) in visited:
            continue
        visited.add((x, y))
        path = path + [(x, y)]
        if x == target or y == target:
            return path
        states = [(a,y), (x,b), (0,y), (x,0),
                  (x-min(x,b-y), y+min(x,b-y)),
                  (x+min(y,a-x), y-min(y,a-x))]
        for s in states:
            if s not in visited:
                q.append((s, path))
    return None

a = int(input("Enter first jug capacity: "))
b = int(input("Enter second jug capacity: "))
target = int(input("Enter target amount: "))
ans = water_jug(a, b, target)
if ans:
    for x in ans: print(x)
else:
    print("No solution")
