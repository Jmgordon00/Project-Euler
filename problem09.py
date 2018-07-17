# problem09.py

def main():
    for a in range(3,1000):
        for b in range(a+1, 1009):
            c = (a**2 + b**2) ** 0.5

            if a+b+c == 1000:
                print(a*b*c)
                break


if __name__ == '__main__':
    main()
