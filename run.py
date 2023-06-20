# Write your code to expect a terminal of 80 characters wide and 24 rows high
import random

#words source: https://github.com/Xethron/Hangman
words = ['able', 'about', 'account', 'acid', 'across', 'act', 'addition', 'adjustment', 'advertisement', 'after', 'again', 'against', 'agreement', 'air', 'all', 'almost', 'among', 'amount', 'amusement', 'and', 'angle', 'angry', 'animal', 'answer', 'ant', 'any', 'apparatus', 'apple', 'approval', 'arch', 'argument', 'arm', 'army', 'art', 'as', 'at', 'attack', 'attempt', 'attention', 'attraction', 'authority', 'automatic', 'awake', 'baby', 'back', 'bad', 'bag', 'balance', 'ball', 'band', 'base', 'basin', 'basket', 'bath', 'be', 'beautiful', 'because', 'bed', 'bee', 'before', 'behaviour', 'belief', 'bell', 'bent', 'berry', 'between', 'bird', 'birth', 'bit', 'bite', 'bitter', 'black', 'blade', 'blood', 'blow', 'blue', 'board', 'boat', 'body', 'boiling', 'bone', 'book', 'boot', 'bottle', 'box', 'boy', 'brain', 'brake', 'branch', 'brass', 'bread', 'breath', 'brick', 'bridge', 'bright', 'broken', 'brother', 'brown', 'brush', 'bucket', 'building', 'bulb', 'burn', 'burst', 'business', 'but', 'butter', 'button', 'by', 'cake', 'camera', 'canvas', 'card', 'care', 'carriage', 'cart', 'cat', 'cause', 'certain', 'chain', 'chalk', 'chance', 'change', 'cheap', 'cheese', 'chemical', 'chest', 'chief', 'chin', 'church', 'circle', 'clean', 'clear', 'clock', 'cloth', 'cloud', 'coal', 'coat', 'cold', 'collar', 'colour', 'comb', 'come', 'comfort', 'committee', 'common', 'company', 'comparison', 'competition', 'complete', 'complex', 'condition', 'connection', 'conscious', 'control', 'cook', 'copper', 'copy', 'cord', 'cork', 'cotton', 'cough', 'country', 'cover', 'cow', 'crack', 'credit', 'crime', 'cruel', 'crush', 'cry', 'cup', 'cup', 'current', 'curtain', 'curve', 'cushion', 'damage', 'danger', 'dark', 'daughter', 'day', 'dead', 'dear', 'death', 'debt', 'decision', 'deep', 'degree', 'delicate', 'dependent', 'design', 'desire', 'destruction', 'detail', 'development', 'different', 'digestion', 'direction', 'dirty', 'discovery', 'discussion', 'disease', 'disgust', 'distance', 'distribution', 'division', 'do', 'dog', 'door', 'doubt', 'down', 'drain', 'drawer', 'dress', 'drink', 'driving', 'drop', 'dry', 'dust', 'ear', 'early', 'earth', 'east', 'edge', 'education', 'effect', 'egg', 'elastic', 'electric', 'end', 'engine', 'enough', 'equal', 'error', 'even', 'event', 'ever', 'every', 'example', 'exchange', 'existence', 'expansion', 'experience', 'expert', 'eye', 'face', 'fact', 'fall', 'false', 'family', 'far', 'farm', 'fat', 'father', 'fear', 'feather', 'feeble', 'feeling', 'female', 'fertile', 'fiction', 'field', 'fight', 'finger', 'fire', 'first', 'fish', 'fixed', 'flag', 'flame', 'flat', 'flight', 'floor', 'flower', 'fly', 'fold', 'food', 'foolish', 'foot', 'for', 'force', 'fork', 'form', 'forward', 'fowl', 'frame', 'free', 'frequent', 'friend', 'from', 'front', 'fruit', 'full', 'future', 'garden', 'general', 'get', 'girl', 'give', 'glass', 'glove', 'go', 'goat', 'gold', 'good', 'government', 'grain', 'grass', 'great', 'green', 'grey', 'grip', 'group', 'growth', 'guide', 'gun', 'hair', 'hammer', 'hand', 'hanging', 'happy', 'harbour', 'hard', 'harmony', 'hat', 'hate', 'have', 'he', 'head', 'healthy', 'hear', 'hearing', 'heart', 'heat', 'help', 'high', 'history', 'hole', 'hollow', 'hook', 'hope', 'horn', 'horse', 'hospital', 'hour', 'house', 'how', 'humour', 'I', 'ice', 'idea', 'if', 'ill', 'important', 'impulse', 'in', 'increase', 'industry', 'ink', 'insect', 'instrument', 'insurance', 'interest', 'invention', 'iron', 'island', 'jelly', 'jewel', 'join', 'journey', 'judge', 'jump', 'keep', 'kettle', 'key', 'kick', 'kind', 'kiss', 'knee', 'knife', 'knot', 'knowledge', 'land', 'language', 'last', 'late', 'laugh', 'law', 'lead', 'leaf', 'learning', 'leather', 'left', 'leg', 'let', 'letter', 'level', 'library', 'lift', 'light', 'like', 'limit', 'line', 'linen', 'lip', 'liquid', 'list', 'little', 'living', 'lock', 'long', 'look', 'loose', 'loss', 'loud', 'love', 'low', 'machine', 'make', 'male', 'man', 'manager', 'map', 'mark', 'market', 'married', 'mass', 'match', 'material', 'may', 'meal', 'measure', 'meat', 'medical', 'meeting', 'memory', 'metal', 'middle', 'military', 'milk', 'mind', 'mine', 'minute', 'mist', 'mixed', 'money', 'monkey', 'month', 'moon', 'morning', 'mother', 'motion', 'mountain', 'mouth', 'move', 'much', 'muscle', 'music', 'nail', 'name', 'narrow', 'nation', 'natural', 'near', 'necessary', 'neck', 'need', 'needle', 'nerve', 'net', 'new', 'news', 'night', 'no', 'noise', 'normal', 'north', 'nose', 'not', 'note', 'now', 'number', 'nut', 'observation', 'of', 'off', 'offer', 'office', 'oil', 'old', 'on', 'only', 'open', 'operation', 'opinion', 'opposite', 'or', 'orange', 'order', 'organization', 'ornament', 'other', 'out', 'oven', 'over', 'owner', 'page', 'pain', 'paint', 'paper', 'parallel', 'parcel', 'part', 'past', 'paste', 'payment', 'peace', 'pen', 'pencil', 'person', 'physical', 'picture', 'pig', 'pin', 'pipe', 'place', 'plane', 'plant', 'plate', 'play', 'please', 'pleasure', 'plough', 'pocket', 'point', 'poison', 'polish', 'political', 'poor', 'porter', 'position', 'possible', 'pot', 'potato', 'powder', 'power', 'present', 'price', 'print', 'prison', 'private', 'probable', 'process', 'produce', 'profit', 'property', 'prose', 'protest', 'public', 'pull', 'pump', 'punishment', 'purpose', 'push', 'put', 'quality', 'question', 'quick', 'quiet', 'quite', 'rail', 'rain', 'range', 'rat', 'rate', 'ray', 'reaction', 'reading', 'ready', 'reason', 'receipt', 'record', 'red', 'regret', 'regular', 'relation', 'religion', 'representative', 'request', 'respect', 'responsible', 'rest', 'reward', 'rhythm', 'rice', 'right', 'ring', 'river', 'road', 'rod', 'roll', 'roof', 'room', 'root', 'rough', 'round', 'rub', 'rule', 'run', 'sad', 'safe', 'sail', 'salt', 'same', 'sand', 'say', 'scale', 'school', 'science', 'scissors', 'screw', 'sea', 'seat', 'second', 'secret', 'secretary', 'see', 'seed', 'seem', 'selection', 'self', 'send', 'sense', 'separate', 'serious', 'servant', 'sex', 'shade', 'shake', 'shame', 'sharp', 'sheep', 'shelf', 'ship', 'shirt', 'shock', 'shoe', 'short', 'shut', 'side', 'sign', 'silk', 'silver', 'simple', 'sister', 'size', 'skin', '', 'skirt', 'sky', 'sleep', 'slip', 'slope', 'slow', 'small', 'smash', 'smell', 'smile', 'smoke', 'smooth', 'snake', 'sneeze', 'snow', 'so', 'soap', 'society', 'sock', 'soft', 'solid', 'some', '', 'son', 'song', 'sort', 'sound', 'soup', 'south', 'space', 'spade', 'special', 'sponge', 'spoon', 'spring', 'square', 'stage', 'stamp', 'star', 'start', 'statement', 'station', 'steam', 'steel', 'stem', 'step', 'stick', 'sticky', 'stiff', 'still', 'stitch', 'stocking', 'stomach', 'stone', 'stop', 'store', 'story', 'straight', 'strange', 'street', 'stretch', 'strong', 'structure', 'substance', 'such', 'sudden', 'sugar', 'suggestion', 'summer', 'sun', 'support', 'surprise', 'sweet', 'swim', 'system', 'table', 'tail', 'take', 'talk', 'tall', 'taste', 'tax', 'teaching', 'tendency', 'test', 'than', 'that', 'the', 'then', 'theory', 'there', 'thick', 'thin', 'thing', 'this', 'thought', 'thread', 'throat', 'through', 'through', 'thumb', 'thunder', 'ticket', 'tight', 'till', 'time', 'tin', 'tired', 'to', 'toe', 'together', 'tomorrow', 'tongue', 'tooth', 'top', 'touch', 'town', 'trade', 'train', 'transport', 'tray', 'tree', 'trick', 'trouble', 'trousers', 'true', 'turn', 'twist', 'umbrella', 'under', 'unit', 'up', 'use', 'value', 'verse', 'very', 'vessel', 'view', 'violent', 'voice', 'waiting', 'walk', 'wall', 'war', 'warm', 'wash', 'waste', 'watch', 'water', 'wave', 'wax', 'way', 'weather', 'week', 'weight', 'well', 'west', 'wet', 'wheel', 'when', 'where', 'while', 'whip', 'whistle', 'white', 'who', 'why', 'wide', 'will', 'wind', 'window', 'wine', 'wing', 'winter', 'wire', 'wise', 'with', 'woman', 'wood', 'wool', 'word', 'work', 'worm', 'wound', 'writing', 'wrong', 'year', 'yellow', 'yes', 'yesterday', 'you', 'young', 'Bernhard', 'Breytenbach', 'Android']

error_counter = 0


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

    hangman_design()
    guess = input('Guess a letter: ').upper()

    for letter in data:
        print('_', end=' ')
        if guess == letter:
            used_letters.append(guess)
            hangman_design()
            print(used_letters, end='\n')
            print(guess, end=" ")
            print('Good guess. Try another letter: ')
            guess = input('Guess a letter: ').upper()
        else:
            used_letters.append(guess)
            print(used_letters, end='\n')
            error_counter += 1
            hangman_design()
            print('_', end=' ')
            print('\n')
            print('Sorry, wrong letter. Try another one: ')
            guess = input('Guess a letter: ').upper()
    
    while error_counter < 6:
        if guess.isalpha() == True:
            game_structure(data)
        else:
            print(f'Sorry, {guess} is not a valid answer. Please try again.')    

main_screen()