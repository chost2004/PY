'''
example: [['XXX', 3], ['XXXXX', 6], ['XXXXXX', 9], ['XXX',2]]
when you need 4 chairs:
result -- > [0, 1, 3] (no chairs free in room 0, take 1 from room 1,
take 3 from room 2. No need to consider room 4 as you have your 4 chairsalready.
If you need no chairs, return 'Game On'.
If there aren't enough spare chairs available, return 'Not enough!'
meeting([['XXX', 3], ['XXXXX', 6], ['XXXXXX', 9]], 4) ---> [0, 1, 3]
meeting([['XXX', 1], ['XXXXXX', 6], ['X', 2], ['XXXXXX', 8], ['X', 3], ['XXX', 1]], 5) ---> [0, 0, 1, 2, 2]
meeting([['XX', 2], ['XXXX', 6], ['XXXXX', 4]], 0) ---> 'Game On'

'''
def meeting(rooms, need):
    if need == 0:
        return 'Game On'
    chairs = 0
    result = []
    for room in rooms:
        free_chairs = room[1] - len(room[0]) if (room[1] - len(room[0]))>0 else 0
        chairs = chairs + free_chairs
        result.append(free_chairs)
        if chairs >= need:
            break
    if chairs >= need:
        return result
    return 'Not enough!'
print ("meeting([['XXX', 3], ['XXXXX', 6], ['XXXXXX', 9]], 4):\n", meeting([['XXX', 3], ['XXXXX', 6], ['XXXXXX', 9]], 4), "\n")
print ("meeting([['XXX', 1], ['XXXXXX', 6], ['X', 2], ['XXXXXX', 8], ['X', 3], ['XXX', 1]], 5):\n", meeting([['XXX', 1], ['XXXXXX', 6], ['X', 2], ['XXXXXX', 8], ['X', 3], ['XXX', 1]], 5), "\n")
print ("meeting([['XX', 2], ['XXXX', 6], ['XXXXX', 4]], 0)\n", meeting([['XX', 2], ['XXXX', 6], ['XXXXX', 4]], 0), '\n')

