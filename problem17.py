# problem17.py

import time

def main():
    start = time.time()
    
    singles = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
    tens = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6]
    hundred = 7
    thousand = 8
    AND = 3

    total = 0

    for n in range(1, 1000):
        c = n % 10
        b = int(((n % 100) - c) / 10)
        a = int(((n % 1000) - (b * 10) - c) / 100)

        if a != 0:
            total += singles[a] + hundred

            if b != 0 or c != 0:
                total += AND

        if b == 0 or b == 1:
            total += singles[b * 10 + c]
        else:
            total += tens[b] + singles[c]

    total += singles[1] + thousand

    print(total)



if __name__ == '__main__':
    main()
