import config
import pygame


class Bomb:
    position = []

    def __init__(self,  position):
        self.position = position


    def drawBomb(self, display):
        pygame.draw.circle(display, (0, 0, 0), (self.position[0]*(config.TILE_WIDTH+config.TILE_SPACING)+config.TILE_WIDTH//2, self.position[1]*(config.TILE_WIDTH+config.TILE_SPACING)+config.TILE_WIDTH//2), 7, 0)