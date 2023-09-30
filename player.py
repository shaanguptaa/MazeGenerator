from pygame.draw import rect, circle
from pygame import Rect
from pygame.sprite import Sprite

class Player(Sprite):
    def __init__(self, start_tile):
        super().__init__()
        self.size = start_tile.size * 0.65
        self.row = start_tile.row
        self.col = start_tile.col
        self.x =  self.col * self.size + self.size
        self.y =  self.row * self.size + self.size
        self.rect = Rect(self.x, self.y, self.size, self.size)
        self.rect.center = start_tile.rect.center
        self.color = (0, 0, 255)

    def set_player_to_tile(self, tile):
        self.row = tile.row
        self.col = tile.col
        self.x =  self.col * self.size + self.size
        self.y =  self.row * self.size + self.size
        self.rect.center = tile.rect.center       

    def draw(self, window):
        rect(window, self.color, self.rect, 0, round(self.size / 2))
        