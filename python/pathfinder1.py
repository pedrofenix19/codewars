def getPossibleNextPositions(mazearr, pos):
    pnp = []
    print("maze " + str(mazearr))
    print("maze " + str(pos[0]))
    #if can move down
    if pos[0] < len(mazearr) - 1 and mazearr[pos[0] + 1] != "W":
        pnp.append((pos[0] + 1, pos[1]))
    #if can move right
    if pos[1] <= len(mazearr) - 1 and mazearr[pos[1] + 1] != "W":
        pnp.append((pos[0], pos[1] + 1))
    #if can move left
    if pos[1] > 0 and mazearr[pos(1) - 1] != "W":
        pnp.append((pos[0], pos[1] - 1))
    #if can move up
    if pos[0] > 0 and mazearr[pos(0) - 1] != "W":
        pnp.append((pos[0] - 1, pos[1]))

    return pnp

def path_finder(maze):
    mazearr = maze.split("\n")
    print(str(mazearr))
    n = len(mazearr)
    mazearr[n-1] = mazearr[n-1][:-1] + "G"
    print(str(mazearr))
    paths = [[(0,0)]]
    i = 0
    while i < len(paths):
        p = paths.pop(0)
        print("p es " + str(p))
        pnp = getPossibleNextPositions(mazearr, p[-1])
        if any([ mazearr[x[0]][x[1]] == "G" for x in pnp]):
            return True

        for i in pnp:
            if all([x[len(x) - 1][0] != i[0] and x[len(x) - 1][1] != i[1] for x in paths]):
                paths.append(p + [i])

        i += 1

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

for i in [a,b,c,d]:
    print(str(path_finder(i)))