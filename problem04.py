# problem04.py

'''Find the largest palindrome made from the product of two 3-digit numbers.'''


def isPalindrome(n):
    string = str(n)
    backwardString = string[::-1]

    return string == backwardString

    
def main():

    num1 = 100
    num2 = 100
    product = 0
    test = 0

    while num1 < 1000:
        while num2 < 1000:
            test = num1 * num2
            if isPalindrome(test):
                if test > product:
                    product = test
            num2+=1
        num1+=1
        num2 = 100

    print(product)


if __name__ == "__main__":
    main()
