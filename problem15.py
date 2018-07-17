# problem15.py

import time

def route(size):
    grid = [1] * size

    for i in range(size):
        for j in range(i):
            grid[j] += grid[j-1]
        grid[i] = 2 * grid[i-1]

    return grid[size - 1]

def main():
    start = time.time()

    print(route(20))
    print(time.time() - start)


 

if __name__ == '__main__':
    main()
