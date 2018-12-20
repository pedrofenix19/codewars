expanded_form = lambda num: ''.join([str(num)[x] + '0'*(len(str(num))-x-1) + " + " if str(num)[x] != '0' else '' for x in range(len(str(num)))])[:-3]


for i in [12, 42, 70304]:
    print(expanded_form(i))