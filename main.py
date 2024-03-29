import random
def guess(x):
    randomNum = random.randint(1, x)
    guess = 0
    while guess != randomNum:
        guess = int(input(f'Guess a number between 1 and {x}: '))
        if guess < randomNum:
            print('Sorry, guess again. Too low.')
        elif guess > randomNum:
                print('Sorry, guess again. Too high.')

    print(f'Yay, congrats. You have guessed the right number!')

# def userInput():
#     x = int(input("Enter a number: "))
#     return x

def computerguess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low
        feedback = input(f'Is {guess} too high (H), too low (L) or correct (C)').lower()
        if feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1

    print(f'Yay! The computer guessed your number correctly!')

computerguess(100)