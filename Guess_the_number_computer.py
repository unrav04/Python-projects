import random
def comp_guess():
    print('guess a number between 1 and 100. I will try to guess the number you are thinking of')
    comp_guess=-1
    x=0
    y=100
    z=''
    while z!='correct':
        comp_guess=random.randint(x,y)
        print(comp_guess)
        z=input('if the guess is too high, type 1, If it is too low, type 0, And type correct, if it is right. (If you made a mistake in the limits, type reset, to reset the limits): ')
        if(y-x>=10):
            if z=='1':
                y=comp_guess
            elif z=='0':
                x=comp_guess
            elif z=='correct':
                print('thank you for playing')
                break
            elif z=='reset':
                x=0
                y=100
                print('it is reset')
        else:
            if z=='1':
                y=y-1
            elif z=='0':
                x=x+1
            elif z=='correct':
                print('thank you for playing')
                break
            elif z=='reset':
                x=0
                y=100
                print('it is reset')
        pass
    print('EZ')

comp_guess()
    