import bisect as b

def dbl_linear(n):
    u = [1]
    for x in range(n):
        y, z = 2 * u[x] + 1, 3 * u[x] + 1
        b.insort(u,y)
        b.insort(u,z)

    return list(set(u))[n]