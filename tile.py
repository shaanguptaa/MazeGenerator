from pygame.sprite import Sprite
from pygame import Rect
from pygame.draw import line, rect
from pygame.display import get_window_size

class Tile(Sprite):
    def __init__(self, row, col):
        super().__init__()
        self.visited = False
        self.top = self.bottom = self.left = self.right = True
        self.size = round(min(get_window_size()) / 22)
        self.row = row
        self.col = col
        self.x = col * self.size + self.size
        self.y = row * self.size + self.size
        self.rect = Rect(self.x, self.y, self.size, self.size)
        self.color = (0, 255, 0)
        self.border_color = (255, 0, 0)
        self.border_width = 2
        self.exclude_moves = set()

    def show_tile(self, window):
        rect(window, self.color, self.rect)
        if self.top:
            line(window, self.border_color, (self.x, self.y), (self.x + self.size, self.y), self.border_width)
        if self.right:
            line(window, self.border_color, (self.x + self.size, self.y), (self.x + self.size, self.y + self.size), self.border_width)
        if self.bottom:
            line(window, self.border_color, (self.x, self.y + self.size), (self.x + self.size, self.y + self.size), self.border_width)
        if self.left:
            line(window, self.border_color, (self.x, self.y), (self.x, self.y + self.size), self.border_width)