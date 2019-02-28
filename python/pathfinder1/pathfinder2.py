import cProfile
import bisect as bi
import mazes

def get_possible_next_positions(mazearr, pos):
    pnp = []
    n = len(mazearr)
    #if can move down
    if pos[0] < n - 1 and mazearr[pos[0] + 1][pos[1]] != "W":
        pnp.append((pos[0] + 1, pos[1]))
        #bi.insort(pnp,(pos[0] + 1, pos[1]))
    #if can move right
    if pos[1] < n - 1 and mazearr[pos[0]][pos[1] + 1] != "W":
        pnp.append((pos[0], pos[1] + 1))
        #bi.insort(pnp,(pos[0], pos[1] + 1))
    #if can move left
    if pos[1] > 0 and mazearr[pos[0]][pos[1] - 1] != "W":
        pnp.append((pos[0], pos[1] - 1))
        #bi.insort(pnp,(pos[0], pos[1] - 1))
    #if can move up
    if pos[0] > 0 and mazearr[pos[0] - 1][pos[1]] != "W":
        pnp.append((pos[0] - 1, pos[1]))
        #bi.insort(pnp,(pos[0] - 1, pos[1]))

    return pnp

#def pointIsOpen(open_list, point):
#    return inSorted(open_list, point)
#
#def pointIsClosed(closed_list, point):
#    return inSorted(closed_list, point)
#
#def isInpnp(pnp,point):
#    return inSorted(pnp, point)

def in_sorted(sorted_list, point):
    l = bi.bisect_left(sorted_list,point)
    if l == len(sorted_list):
        return False
    
    return point == sorted_list[l]


def path_finder(maze):
    mazearr = maze.split("\n")
    n = len(mazearr)
    if n == 1:
        return True
    open_points = [(0,0)]
    closed_points = []
    while len(open_points) > 0:
        current_point = open_points.pop(0)
        pnp = get_possible_next_positions(mazearr, current_point)
        if (n-1,n-1) in pnp:
            return True

        for i in pnp:
            #if not inSorted(open_points,i) and not pointIsClosed(closed_points,i):
            if not in_sorted(closed_points,i) and not in_sorted(open_points,i):
                bi.insort(open_points,i)

        bi.insort(closed_points,current_point)

    return False 


def main(mazes):
    n = 1
    for i in mazes:
        print(str(n) + ") " + str(path_finder(i)))
        n += 1


mazes = mazes.get_mazes()
cProfile.run('main(mazes)')