import random
import string
from words import words

def legit_word(words):
    word=random.choice(words)
    while '-' in word or ' ' in word:
        word=random.choice(words)
    return word.upper()
def hangman(word):
    word=legit_word(words)
    comp_word=set(word)
    used_letter=set()
    alphabet = set(string.ascii_uppercase)
    while(len(comp_word)>0):
        user_letter=input('INPUT A WORD: ').upper()
        if user_letter in alphabet-used_letter:
            used_letter.add(user_letter)
            if user_letter in comp_word:
                comp_word.remove(user_letter)
        elif user_letter in used_letter:
            print('already used')
        else:
            print('invalid letter')
        print('you haave used these letters: ',' '.join(used_letter))
        word_list=[letter if letter in used_letter else '-' for letter in word]
        print('Current Word:  ', ' '.join(word_list))
    
hangman(words)