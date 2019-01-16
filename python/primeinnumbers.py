import math

def isPrime(n):
    return all([n % x != 0 for x in range(2,1 + math.ceil(math.sqrt(n)))])

#def getPrimesList(n):
#    primes = [2]
#    for i in range(3,n + 1,2):
#        if isPrime(i):
#            primes.append(i)
#
#    return primes


def primeFactors(n):
    factors = []
    primesList = []
    res = n
    resp = ""
    #primesList = getPrimesList(n)
    while res != 1:
        foundInList = False
        for i in primesList:
            if res % i == 0:
                factors.append(i)
                if not i in primesList:
                    primesList.append(i)
                res = res // i
                foundInList = True
                break

        if not foundInList:
            for i in range(2 if primesList == [] else primesList[-1], res + 1):
                if res % i == 0:
                    factors.append(i)
                    if not i in primesList:
                        primesList.append(i)
                    res = res // i
                    break

    primesSet = set(factors)
    for i in sorted(primesSet):
        count = factors.count(i)
        if count == 1:
            resp = resp + "(" + str(i) + ")"
        else:
            resp = resp + "(" + str(i) + "**" + str(count) + ")"
    return resp


tests = [86240]
for i in tests:
    print("primos de " + str(i) + " son " + str(primeFactors(i)))




    