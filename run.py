# Write your code to expect a terminal of 80 characters wide and 24 rows high

def hangman_design():
    """
    Structure for the design of the hangman.
    Based on the amount of errors of the user, the design change.
    """
    if error_counter == 0:
        print('    ______    ')
        print('    |    |    ')
        print('         |    ')
        print('         |    ')
        print('         |    ')
        print('         |    ')
        print('       *****  ')
    
    elif error_counter == 1:
        print('    ______    ')
        print('    |    |    ')
        print('    O    |    ')
        print('         |    ')
        print('         |    ')
        print('         |    ')
        print('       *****  ')
    
    elif error_counter == 2:
        print('    ______    ')
        print('    |    |    ')
        print('    O    |    ')
        print('    |    |    ')
        print('         |    ')
        print('         |    ')
        print('       *****  ')
        
    elif error_counter == 3:
        print('    ______    ')
        print('    |    |    ')
        print('    O    |    ')
        print('   /|    |    ')
        print('         |    ')
        print('         |    ')
        print('       *****  ')

    elif error_counter == 4:
        print('    ______    ')
        print('    |    |    ')
        print('    O    |    ')
        print('   /|\   |    ')
        print('         |    ')
        print('         |    ')
        print('       *****  ')

    elif error_counter == 5:
        print('    ______    ')
        print('    |    |    ')
        print('    O    |    ')
        print('   /|\   |    ')
        print('   /     |    ')
        print('         |    ')
        print('       *****  ')

    elif error_counter == 6:
        print('    ______    ')
        print('    |    |    ')
        print('    O    |    ')
        print('   /|\   |    ')
        print('   / \   |    ')
        print('         |    ')
        print('       *****  ')


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
        
        elif data.lower() == 'm':
            print('You chose the difficult: medium.')

        elif data.lower() == 'h':
            print('You chose the difficult: hard.')

        else:
            print(f'Sorry, {data} is not a valid answer. Please try again.')

main_screen()