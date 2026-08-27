from collections import deque

def solve(start, goal):
    q = deque([(start, [])])
    visited = {start}
    while q:
        s, path = q.popleft()
        path = path + [s]
        if s == goal:
            return path
        z = s.index(0)
        r, c = divmod(z, 3)
        for dr, dc in [(1,0),(-1,0),(0,1),(0,-1)]:
            nr, nc = r+dr, c+dc
            if 0 <= nr < 3 and 0 <= nc < 3:
                a = list(s)
                nz = nr*3 + nc
                a[z], a[nz] = a[nz], a[z]
                ns = tuple(a)
                if ns not in visited:
                    visited.add(ns)
                    q.append((ns, path))
    return None

start = tuple(map(int, input("Enter initial state: ").split()))
goal = tuple(map(int, input("Enter goal state: ").split()))
ans = solve(start, goal)
if ans:
    for x in ans: print(x)
    print("Moves:", len(ans)-1)
else:
    print("No solution")
