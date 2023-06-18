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
    print("""
           ________            __  __                                      
 /_  __/ /_  ___     / / / /___ _____  ____ _____ ___  ____ _____ 
  / / / __ \/ _ \   / /_/ / __ `/ __ \/ __ `/ __ `__ \/ __ `/ __ \
 / / / / / /  __/  / __  / /_/ / / / / /_/ / / / / / / /_/ / / / /
/_/ /_/ /_/\___/  /_/ /_/\__,_/_/ /_/\__, /_/ /_/ /_/\__,_/_/ /_/ 
                                    /____/                        
          """)

main_screen()