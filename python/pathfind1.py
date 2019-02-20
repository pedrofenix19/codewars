#def find_way(cur_x, cur_y, n):
#    if cur_x + 1 < 

def path_finder(maze):
    n = len(maze)
    print("n es %s" %(n))
    return





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

print(str(path_finder(a)))
print(str(path_finder(b)))
print(str(path_finder(c)))
print(str(path_finder(d)))
