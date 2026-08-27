from itertools import permutations

w1 = input("Enter first word: ").upper()
w2 = input("Enter second word: ").upper()
w3 = input("Enter result word: ").upper()

letters = sorted(set(w1 + w2 + w3))
if len(letters) > 10:
    print("Too many letters")
else:
    for p in permutations(range(10), len(letters)):
        d = dict(zip(letters, p))
        if d[w1[0]] == 0 or d[w2[0]] == 0 or d[w3[0]] == 0:
            continue
        n1 = int(''.join(str(d[x]) for x in w1))
        n2 = int(''.join(str(d[x]) for x in w2))
        n3 = int(''.join(str(d[x]) for x in w3))
        if n1 + n2 == n3:
            print(d)
            print(n1, "+", n2, "=", n3)
            break
    else:
        print("No solution")
