def vacuum(a, b, pos):
    room = {'A': a, 'B': b}
    cost = 0
    while 'Dirty' in room.values():
        print("Position:", pos, room)
        if room[pos] == 'Dirty':
            room[pos] = 'Clean'
            cost += 1
            print("Action: SUCK")
        else:
            pos = 'B' if pos == 'A' else 'A'
            cost += 1
            print("Action: MOVE")
    print("Final:", room, "| Cost:", cost)

a = input("Enter A (Clean/Dirty): ").capitalize()
b = input("Enter B (Clean/Dirty): ").capitalize()
pos = input("Enter starting position (A/B): ").upper()
if a not in ('Clean','Dirty') or b not in ('Clean','Dirty') or pos not in ('A','B'):
    print("Invalid input")
else:
    vacuum(a, b, pos)
