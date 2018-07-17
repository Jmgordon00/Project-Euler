# problem06.py

'''Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.'''

def main():
    sumOfSquares = 0
    squareOfSum = 0

    i = 0
    while i <= 100:
        add = i**2
        sumOfSquares += add
        i += 1

    j = 0
    while j <= 100:
        squareOfSum += j
        j += 1

    squareOfSum *= squareOfSum

    print(squareOfSum - sumOfSquares)


if __name__ == '__main__':
    main()
