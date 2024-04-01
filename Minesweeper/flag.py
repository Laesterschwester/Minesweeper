import config
import pygame

class Flag:
    def drawFlag(self, display, position):
        x = position[0]*(config.TILE_WIDTH+config.TILE_SPACING)
        y = position[1]*(config.TILE_WIDTH+config.TILE_SPACING)
        flagTopLeftX = config.TILE_WIDTH*0.5
        flagTopLeftY = 1
        flagHeight = 4
        flagLength = 5
        pygame.draw.polygon(display, (200, 0, 0), [(x+flagTopLeftX, y+flagTopLeftY), (x+flagTopLeftX, y+flagTopLeftY+flagHeight), (x+flagTopLeftX+flagLength, y+flagTopLeftY+flagHeight/2)])#flag
        pygame.draw.rect(display, (0, 0, 0), (x+config.TILE_WIDTH*0.5, y+1, config.TILE_WIDTH*0.13, config.TILE_WIDTH*0.8))#post
        """        pygame.draw.rect(display, (0, 0, 0), (x+config.TILE_WIDTH*0.27, y+config.TILE_WIDTH*0.75, config.TILE_WIDTH*0.5, config.TILE_WIDTH*0.2))#"podest"
        """


