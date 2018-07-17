# problem14.py

import time

def collatz(n):
    count = 1
    
    while n > 1:
        count += 1

        if n % 2 == 0:
            n = n/2
        else:
            n = 3*n + 1
    return count

def main():
    start = time.time()
    maxLength = 1
    answer = 1
    
    for n in range(1000000):
        length = collatz(n)
        
        if length > maxLength:
            maxLength = collatz(n)
            answer = n
    
    print(answer)
    print(time.time() - start)


if __name__ == '__main__':
    main()
