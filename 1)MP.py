regions = ['A', 'B', 'C', 'D', 'E']

neighbors = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'E'],
    'D': ['B', 'E'],
    'E': ['C', 'D']
}

colors = ['Red', 'Green', 'Blue']
assignment = {}

def is_valid(region, color):
    for n in neighbors[region]:
        if n in assignment and assignment[n] == color:
            return False
    return True

def solve():
    if len(assignment) == len(regions):
        return True

    region = [r for r in regions if r not in assignment][0]

    for color in colors:
        if is_valid(region, color):
            assignment[region] = color

            if solve():
                return True

            del assignment[region]

    return False

if solve():
    print("Valid Colouring:")
    for r in assignment:
        print(r, "=", assignment[r])
else:
    print("No Solution")