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


if __name__ == "__main__":
    for i in range(4):
        print("Para %d parentesis" % (i))
        print(str(balanced_parens(i)))