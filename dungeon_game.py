import random
import os
'''
CELLS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
         (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
         (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
         (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
         (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_locations():
    return random.sample(CELLS, 3)

def move_player(player, move):
    x, y = player
    if move == 'LEFT':
        x -= 1
    if move == 'RIGHT':
        x += 1
    if move == 'UP':
        y -= 1
    if move == 'DOWN':
        y += 1

    return x, y

def get_moves(player):
    moves = ['UP', 'RIGHT', 'DOWN', 'LEFT']
    x, y = player
    if x == 0:
        moves.remove('LEFT')
    if x == 4:
        moves.remove('RIGHT')
    if y == 0:
        moves.remove('UP')
    if y == 4:
        moves.remove('DOWN')

    return moves

def game_loop():
    monster, door, player = get_locations() 
    
    while True:
        valid_moves = get_moves(player)
        clear_screen()
        print('Welcome to the Dungeon!')
        input('Press ENTER to start!')
        clear_screen()
        game_loop()

    print('You\'re currently in room {}.'.format(player))
    print('You can move {}.'.format(', '.join(valid_moves)))
    print('Enter QUIT to quit.')

    move = input('> ').upper()

    if move == 'QUIT':
        break 
    if move in valid_moves:
        player = move_player(player, move)
    else:
        print('\n** Invalid move. There is a wall there!\n **')
        continue
'''
CELLS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
         (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
         (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
         (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
         (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)
]

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def get_locations():
    return random.sample(CELLS, 3)

def move_player(player, move):
    # Get the player's location.
    x, y = player

    if move == 'LEFT': # If move == LEFT, x-1
        x -= 1
    if move == 'RIGHT': # If move == RIGHT, x+1
        x += 1
    if move == 'UP': # If move == UP, y-1
        y -= 1
    if move == 'DOWN': # If move == DOWN, y+1
        y += 1     
       
    return x, y

# Function that gives us a list of moves.
def get_moves(player):
    moves = ['UP', 'RIGHT', 'DOWN', 'LEFT']
    x, y = player # Unpacking the player tuple. 
 
    if x == 0:
       moves.remove('LEFT') # If player's x == 0, they can't move left.
    if x == 4:
        moves.remove('RIGHT') # If player's x == 4, they can't move right.
    if y == 0:
        moves.remove('UP') # If player's y == 0, they can't move up.
    if y == 4:
        moves.remove('DOWN')# If player's y == 4, they can't move down.

    return moves

monster, door, player = get_locations()    

while True:
    valid_moves = get_moves(player)
    clear_screen()
    print('Welcome to the dungeon!')
    print('You\'re currently in room {}.'.format(player))
    print('You can move {}.'.format(', '.join(valid_moves)))
    print('Enter QUIT to quit.')

    move = input('> ').upper()

    if move == 'QUIT':
       break  
    if move in valid_moves:
        player = move_player(player, move)
    else:
        print('Invalid move: There is a wall there.')
        continue
