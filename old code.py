# class Tile(pygame.sprite.Sprite):
#     def __init__(self, row, col, size):
#         super().__init__()
#         self.visited = False
#         self.top = self.bottom = self.left = self.right = True
#         self.row = row
#         self.col = col
#         self.size = size
#         self.rect = pygame.Rect(row, col, size, size)

#     def show_tile(self):
#         if self.top:
#             pygame.draw.line(WINDOW, (255, 0, 0), (self.row, self.col), (self.row + self.size, self.col), 2)
#         if self.right:
#             pygame.draw.line(WINDOW, (255, 0, 0), (self.row + self.size, self.col), (self.row + self.size, self.col + self.size), 2)
#         if self.bottom:
#             pygame.draw.line(WINDOW, (255, 0, 0), (self.row, self.col + self.size), (self.row + self.size, self.col + self.size), 2)
#         if self.left:
#             pygame.draw.line(WINDOW, (255, 0, 0), (self.row, self.col), (self.row, self.col + self.size), 2)

# class Player(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         self.size = tile_size * 0.65
#         self.row = MAZE.start_tile[0]
#         self.col = MAZE.start_tile[1]
#         # self.x = MAZE[self.row][self.col].x
#         # self.y = MAZE[self.row][self.col].y
#         self.rect = pygame.Rect(self.row, self.col, self.size, self.size)
#         self.rect.center = MAZE.tiles[self.row][self.col].rect.center
#         self.color = (0, 0, 255)

#     def set_player_to_tile(self, row, col):
#         # self.row = random.randint(0, 9)
#         # self.col = random.randint(0, 9)
#         self.row = row
#         self.col = col
#         self.rect.center = MAZE.tiles[self.row][self.col].rect.center

#     def draw(self):
#         pygame.draw.rect(WINDOW, self.color, self.rect)


# class Maze:
#     def __init__(self) -> None:
#         # Init Maze Parameters
#         self.size = (10, 10)
#         self.tiles = [[None] * self.size[0] for i in range(self.size[1])]

#         #  gen tiles
#         self.gen_tiles()

#         self.start_tile = (0, 0)
#         self.end_tile = (self.size[0] - 1, self.size[1] - 1)
#         self.tiles[self.start_tile[0]][self.start_tile[1]].visited = True

#     def gen_tiles(self):
#         for i in range(self.size[0]):
#             for j in range(self.size[1]):
#                 self.tiles[i][j] = Tile(j * tile_size + tile_size, i * tile_size + tile_size, tile_size)

#     def show_maze(self):
#         for row in range(self.size[0]):
#             for col in range(self.size[1]):
#                 self.tiles[row][col].show_tile(WINDOW)

#     def next_move(self):
#         pass