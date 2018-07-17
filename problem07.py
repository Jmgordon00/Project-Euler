# problem07.py

from Utilities import *

def main():
    i = 0
    n = 2
    primes = []
    
    while n != 0:
        if isPrime(n):
            primes.append(n)
            i += 1
        n += 1
        
        if i == 10001:
            n = 0

    print(primes[10000])


if __name__ == '__main__':
    main()
