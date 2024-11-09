import random
def rock_paper_scissors():
    c=0
    h=0
    print('welcome to rock papers scissors')
    while True:
        print()
        hmove=(input('Type *rock* , *paper* or *scissors*: '))
        print()
        choises=['rock','paper','scissors']
        cmove=random.choice(choises)
        if hmove=='rock':
            if cmove=='paper':
                print(f"You chose {hmove} and the computer chose {cmove}. You loose")
                c=c+1
            elif cmove=='scissors':
                print(f"You chose {hmove} and the computer chose {cmove}. You won")
                h=h+1
            else:
                print(f"You chose {hmove} and the computer chose {cmove}. Its a draw")
        elif hmove=='paper':
            if cmove=='scissors':
                print(f"You chose {hmove} and the computer chose {cmove}. You loose")
                c=c+1
            elif cmove=='rock':
                print(f"You chose {hmove} and the computer chose {cmove}. You won")
                h=h+1
            else:
                print(f"You chose {hmove} and the computer chose {cmove}. Its a draw")
        elif hmove=='scissors':
            if cmove=='rock':
                print(f"You chose {hmove} and the computer chose {cmove}. You loose")
                c=c+1
            elif cmove=='paper':
                print(f"You chose {hmove} and the computer chose {cmove}. You won")
                h=h+1
            else:
                print(f"You chose {hmove} and the computer chose {cmove}. Its a draw")
        else:
            print('Incorrect Input')
        print()
        print(f"The computer has won {c} times, and you have won {h} times")
        print()
        
        r=input('Do you wanna play again? y/n: ')
        print()
        if r=='n':
            print('Thank you for playing')
            break
        else:
            continue
        pass
rock_paper_scissors()