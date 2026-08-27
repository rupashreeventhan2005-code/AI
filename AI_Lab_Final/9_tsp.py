from itertools import permutations

n = int(input("Enter number of cities: "))
cost = []
for i in range(n):
    cost.append(list(map(int, input().split())))

best = float('inf')
best_path = None
for p in permutations(range(1, n)):
    path = (0,) + p + (0,)
    total = 0
    for i in range(n):
        total += cost[path[i]][path[i+1]]
    if total < best:
        best = total
        best_path = path

print("Best path:", best_path)
print("Minimum cost:", best)
