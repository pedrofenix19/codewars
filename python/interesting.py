import re 

def is_interesting(n, ap):
    if is_i(n, ap):   
        return 2
    if is_i(n + 1, ap) or is_i(n+2, ap):
        return 1
    else:
        return 0

def is_i(n, ap):
    if n <= 99:
        return False
        
    if n in ap or re.match(r'\d{1}00+', str(n)) \
        or str(n) == str(n)[::-1] or is_ascending(n) \
        or is_descending(n):
        return True
        
def is_ascending(n):
    a = all( ((int(str(n)[i]) - 1) % 10) + 1 == (int(str(n)[i + 1]) - 1) % 10 for i in range(len(str(n)) - 1)) \
     and all(i != "0" for i in str(n)[:-1])
    print(str(n) + " es ascendente " + str(a))
    return a

def is_descending(n):
    a = all( int(str(n)[i]) - 1 == int(str(n)[i+1]) for i in range(len(str(n)) - 1))
    print(str(n) + " es descendente" + str(a))
    return a

inputs = [
    [3, [1337, 256]],
    [1336, [1337, 256]],
    [1337, [1337, 256]],
    [11208, [1337, 256]],
    [11209, [1337, 256]],
    [11211, []],
    [109, []],
    [10, []],
    [int("09"), []],
]
    
    
for i in inputs:
    print(str(i[0]) + ":" +str(is_interesting(i[0],i[1])))
    #print(str(i[0]) + ":" +str(is_interesting(i[0])))