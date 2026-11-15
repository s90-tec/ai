rooms = {'A': 'Dirty', 'B': 'Dirty'}
location = 'A'

while 'Dirty' in rooms.values():

    if rooms[location] == 'Dirty':
        print("Cleaning", location)
        rooms[location] = 'Clean'

    elif location == 'A':
        location = 'B'
        print("Moving to B")

    else:
        location = 'A'
        print("Moving to A")

print("All rooms are clean!")
print(rooms)
