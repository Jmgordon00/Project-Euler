# problem02.py

'''Find the sum of the even fibonacci numbers from 1-4,000,000'''

def main():
    
    x1 = 1
    x2 = 2
    count = 0
    
    while x2 < 4000000:
        if x2 % 2 == 0:
            count += x2
        x2 = x1+x2
        x1 = x2-x1

    print(count)


if __name__ == "__main__":
    main()
