import config
import pygame


class Tile:
    bomb = False
    flag = False
    revealed = False
    visible = True
    color = config.TILE_COLOR
    position = []
    width = config.TILE_WIDTH

    def __init__(self, position):
        self.position = position
        pass

    def is_empty(self):
        if not self.bomb and not self.flag:
            return True
        else:
            return False

    def get_bool_flag(self):
        return self.visible

    def set_flag(self):
        self.flag = True

    def delete_flag(self):
        self.flag = False

    def place_bomb(self):
        self.bomb = True

    def change_color(self, col):
        self.color = col

    def click_tile(self, event):
        if event.button == 1 and not self.flag:
            self.reveal()
        elif event.button == 3:
            if not self.flag and self.visible:
                self.flag = True
            else:
                self.flag = False

    def reveal(self):
        self.visible = False

    def draw_tile(self, display):
        if self.visible:
            pygame.draw.rect(
                display,
                self.color,
                (self.position[0], self.position[1], self.width, self.width),
            )
