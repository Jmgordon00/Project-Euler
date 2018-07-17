# problem10.py

from Utilities import *

def main():
    primeSum = 0
    
    for n in range(2000000):
        if isPrime(n):
            primeSum += n

    print(primeSum)


if __name__ == '__main__':
    main()
