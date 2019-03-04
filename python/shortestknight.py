import numpy as np

def get_next_hops(pos):
    next_hops = []
    #if can move UUR
    if pos[0] > 1 and pos[1] < 7:
        next_hops.append((pos[0] - 2, pos[1] + 1))
    #if can move RRU
    if pos[0] > 0 and pos[1] < 6:
        next_hops.append((pos[0] - 1, pos[1] + 2))
    #if can move RRD
    if pos[0] < 7 and pos[1] < 6:
        next_hops.append((pos[0] + 1, pos[1] + 2))
    #if can move DDR
    if pos[0] < 6 and pos[1] < 7:
        next_hops.append((pos[0] + 2, pos[1] + 1))
    #if can move DDL
    if pos[0] < 6 and pos[1] > 0:
        next_hops.append((pos[0] + 2, pos[1] - 1))
    #if can move LLD
    if pos[0] < 7 and pos[1] > 1:
        next_hops.append((pos[0] + 1, pos[1] - 2))
    #if can move LLU
    if pos[0] > 0 and pos[1] > 1:
        next_hops.append((pos[0] - 1, pos[1] - 2))
    #if can move UUL
    if pos[0] > 1 and pos[1] > 0:
        next_hops.append((pos[0] - 2, pos[1] - 1))

    return next_hops

def knight(p1, p2):
    pos_mapping = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    start_pos = (int(p1[1])-1, pos_mapping[p1[0]])
    end_pos = (int(p2[1])-1, pos_mapping[p2[0]])
    board = np.full((8,8), -1)
    board[start_pos[0],start_pos[1]] = 0
    open_points = [start_pos]

    while len(open_points) > 0:
        current_point = open_points.pop(0)
        next_hops = get_next_hops(current_point)

        if end_pos in next_hops:
            return board[current_point[0]][current_point[1]] + 1

        for point in [x for x in next_hops if board[x[0]][x[1]] == -1]:
            board[point[0]][point[1]] = board[current_point[0]][current_point[1]] + 1
            open_points.append(point)

    return 0






arr = [['a1', 'c1', 2], ['a1', 'f1', 3], ['a1', 'f3', 3], ['a1', 'f4', 4], ['a1', 'f7', 5]]
for x in arr:
    print(str(knight(x[0], x[1])))

