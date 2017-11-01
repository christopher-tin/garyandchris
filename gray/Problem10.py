def sumOfPrimes(n):
    sum = 0 
    primes = [True] * n 
    primes[0],primes[1] = [None]*2
    for ind,val in enumerate(primes):
        if val is True and ind > n ** 0.5 + 1:
            sum += ind
        elif val is True:
            primes[ind*2::ind] = [False] * (((n - 1)//ind) - 1)
            sum += ind
            
    return sum
print (sumOfPrimes(2000000))


