import random
def random_guess(x):
    ranumb=random.randint(1,x)
    guess=0
    while guess!=ranumb:
        guess=int(input('Guess a number between 1 and 100: '))
        if guess>ranumb:
            print("sorry too high")
        elif guess<ranumb:
            print('sorry too low')
    print(f'congrats, the number is {ranumb}')
    pass
random_guess(100)
    