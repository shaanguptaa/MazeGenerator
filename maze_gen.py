import pygame
from maze import Maze
from player import Player
from random import choice

# init pygame and create a window
pygame.init()

WINDOW = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Maze Generator")
WINDOW.fill((0, 0, 0))

clock = pygame.time.Clock()
FRAMERATE = 15

MAZE = Maze()
PLAYER = Player(MAZE.get_start_tile())
PATH = []

moves = []

def next_move():
    global moves
    
    avail_moves = MAZE.get_moves_for_tile(PLAYER.row, PLAYER.col)

    if avail_moves:
        pref_move = choice(avail_moves)
        moves.append(((PLAYER.row, PLAYER.col), pref_move))
        MAZE.move(PLAYER, pref_move)
    else:
        # move back 1 step
        new_pos, played_move = moves.pop()
        MAZE.move_back(PLAYER, played_move)

def finalize():
    global moves
    
    avail_moves = MAZE.get_moves_for_tile(PLAYER.row, PLAYER.col, False)
    
    if avail_moves:
        pref_move = choice(avail_moves)
        MAZE.move(PLAYER, pref_move)
    else:
        # move to next step in path(moves[])
        pos, played_move = moves.pop(0)
        PLAYER.set_player_to_tile(MAZE.get_tile(pos[0], pos[1]))

def finalize_v2():
    
    avail_moves = MAZE.get_moves_for_tile(PLAYER.row, PLAYER.col, False)
    if avail_moves:
        pref_move = choice(avail_moves)
        MAZE.move(PLAYER, pref_move)
        # print(pref_move)
    else:
        # move to a random step in path avoiding maze bounds
        avail_moves = []
        if PLAYER.row > 0:
            avail_moves.append('top')
        if PLAYER.row < MAZE.size[1] - 1:
            avail_moves.append('bottom')
        if PLAYER.col > 0:
            avail_moves.append('left')
        if PLAYER.col < MAZE.size[0] - 1:
            avail_moves.append('right')

        pref_move = choice(avail_moves)
        MAZE.move(PLAYER, pref_move)
        # start at the next unvisited tile
        try:
            PLAYER.set_player_to_tile(MAZE.get_unvisited_tile())
            MAZE.tiles[PLAYER.row][PLAYER.col].visited = True
        except Exception as e:
            # no unvisited tiles left
            global finalizing_v2
            finalizing_v2 = False


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            exit()
    
    MAZE.show_maze(WINDOW)
    PLAYER.draw(WINDOW)
    
    pygame.display.update()
    clock.tick(FRAMERATE)
    
    if not MAZE.reached_finish(PLAYER):
        next_move()
    else:
        print('Path done')
        running = False


print('Generating fake paths')
pos, played_move = moves.pop(0)    # Starting with the start tile
PLAYER.set_player_to_tile(MAZE.get_tile(pos[0], pos[1]))

finalizing = True
while finalizing:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finalizing = False
            pygame.quit()
            exit()
    
    MAZE.show_maze(WINDOW)
    PLAYER.draw(WINDOW)
    
    pygame.display.update()
    clock.tick(FRAMERATE)
    
    if not MAZE.reached_finish(PLAYER) and moves:
        finalize()
    else:
        finalizing = False


print("Finalizing remaining unvisited tiles")
finalizing_v2 = True

try:
    PLAYER.set_player_to_tile(MAZE.get_unvisited_tile())
    MAZE.tiles[PLAYER.row][PLAYER.col].visited = True
except Exception as e:
    # no unvisited tiles left
    finalizing_v2 = False

while finalizing_v2:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finalizing_v2 = False
            pygame.quit()
            exit()
    
    MAZE.show_maze(WINDOW)
    PLAYER.draw(WINDOW)
    
    pygame.display.update()
    clock.tick(FRAMERATE)
    
    finalize_v2()

print('completed')

PLAYER.set_player_to_tile(MAZE.get_start_tile())

WINDOW.fill((0, 255, 0))
MAZE.show_maze(WINDOW)
PLAYER.draw(WINDOW)
pygame.display.update()

# save screenshot of maze
print('Saving image of maze')
pygame.image.save(WINDOW, 'MazeGenerator/maze.png')

# export maze to json
print('Exporting maze to json')
MAZE.export_to_json('MazeGenerator/maze.json')

print('Completed \nClose the window to exit')

# wait for user to close window
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    MAZE.show_maze(WINDOW)
    PLAYER.draw(WINDOW)
    
    pygame.display.update()
    clock.tick(FRAMERATE)