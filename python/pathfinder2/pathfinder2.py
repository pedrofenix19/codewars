import cProfile
import mazes

def get_possible_next_positions(mazearr, pos):
    pnp = []
    n = len(mazearr)
    #if can move down
    if pos[0] < n - 1 and mazearr[pos[0] + 1][pos[1]] != "W":
        pnp.append((pos[0] + 1, pos[1], pos[2] + 1))
    #if can move right
    if pos[1] < n - 1 and mazearr[pos[0]][pos[1] + 1] != "W":
        pnp.append((pos[0], pos[1] + 1, pos[2] + 1))
    #if can move left
    if pos[1] > 0 and mazearr[pos[0]][pos[1] - 1] != "W":
        pnp.append((pos[0], pos[1] - 1, pos[2] + 1))
    #if can move up
    if pos[0] > 0 and mazearr[pos[0] - 1][pos[1]] != "W":
        pnp.append((pos[0] - 1, pos[1], pos[2] + 1))

    return pnp

def path_finder(maze):
    mazearr = maze.split("\n")
    n = len(mazearr)
    open_points = [(0,0,0)]
    closed_points = []
    while len(open_points) > 0:
        current_point = open_points.pop(0)
        pnp = get_possible_next_positions(mazearr, current_point)

        if any([ p[0] == n - 1 and p[1] == n - 1  for p in pnp]):
            return pnp[0][2]

        for i in pnp:
          if not any([ i[0] == j[0] and i[1] == j[1] for j in open_points + closed_points]):
            open_points.append(i)

        closed_points.append(current_point)

    return False 


def main(mazes):
    n = 1
    for i in mazes:
        print(str(n) + ") " + str(path_finder(i)))
        n += 1


mazes = mazes.get_mazes()
cProfile.run('main(mazes)')