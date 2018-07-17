# Utilities.py

from math import *
'''Project Euler Utilities'''

def isPalindrome(n):
    string = str(n)
    backwardString = string[::-1]

    return string == backwardString


def isEven(n):
    return n % 2 == 0


def factors(n):
    factors = []
    i = 1

    maxDiv = int(sqrt(n)) + 1
    
    while i < maxDiv:
        if n % i == 0:
            factors.append(i)
            factors.append(int(n/i))
        i += 1

    return factors
    

def isPrime(n):
    if n < 2:
        return False
    return factors(n) == [1,n]


def isPrimeHigh(n):
    pass


def isPythagoreanTriple(a, b, c):
    
    return a**2 + b**2 == c**2
