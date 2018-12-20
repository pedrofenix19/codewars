def lsd(pyramid):
    slide = pyramid[0][0]
    pos = 0
    for i in pyramid[1:]:
        if pos == 0:
            if i[pos] > i[pos + 1]:
                slide += i[pos]
            else:
                slide += i[pos + 1]
                pos = 1
        elif pos == len(i) - 1:
            if i[pos] > i[pos -1]:
                slide +=1
    return slide


print(lsd([[3], [7, 4], [2, 4, 6], [8, 5, 9, 3]]))