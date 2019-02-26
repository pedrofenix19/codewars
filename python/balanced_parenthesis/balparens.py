import itertools as it
import time

def are_parens_balanced(s):
    opening_parens, closing_parens = 0, 0
    for p in s:
        if p == "(":
            opening_parens += 1
        else:
            closing_parens += 1

        if closing_parens > opening_parens:
            return False

    return True

def balanced_parensitertools(n):
    complete_parens = "(" * n + ")" * n
    return [''.join(s) for s in set(it.permutations(complete_parens)) if are_parens_balanced(s) ]


def bp(pstr, balanced, openingleft, closingleft):
    #print("bp %s, op %d, cl %d" % (pstr, openingleft, closingleft))
    if openingleft == 0 and closingleft == 0:
        #print("adding %s" %(pstr))
        balanced.append(pstr)
        return

    if pstr.count(")") > pstr.count("("):
        #print("hay desbalance")
        return

    if openingleft > 0:
        bp(pstr + "(", balanced, openingleft - 1, closingleft)
    
    if closingleft > 0:
        bp(pstr + ")", balanced, openingleft, closingleft - 1)


def balanced_parensdin(n):
    balanced = []
    bp("",balanced,n,n)    
    return balanced


for i in range(10):
    print("Para %d parentesis" % (i))
    start_time_it = time.time()
    print(str(balanced_parensitertools(i)))
    end_time_it = time.time()
    print(str(balanced_parensdin(i)))
    end_time_din = time.time()
    print("it %.8f" % (end_time_it - start_time_it))
    print("di %.8f" % (end_time_din - end_time_it))