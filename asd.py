def nprime(number):
    tempNumber=0
    primes = [1]
    while len(primes)<number:
        if tempNumber < primes[-1]: tempNumber = primes[-1]
        tempNumber += 1
        if (isprime(tempNumber) == "prime"): primes.append(tempNumber)
    
    return(primes[-1])

def isprime(n):
    for i in range(2,n-1):
        if n % i == 0:
            return("!prime")
    return("prime")
print(nprime(10))