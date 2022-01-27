## Guess number with error handling
def guessnum(number):
    answer = 9
    if number > answer:
        print('The Number entered is too high')
        reenter()
    elif number < answer:
        print('The number entered is too low')
        reenter()
    elif number == answer:
        print('Yes! You got it!')

def enter_fun():
    print(' I am thinking of a number between 1 and 10')
    num1 = input("Guess what it is :  ")
    try:
        num = int(num1)
        guessnum(num)
    except:
        print('That is not a number')
        reenter()

def reenter():
    try:
        num = int(input('>> '))
        guessnum(num)
    except:
        print('That is not a number')
        num = int(input('>> '))
        guessnum(num)

enter_fun()
