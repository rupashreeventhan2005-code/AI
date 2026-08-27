from collections import deque

def valid(m, c, n):
    return 0 <= m <= n and 0 <= c <= n and \
           (m == 0 or m >= c) and (n-m == 0 or n-m >= n-c)

def solve(n, boat):
    start, goal = (n, n, 0), (0, 0, 1)
    q = deque([(start, [])])
    visited = set()
    while q:
        state, path = q.popleft()
        if state in visited:
            continue
        visited.add(state)
        m, c, side = state
        path = path + [state]
        if state == goal:
            return path
        for x in range(boat+1):
            for y in range(boat+1):
                if 1 <= x+y <= boat:
                    nm, nc = (m-x, c-y) if side == 0 else (m+x, c+y)
                    ns = (nm, nc, 1-side)
                    if valid(nm, nc, n) and ns not in visited:
                        q.append((ns, path))
    return None

n = int(input("Enter missionaries/cannibals: "))
boat = int(input("Enter boat capacity: "))
ans = solve(n, boat)
if ans:
    for x in ans: print(x)
    print("Trips:", len(ans)-1)
else:
    print("No solution")
