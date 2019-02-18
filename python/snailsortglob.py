#1x1 1
#2x2 2,1,1
#3x3 3,2,2,1,1
#4x4 4,3,3,
#5x5

upper_bound, left_bound = 0, 0
lower_bound, right_bound = len(array) - 1, len(array) - 1
direction = "R"
i, j = 0, 0

def next_state(direction, i, j, upper_bound, lower_bound, left_bound, right_bound):
     if direction == "R":
          if j < right_bound:
               return "R", i, j + 1, upper_bound, lower_bound, left_bound, right_bound
          else:
               return "D", i + 1, j, upper_bound + 1, lower_bound, left_bound, right_bound
     elif direction == "D":
          if i < lower_bound:
               return "D", i + 1, j, upper_bound, lower_bound, left_bound, right_bound
          else:
               return "L", i, j - 1, upper_bound, lower_bound, left_bound, right_bound - 1
     elif direction == "L":
          if j > left_bound:
               return "L", i, j - 1, upper_bound, lower_bound, left_bound, right_bound
          else:
               return "U", i - 1, j, upper_bound, lower_bound - 1, left_bound, right_bound
     else:
          if i > upper_bound:
               return "U", i - 1, j, upper_bound, lower_bound, left_bound, right_bound
          else:
               return "R", i, j + 1, upper_bound, lower_bound, left_bound + 1, right_bound


def snail(array):
     
     total_elements = len(array) * len(array)

     res = []
     while(len(res) != total_elements):
          res.append(array[i][j])
          state = next_state(direction, i, j, upper_bound, lower_bound, left_bound, right_bound)
          direction = state[0]
          i = state[1]
          j = state[2]
          upper_bound = state[3]
          lower_bound = state[4]
          left_bound = state[5]
          right_bound = state[6]


     return res

arrays = []
arrays.append([[1,2,3],
     [4,5,6],
     [7,8,9]])
arrays.append([[1,2,3],
     [8,9,4],
     [7,6,5]])

a = arrays[0]

for i in arrays:
     print("arr")
     print(str(snail(i)))