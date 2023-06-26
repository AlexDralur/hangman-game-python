import random
from words import words

#words source: https://github.com/Xethron/Hangman

def main_screen():
    """
    First screen of the game. 
    Allows user to start the game.
    """

    print("""
  _____ _            _   _                                         
 |_   _| |__   ___  | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __  
   | | | '_ \ / _ \ | |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
   | | | | | |  __/ |  _  | (_| | | | | (_| | | | | | | (_| | | | |
   |_| |_| |_|\___| |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                       |___/                       """)
    hangman_design(6)
    print ('WELCOME TO THE HANGMAN')
    play = input('Would you like to play? Press 1')
    check_answer(play)

def check_answer(data):
    """Function to check if the user has 
    pressed the correct key to start the game."""

    try:
        answer = int(data)
        
        if answer == 1:
            difficulty = input('Please type "E" for easy, "M" for medium or "H" for hard.')
            change_difficulty(difficulty)

    except ValueError:
        second_try = input(f'{data} is not a number, please try again.')
        check_answer(second_try)

    else:
        second_try = input(f'Sorry, {data} is not a valid answer. Please try again.')
        check_answer(second_try)

def change_difficulty(data):
    """Check which level of difficulty the user has 
    chosen and if it is one of the correct keys"""
    
    try:
        option = data.isalpha()

    except TypeError:
        print(f'{data} is not a valid option, please try again.')

    else:
        if data.lower() == 'e':
            print('You chose the difficult: easy.')
            rules()
            random_word = choose_word('e')
            game_structure(random_word)
        
        elif data.lower() == 'm':
            print('You chose the difficult: medium.')
            rules()
            random_word = choose_word('m')
            game_structure(random_word)

        elif data.lower() == 'h':
            print('You chose the difficult: hard.')
            rules()
            random_word = choose_word('h')
            game_structure(random_word)

        else:
            difficulty_second = input(f'Sorry, {data} is not a valid answer. Please try again: ')
            change_difficulty(difficulty_second)


def choose_word(data):
    """Once the user chooses the difficult, the function runs and 
    retrieves one random word based on the user’s choice"""

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
    hidden_word = '_' * len(data)
    hangman_design(error_counter)
    print(hidden_word)
    guess = input('Guess a letter: ').upper()


    while error_counter < 6:

        if guess.isalpha() and len(guess) == 1:
            if guess in used_letters:
                print(f'Sorry, {guess} has already been used. Please try again.')
                print(f'Used letters: {used_letters}', end='\n')
                hangman_design(error_counter)
                print(hidden_word, end=" ")
                print('\n')
                guess = input('Guess a letter: ').upper()
            elif guess in data:
                used_letters.append(guess)
                word_as_list = list(hidden_word)
                indices = [i for i, letter in enumerate(data) if letter == guess]
                for index in indices:
                    word_as_list[index] = guess
                hidden_word = "".join(word_as_list)
                if hidden_word == data:
                    endgame('won', data)
                print(f'Used letters: {used_letters}', end='\n')
                hangman_design(error_counter)
                print(hidden_word, end=" ")
                print('\n')
                guess = input('Good guess. Try another letter: ').upper()
            else:                
                used_letters.append(guess)
                error_counter += 1
                print(f'Used letters: {used_letters}', end='\n')
                hangman_design(error_counter)
                print(hidden_word, end=" ")
                print('\n')
                if error_counter == 1:
                    print(f'You have made {error_counter} mistake.')
                else:
                    print(f'You have made {error_counter} mistakes.')
                guess = input('Try again. Guess a letter: ').upper()
        elif len(guess) < 1:
            print(f'Used letters: {used_letters}', end='\n')
            hangman_design(error_counter)
            print(hidden_word, end=" ")
            print('\n')
            guess = input('No letter identified. Please, guess a letter: ').upper()
        elif len(guess) > 1:
            print(f'Used letters: {used_letters}', end='\n')
            hangman_design(error_counter)
            print(hidden_word, end=" ")
            print('\n')
            guess = input('Please, guess only one letter at a time. Please, guess a letter: ').upper()
        else:
            print(f'Used letters: {used_letters}', end='\n')
            hangman_design(error_counter)
            print(hidden_word, end=" ")
            print('\n')
            print(f'Sorry, {guess} is not a valid answer. Please try again.')
            guess = input('Guess a letter: ').upper()
        
    if error_counter == 6:
        endgame('lose', data)

def endgame(data, word):

    if data == "lose":
        print("""
           ____                         ___                 
          / ___| __ _ _ __ ___   ___   / _ \__   _____ _ __ 
         | |  _ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__|
         | |_| | (_| | | | | | |  __/ | |_| |\ V /  __/ |   
          \____|\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|   
                                                    """)
        hangman_design(6)
        replay = input(f'Sorry, you ran out of tries. The word was {word} Press Y to play again.').upper()
        
        if replay == 'Y':
            main_screen()
        else:
            while replay != 'Y':
                replay = input('Sorry, that is not a validate input. Press Y to play it again.').upper()
                if replay == "Y":
                    main_screen()

    elif data == "won":
        print("""
           ____                            _         _       _   _                 _ 
          / ___|___  _ __   __ _ _ __ __ _| |_ _   _| | __ _| |_(_) ___  _ __  ___| |
         | |   / _ \| '_ \ / _` | '__/ _` | __| | | | |/ _` | __| |/ _ \| '_ \/ __| |
         | |__| (_) | | | | (_| | | | (_| | |_| |_| | | (_| | |_| | (_) | | | \__ \_|
          \____\___/|_| |_|\__, |_|  \__,_|\__|\__,_|_|\__,_|\__|_|\___/|_| |_|___(_)
                           |___/                                                     """)
        replay = input(f'Congratulations, you guessed "{word}". Press Y to play again.').upper()
    
        if replay == 'Y':
            main_screen()
        else:
            while replay != 'Y':
                replay = input('Sorry, that is not a validate input. Press Y to play it again.').upper()
                if replay == "Y":
                    main_screen()

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

def rules():
    print('These are the rules of the game:')
    print('1. You can only chose one letter each time.')
    print('2. You cannot guess the whole word at once.')
    print('3. You can make five wrong guesses.')
    print('4. If you the whole doll is hanging, you lost the game.')
    print('5. Good luck!')
main_screen()