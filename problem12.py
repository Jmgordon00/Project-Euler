# problem12.py

from Utilities import *

def main():
    i = 1
    n = 0
    
    while i != 0:
        if len(factors(n)) > 500:
            break

        n += i
        i += 1

    print(n)

if __name__ == '__main__':
    main()
