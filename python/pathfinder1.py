import time

def get_possible_next_positions(mazearr, pos):
    pnp = []
    n = len(mazearr)
    #if can move down
    if pos[0] < n - 1 and mazearr[pos[0] + 1][pos[1]] != "W":
        pnp.append((pos[0] + 1, pos[1]))
    #if can move right
    if pos[1] < n - 1 and mazearr[pos[0]][pos[1] + 1] != "W":
        pnp.append((pos[0], pos[1] + 1))
    #if can move left
    if pos[1] > 0 and mazearr[pos[0]][pos[1] - 1] != "W":
        pnp.append((pos[0], pos[1] - 1))
    #if can move up
    if pos[0] > 0 and mazearr[pos[0] - 1][pos[1]] != "W":
        pnp.append((pos[0] - 1, pos[1]))

    return pnp

def path_finder(maze):
    mazearr = maze.split("\n")
    n = len(mazearr)
    open_points = [(0,0)]
    closed_points = []
    while len(open_points) > 0:
        current_point = open_points.pop(0)
        pnp = get_possible_next_positions(mazearr, current_point)

        if any([ x == (n-1,n-1) for x in pnp]):
            return True

        for i in pnp:
            if any([x == i for x in closed_points]):
                break
            
            open_points.append(i)

        closed_points.append(current_point)

    return False 



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

st = time.time()
for i in [a,b,c,d,e]:
    print("*********************************************************" + str(path_finder(i)))
et = time.time()

print("Time: %.6f secs" % (et - st))