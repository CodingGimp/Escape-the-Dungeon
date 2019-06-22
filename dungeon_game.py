import random

CELLS = [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0),
         (0, 1), (1, 1), (2, 1), (3, 1), (4, 1),
         (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
         (0, 3), (1, 3), (2, 3), (3, 3), (4, 3),
         (0, 4), (1, 4), (2, 4), (3, 4), (4, 4)
]

def get_locations():
    monster = None
    door = None
    player = None

    return monster, door, player

def move_player(player, move):
    return player

def get_moves(player):
    moves = ['UP', 'RIGHT', 'DOWN', 'LEFT']



while True:
    print('Welcome to the Dungeon!')
    print('You\'re currently in room {}.')
    print('You can move {}.')
    print('Enter QUIT to quit.')

    move = input('> ').upper()

    if move == 'QUIT':
        break 
    