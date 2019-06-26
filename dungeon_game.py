import random
import os

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

def draw_map(player):
    print(' _' * 5)
    tile = "|{}"

    for cell in CELLS:
        x, y = cell
        if x < 4:
            line_end = ''
            if cell == player:
                output = tile.format('X')
            else:
                output = tile.format('_')
        else:
            line_end = '\n'    
            if cell == player:
                output = tile.format('X|')
            else:
                output = tile.format('_|')
        print(output, end=line_end)

def game_loop(): 
    monster, door, player = get_locations()
    playing = True

    while playing:  
        clear_screen()
        draw_map(player)
        valid_moves = get_moves(player)

        print('You\'re currently in room {}.'.format(player))
        print('You can move {}.'.format(', '.join(valid_moves)))
        print('Enter QUIT to quit.')

        move = input('> ').upper()

        if move == 'QUIT':
            break  
        if move in valid_moves:
            player = move_player(player, move)

            if player == monster:
                print('\n*** The monster got you. Sorry, you lose...***\n')
                playing = False

            if player == door:
                print('\n*** Congratulations! You found the door and escape the dungeon...YOU WIN!!!***')
                playing = False     
        else:
            input('Invalid move: There is a wall there.')
    else:
        if input('Would you like to play again? [Yes/No] ').upper() != 'NO':
            game_loop()

clear_screen()
print('Welcome to the dungeon!')
input('Press ENTER to start!')
clear_screen
game_loop()

    
