import math

def isPrime(n):
    return all([n % x != 0 for x in range(2,1 + math.floor(math.sqrt(n)))])

def getPrimesList(n):
    primes = []
    for i in range(2,n + 1):
        if isPrime(i):
            primes.append(i)

    return primes


def primeFactors(n):
    factors = []
    res = n
    resp = ""
    primesList = getPrimesList(n)
    while res != 1:
        for i in primesList:
            if res % i == 0:
                factors.append(i)
                res = res // i
                break

    primesSet = set(factors)
    for i in primesSet:
        count = factors.count(i)
        if count == 1:
            resp = resp + "(" + str(i) + ")"
        else:
            resp = resp + "(" + str(i) + "**" + str(count) + ")"
    return resp

tests = [7775460]
for i in tests:
    print("primos de " + str(i) + " son " + str(primeFactors(i)))



    