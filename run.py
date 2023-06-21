# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random
from words import words

#words source: https://github.com/Xethron/Hangman

def main_screen():
    print("""  _____ _            _   _                                         
 |_   _| |__   ___  | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __  
   | | | '_ \ / _ \ | |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
   | | | | | |  __/ |  _  | (_| | | | | (_| | | | | | | (_| | | | |
   |_| |_| |_|\___| |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                       |___/                       """)
    print ('WELCOME TO THE HANGMAN')
    print('Would you like to play? Press 1')
    print('Change difficult? Press 2')
    first_option = input('Choose your option: ')
    check_answer(first_option)

def check_answer(data):
    try:
        answer = int(data)

    except ValueError:
        print(f'{data} is not a number, please try again.')

    else:
        if answer == 1:
            print('soon')
        
        elif answer == 2:
            difficulty = input('Please type "E" for easy, "M" for medium or "H" for hard.')
            change_difficulty(difficulty)

        else:
            print(f'Sorry, {data} is not a valid anwer. Please try again.')

def change_difficulty(data):

    try:
        option = data.isalpha()

    except TypeError:
        print(f'{data} is not a valid option, please try again.')

    else:
        if data.lower() == 'e':
            print('You chose the difficult: easy.')
            random_word = choose_word('e')
            game_structure(random_word)
        
        elif data.lower() == 'm':
            random_word = choose_word('m')
            game_structure(random_word)

        elif data.lower() == 'h':
            random_word = choose_word('h')
            game_structure(random_word)

        else:
            print(f'Sorry, {data} is not a valid answer. Please try again: ')


def choose_word(data):
    word = random.choice(words)
    if data == 'e':
        while len(word) >= 4:
            word = random.choice(words)
        else:
            return word.upper()

    elif data == 'm':
        while len(word) < 5 or len(word) >= 6:
            word = random.choice(words)
        else:
            return word.upper()
        
    elif data == 'h':
        while len(word) <= 6:
            word = random.choice(words)
        else:
            return word.upper()


def game_structure(data):

    error_counter = 0
    used_letters = []

    hangman_design(error_counter)

    hidden_word = '_' * len(word)

    while error_counter < 6:
        print(hidden_word)
        print(f'You have made {error_counter} mistakes.')

        guess = input('Guess a letter:').upper()

        if guess.isalpha() and len(guess) == 1:
            if guess in used_letters:
                hangman_design(error_counter)
                print(f'Sorry, {guess} has already been used. Please try again.')
            elif guess in word:
                used_letters.append(guess)
                hangman_design(error_counter)
                print(f'Used letters: {used_letters}', end='\n')
                print(guess, end=" ")
                print('Good guess. Try another letter: ')
                guess = input('Guess a letter: ').upper()
            else:
                used_letters.append(guess)
                print(f'Used letters: {used_letters}', end='\n')
                error_counter += 1
                hangman_design(error_counter)
                print('_', end=' ')
                print('\n')
                print('Sorry, wrong letter. Try another one: ')
                guess = input('Guess a letter: ').upper()


    for letter in data:
        print('_', end=' ')
        if guess == letter:
            used_letters.append(guess)
            hangman_design(error_counter)
            print(used_letters, end='\n')
            print(guess, end=" ")
            print('Good guess. Try another letter: ')
            guess = input('Guess a letter: ').upper()
        else:
            used_letters.append(guess)
            print(used_letters, end='\n')
            error_counter += 1
            hangman_design(error_counter)
            print('_', end=' ')
            print('\n')
            print('Sorry, wrong letter. Try another one: ')
            guess = input('Guess a letter: ').upper()
    
    while error_counter < 6:
        if guess.isalpha() == True:
            game_structure(data)
        else:
            print(f'Sorry, {guess} is not a valid answer. Please try again.')    

def hangman_design(data):
    """
    Structure for the design of the hangman.
    Based on the amount of errors of the user, the design change.
    """
    if data == 0:
        print('    ______    ')
        print('    |    |    ')
        print('         |    ')
        print('         |    ')
        print('         |    ')
        print('         |    ')
        print('       *****  ')
    
    elif data == 1:
        print('    ______    ')
        print('    |    |    ')
        print('    O    |    ')
        print('         |    ')
        print('         |    ')
        print('         |    ')
        print('       *****  ')
    
    elif data == 2:
        print('    ______    ')
        print('    |    |    ')
        print('    O    |    ')
        print('    |    |    ')
        print('         |    ')
        print('         |    ')
        print('       *****  ')
        
    elif data == 3:
        print('    ______    ')
        print('    |    |    ')
        print('    O    |    ')
        print('   /|    |    ')
        print('         |    ')
        print('         |    ')
        print('       *****  ')

    elif data == 4:
        print('    ______    ')
        print('    |    |    ')
        print('    O    |    ')
        print('   /|\   |    ')
        print('         |    ')
        print('         |    ')
        print('       *****  ')

    elif data == 5:
        print('    ______    ')
        print('    |    |    ')
        print('    O    |    ')
        print('   /|\   |    ')
        print('   /     |    ')
        print('         |    ')
        print('       *****  ')

    elif data == 6:
        print('    ______    ')
        print('    |    |    ')
        print('    O    |    ')
        print('   /|\   |    ')
        print('   / \   |    ')
        print('         |    ')
        print('       *****  ')

main_screen()