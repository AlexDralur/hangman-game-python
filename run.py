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
    print('Would you like to play? Press Y')
    print('Change difficult? Press D')
    first_option = input('Choose your option: ')
    check_answer(first_option)

def check_answer(data):
    if data.lower() == 'y' or data.lower() == 'd':
        print('correct')
    else:
        print(f'Sorry, {data} is not a valid anwer. Please try again.')

main_screen()