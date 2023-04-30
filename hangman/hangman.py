import random
from words import words
import string

def get_valid_word(words):
    word = random.choice(words)     #randomly choses word from the list
    while '-' in word or ' ' in word:
        word = random.choice(words)

    return (word.upper())

def hangman():      #to keep track of letters of words guessed and correctly guessed
    word = get_valid_word(words)
    word_letters = set(word)        #letters guessed in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set()        #keep track of words that user has guessed
    
     
    while len(word_letters) > 0:
        print("You have usedd these letters: ", " ".join(used_letters))

        word_list = (letter if letter in used_letters else '_' for letter in word)
        print("Current word:", " ".join(word_list))

        user_letter = input("Guess the letter: ".upper())       #get user input
        if user_letter in alphabet - used_letters:      #if a valid character in alphabet
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

        elif user_letter in word_letters:
            print("You have already used that character. Please try again: ")
        else:
            print("Invalid character. Please try again.")


hangman()