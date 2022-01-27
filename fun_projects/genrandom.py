# Guess a random Number

def guessnum(number):
    answer = 9
    if number > answer:
        print('The Number entered is too high')
        num = int(input('>> '))
        guessnum(num)
    elif number < answer:
        print('The number entered is too low')
        num = int(input('>> '))
        guessnum(num)
    elif number == answer:
        print('Yes! You got it!')
print(' I am thinking of a number between 1 and 10')
num = int(input("Guess what it is :  "))
guessnum(num)
