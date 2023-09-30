from tile import Tile

class Maze:
    def __init__(self):
        # Init Maze Parameters
        self.size = (20, 20)
        self.tiles = [[None] * self.size[0] for i in range(self.size[1])]

        #  gen tiles
        self.gen_tiles()

        self.start_tile = (0, 0)
        self.end_tile = (self.size[0] - 1, self.size[1] - 1)
        self.tiles[self.start_tile[0]][self.start_tile[1]].visited = True

    def gen_tiles(self):
        for i in range(self.size[0]):
            for j in range(self.size[1]):
                self.tiles[i][j] = Tile(i, j)

    def show_maze(self, window):
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                self.tiles[row][col].show_tile(window)

    def get_tile(self, row, col):
        return self.tiles[row][col]
    
    def get_start_tile(self):
        return self.tiles[self.start_tile[0]][self.start_tile[1]]
    
    def get_moves_for_tile(self, row, col, check_exclude_moves = True):
        tile = self.get_tile(row, col)
        moves = []
        if tile.row > 0 and (not self.get_tile(tile.row - 1, tile.col).visited):
            moves.append('top')
        if tile.row < self.size[1] - 1 and (not self.get_tile(tile.row + 1, tile.col).visited):
            moves.append('bottom')
        if tile.col > 0 and (not self.get_tile(tile.row, tile.col - 1).visited):
            moves.append('left')
        if tile.col < self.size[0] - 1 and (not self.get_tile(tile.row, tile.col + 1).visited):
            moves.append('right')
        
        if check_exclude_moves:
            moves = list(set(moves) - tile.exclude_moves)
        return moves
        
    def move(self, player, pref_move):
        curr_tile = self.get_tile(player.row, player.col)
        
        self.tiles[curr_tile.row][curr_tile.col].visited = True
        self.tiles[curr_tile.row][curr_tile.col].color = (255, 255, 255)

        new_row = curr_tile.row
        new_col = curr_tile.col
        
        if pref_move == 'top':
            new_row -= 1
            self.tiles[curr_tile.row][curr_tile.col].top = False
            self.tiles[new_row][new_col].bottom = False

        elif pref_move == 'bottom':
            new_row += 1
            self.tiles[curr_tile.row][curr_tile.col].bottom = False
            self.tiles[new_row][new_col].top = False
        
        elif pref_move == 'left':
            new_col -= 1
            self.tiles[curr_tile.row][curr_tile.col].left = False
            self.tiles[new_row][new_col].right = False
        
        elif pref_move == 'right':
            new_col += 1
            self.tiles[curr_tile.row][curr_tile.col].right = False
            self.tiles[new_row][new_col].left = False

        player.set_player_to_tile(self.get_tile(new_row, new_col))
        self.tiles[new_row][new_col].color = (255, 255, 255)
        self.tiles[new_row][new_col].visited = True

    def move_back(self, player, played_move):
        curr_tile = self.get_tile(player.row, player.col)
        
        self.tiles[curr_tile.row][curr_tile.col].visited = False
        self.tiles[curr_tile.row][curr_tile.col].color = (0, 255, 0)

        new_row = curr_tile.row
        new_col = curr_tile.col
        
        if played_move == 'bottom':
            new_row -= 1
            self.tiles[curr_tile.row][curr_tile.col].top = True
            self.tiles[new_row][new_col].bottom = True

        elif played_move == 'top':
            new_row += 1
            self.tiles[curr_tile.row][curr_tile.col].bottom = True
            self.tiles[new_row][new_col].top = True
        
        elif played_move == 'right':
            new_col -= 1
            self.tiles[curr_tile.row][curr_tile.col].left = True
            self.tiles[new_row][new_col].right = True
        
        elif played_move == 'left':
            new_col += 1
            self.tiles[curr_tile.row][curr_tile.col].right = True
            self.tiles[new_row][new_col].left = True

        player.set_player_to_tile(self.get_tile(new_row, new_col))
        self.tiles[new_row][new_col].exclude_moves.add(played_move)

    def reached_finish(self, player):
        return player.row == self.end_tile[0] and player.col == self.end_tile[1]

    def get_unvisited_tile(self):
        for row in range(self.size[0]):
            for col in range(self.size[1]):
                if self.tiles[row][col].visited == False:
                    return self.tiles[row][col]
        return None