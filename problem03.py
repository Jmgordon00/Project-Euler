# problem03.py

# What is the largest prime factor of the number 600851475143?


def main():

    n = 600851475143
    x = 3

    while x < n:
        if n % x == 0:
            n = n/x
        x += 2

    print(n)

if __name__ == "__main__":
    main()
        
