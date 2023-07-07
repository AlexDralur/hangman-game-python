import random
import os
from words import words


def main_screen():
    """
    First screen of the game.
    Allows user to start the game.
    """

    os.system('clear')

    print("""
  _____ _            _   _
 |_   _| |__   ___  | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __
   | | | '_ \ / _ \ | |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \`
   | | | | | |  __/ |  _  | (_| | | | | (_| | | | | | | (_| | | | |
   |_| |_| |_|\___| |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                                       |___/                       """)
    hangman_design(6)
    print('WELCOME TO THE HANGMAN')
    print('\n')
    print('Type "P" to Play.')
    print('Type "R" to view the rules.')
    play = input('Type "Q" to leave the game.').upper()
    start_game(play)


def start_game(data):
    """Function to check if the user has
    pressed the correct key to start the game."""

    while data != 'P' and data != 'Q' and data != "R":
        print(f'Sorry, {data} is not a valid answer.')
        print('Type "P" to Play, "R" for Rules or "Q" to leave the game.')
        data = input('Try again: ').upper()
        start_game(data)

    if data == 'P':
        print('\n')
        print('Choose one of the following letters for the difficulty:')
        difficulty = input(
        '"E" for easy, "M" for medium or "H" for hard: ')
        change_difficulty(difficulty)

    elif data == "Q":
        exit()

    elif data == "R":
        rules()


def change_difficulty(data):
    """Check which level of difficulty the user has
    chosen and if it is one of the correct keys"""

    if data.upper() == 'E':
        random_word = choose_word('e')
        game_structure(random_word)

    elif data.upper() == 'M':
        random_word = choose_word('m')
        game_structure(random_word)

    elif data.upper() == 'H':
        random_word = choose_word('h')
        game_structure(random_word)

    elif data.upper() == "Q":
        exit()

    else:

        if data.isalpha() is False:
            repeat = input(f'Sorry, {data} is not a letter. Try again: ')
            change_difficulty(repeat)

        else:
            repeat = input(f'Sorry, {data} is not a valid letter. Try again: ')
            change_difficulty(repeat)


def choose_word(data):
    """Once the user chooses the difficult, the function runs and
    retrieves one random word based on the user’s choice"""

    word = random.choice(words)
    acceptable_words = []

    if data == 'e':

        for word in words:

            if len(word) <= 4:
                acceptable_words.append(word)

        return random.choice(acceptable_words).upper()

    elif data == 'm':

        for word in words:

            if len(word) == 5:
                acceptable_words.append(word)

        return random.choice(acceptable_words).upper()

    elif data == 'h':

        for word in words:

            if len(word) >= 6:
                acceptable_words.append(word)

        return random.choice(acceptable_words).upper()


def game_structure(data):
    """Main function that makes the game run.
    While the game is not won or finished, it requests an answer
    from the user and prints the relevant information."""

    os.system('clear')
    error_counter = 0
    used_letters = []
    hidden_word = '_' * len(data)
    hangman_design(error_counter)

    while error_counter < 6:
        print(hidden_word)
        guess = input('Guess a letter: ').upper()

        if guess.isalpha() and len(guess) == 1:

            if guess in used_letters:
                print(f'Used letters: {used_letters}', end='\n')
                print(f'Sorry, {guess} has already been used. Try again.')
                hangman_design(error_counter)
                print('\n')

            elif guess in data:
                used_letters.append(guess)
                word_as_list = list(hidden_word)
                ind = [i for i, letter in enumerate(data) if letter == guess]

                for index in ind:
                    word_as_list[index] = guess
                hidden_word = "".join(word_as_list)

                if hidden_word == data:
                    endgame('won', data)

                print(f'Used letters: {used_letters}', end='\n')
                print('Good guess. Try again.')
                hangman_design(error_counter)
                print('\n')

            else:
                used_letters.append(guess)
                error_counter += 1
                print(f'Used letters: {used_letters}', end='\n')

                if error_counter == 1:
                    print(f'You have made {error_counter} mistake.')

                else:
                    print(f'You have made {error_counter} mistakes.')

                if error_counter < 6:
                    hangman_design(error_counter)

                print('\n')

        elif len(guess) < 1:
            print(f'Used letters: {used_letters}', end='\n')
            print('No letter identified. Please, try again.')
            hangman_design(error_counter)
            print('\n')

        elif guess == "EXIT":
            exit()

        elif len(guess) > 1 and guess.isalpha() is True:
            print(f'Used letters: {used_letters}', end='\n')
            print('Guess one letter at a time. Try again.')
            hangman_design(error_counter)
            print('\n')

        else:
            print(f'Used letters: {used_letters}', end='\n')
            print(f'Sorry, {guess} is not a valid answer. Please try again.')
            hangman_design(error_counter)
            print('\n')

    if error_counter == 6:
        endgame('lose', data)


def endgame(data, word):
    """once the user gets the word right or runs out of chances,
    the function is called. It can provide a congratulations or
    a game over message and asks if the user would like to play again."""

    if data == "lose":
        print("""
           ____                         ___
          / ___| __ _ _ __ ___   ___   / _ \__   _____ _ __
         | |  _ / _` | '_ ` _ \ / _ \ | | | \ \ / / _ \ '__|
         | |_| | (_| | | | | | |  __/ | |_| |\ V /  __/ |
          \____|\__,_|_| |_| |_|\___|  \___/  \_/ \___|_|
                                                    """)
        hangman_design(6)
        print(f'Sorry, you ran out of tries. The word was {word}.')

    elif data == "won":
        print("""
   ____ ___  _   _  ____ ____      _  _____ ____  _
  / ___/ _ \| \ | |/ ___|  _ \    / \|_   _/ ___|| |
 | |  | | | |  \| | |  _| |_) |  / _ \ | | \___ \| |
 | |__| |_| | |\  | |_| |  _ <  / ___ \| |  ___) |_|
  \____\___/|_| \_|\____|_| \_\/_/   \_\_| |____/(_)
                                                    """)
        print(f'Congratulations, you guessed "{word}".')

    restart_game()


def restart_game():
    """Function that restarts the game"""

    replay = ''

    while replay is not 'P' and replay is not 'Q':
        replay = input(
            'Type "P" to play it again or "Q" to leave: ').upper()

        if replay == 'P':
            os.system('clear')
            main_screen()

        elif replay == 'Q':
            exit()

        else:
            print('Sorry, that is not a validate input.')


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
    """Set of instructions to be print out once the game starts."""

    print('\n')
    print('These are the rules of the game:')
    print('1. You can only chose one letter each time.')
    print('2. You cannot guess the whole word at once.')
    print('3. You can make five wrong guesses.')
    print('4. If you the whole doll is hanging, you lost the game.')
    print('5. You can type "QUIT" at any time to quit the game.')
    print('6. Good luck!')
    input('Press any key to return to the main screen')
    main_screen()


main_screen()

