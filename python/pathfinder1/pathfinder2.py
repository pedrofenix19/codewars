import cProfile
import bisect as bi

def get_possible_next_positions(mazearr, pos):
    pnp = []
    n = len(mazearr)
    #if can move down
    if pos[0] < n - 1 and mazearr[pos[0] + 1][pos[1]] != "W":
        #pnp.append((pos[0] + 1, pos[1]))
        bi.insort(pnp,(pos[0] + 1, pos[1]))
    #if can move right
    if pos[1] < n - 1 and mazearr[pos[0]][pos[1] + 1] != "W":
        #pnp.append((pos[0], pos[1] + 1))
        bi.insort(pnp,(pos[0], pos[1] + 1))
    #if can move left
    if pos[1] > 0 and mazearr[pos[0]][pos[1] - 1] != "W":
        #pnp.append((pos[0], pos[1] - 1))
        bi.insort(pnp,(pos[0], pos[1] - 1))
    #if can move up
    if pos[0] > 0 and mazearr[pos[0] - 1][pos[1]] != "W":
        #pnp.append((pos[0] - 1, pos[1]))
        bi.insort(pnp,(pos[0] - 1, pos[1]))

    return pnp

def pointIsOpen(open_list, point):
    return inSorted(open_list, point)

def pointIsClosed(closed_list, point):
    return inSorted(closed_list, point)

def inSorted(sorted_list, point):
    return False if len(sorted_list) == 0 else bi.bisect_left(sorted_list,point) != bi.bisect_right(sorted_list, point)
    #if len(sorted_list) == 0:
    #    return False
    #l = bi.bisect_left(sorted_list,point)
    #r = bi.bisect_right(sorted_list, point)
    #b = l == r
    #return not b



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
        if inSorted(pnp,(n-1,n-1)):
            return True

        for i in pnp:
            if not pointIsOpen(open_points,i) and not pointIsClosed(closed_points,i):
                bi.insort(open_points,i)

        bi.insort(closed_points,current_point)

    return False 


def main():
    a = "\n".join([
      ".W.",
      ".W.",
      "..."
    ])

    b = "\n".join([
      ".W.",
      ".W.",
      "W.."
    ])

    c = "\n".join([
      "......",
      "......",
      "......",
      "......",
      "......",
      "......"
    ])

    d = "\n".join([
      "......",
      "......",
      "......",
      "......",
      ".....W",
      "....W."
    ])

    e = "\n".join([
      ".W....",
      ".W.WW.",
      ".W.W..",
      ".W.W.W",
      ".W.W..",
      "...W.."
    ])

    f = "\n".join([
    ".W....",
    ".W.WW.",
    ".W.W..",
    ".W.W.W",
    ".W.W..",
    "...W.W"
    ])

    g = "\n".join([
    "..W...W.W ",
    "..WW..WWW ",
    ".....W... ",
    ".W..W.... ",
    "W....WWWW ",
    ".......W. ",
    "..W...... ",
    "WW.WW..WW ",
    ".....W..."
    ])

    h = "\n".join([
    ".W...W...W...",
    ".W.W.W.W.W.W.",
    ".W.W.W.W.W.W.",
    ".W.W.W.W.W.W.",
    ".W.W.W.W.W.W.",
    ".W.W.W.W.W.W.",
    ".W.W.W.W.W.W.",
    ".W.W.W.W.W.W.",
    ".W.W.W.W.W.W.",
    ".W.W.W.W.W.W.",
    ".W.W.W.W.W.W.",
    ".W.W.W.W.W.W.",
    "...W...W...W."
    ])

    i = "\n".join([
    ".W...W...W...",
    ".W.W.W.W.W.W.",
    ".W.W.W.W.W.W.",
    ".W.W.W.W.W.W.",
    ".W.W.W.W.W.W.",
    ".W.W.W.W.W.W.",
    ".W.W.W.W.W.W.",
    ".W.W.W.W.W.W.",
    ".W.W.W.W.W.W.",
    ".W.W.W.W.W.W.",
    ".W.W.W.W.W.W.",
    ".W.W.W.W.W.W.",
    "...W...W...W."
    ])

    j = "\n".join([
    ".............",
    "WWWWWWWWWWWW.",
    ".............",
    ".WWWWWWWWWWWW",
    ".............",
    "WWWWWWWWWWWW.",
    "......W......",
    ".WWWWWWWWWWWW",
    ".............",
    "WWWWWWWWWWWW.",
    ".............",
    ".WWWWWWWWWWWW",
    "............."
    ])

    for i in [a,b,c,d,e,f,g,h,i,j]:
        print(str(path_finder(i)))



cProfile.run('main()')