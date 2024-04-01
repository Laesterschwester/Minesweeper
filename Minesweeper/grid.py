import pygame
import config
import gridTile


def drawFlag(display, position):
    x = position[0] * (config.TILE_WIDTH + config.TILE_SPACING)
    y = position[1] * (config.TILE_WIDTH + config.TILE_SPACING)
    flagTopLeftX = config.TILE_WIDTH * 0.5
    flagTopLeftY = 1
    flagHeight = 4
    flagLength = 5
    pygame.draw.polygon(display, (200, 0, 0),
                        [(x + flagTopLeftX, y + flagTopLeftY), (x + flagTopLeftX, y + flagTopLeftY + flagHeight),
                         (x + flagTopLeftX + flagLength, y + flagTopLeftY + flagHeight / 2)])  # flag
    pygame.draw.rect(display, (0, 0, 0),
                     (x + config.TILE_WIDTH * 0.5, y + 1, config.TILE_WIDTH * 0.13, config.TILE_WIDTH * 0.8))  # post
    pygame.draw.rect(display, (0, 0, 0), (
    x + config.TILE_WIDTH * 0.27, y + config.TILE_WIDTH * 0.75, config.TILE_WIDTH * 0.5,
    config.TILE_WIDTH * 0.17))  # "podest"



class Grid:
    grid = [] # 2d

    def __init__(self):
        xGrid = 0
        yGrid = 0
        for x in range(0, config.WINDOW_WIDTH, config.TILE_WIDTH + config.TILE_SPACING):
            self.grid.append([])
            for y in range(0, config.WINDOW_WIDTH, config.TILE_WIDTH + config.TILE_SPACING):
                newTile = gridTile.Tile([x, y])
                self.grid[xGrid].append(newTile)
                yGrid += 1
            xGrid += 1

    def clickOnGrid(self, event, emptyTiles, bombs):
        x = event.pos[0]//(config.TILE_WIDTH+config.TILE_SPACING)
        y = event.pos[1]//(config.TILE_WIDTH+config.TILE_SPACING)

        if [x, y] in emptyTiles and event.button == 1:
            self.revealAdjacent([x, y], emptyTiles)

        for bomb in bombs:
            xBomb = bomb.position[0]
            yBomb = bomb.position[1]
            if [x, y] == [xBomb, yBomb] and event.button == 1 and not self.grid[x][y].flag:
                self.revealBombs(event, bombs)
        else:
            self.grid[x][y].clickTile(event)

    def revealBombs(self, event, bombs):
        for bomb in bombs:
            x = bomb.position[0]
            y = bomb.position[1]
            self.grid[x][y].clickTile(event)

    def revealAdjacent(self, tileIndex, emptyTiles):
        for xShift in range(-1, 2):
            for yShift in range(-1, 2):
                if [xShift, yShift] == [0, 0]:
                    continue
                x = tileIndex[0] + xShift
                y = tileIndex[1] + yShift
                if x < 0 or y < 0 or x > config.NUMBER_OF_TILES_WIDTH-1 or y > config.NUMBER_OF_TILES_HEIGHT-1:
                    continue
                else:
                    if self.grid[x][y].visible == False:
                        continue
                    if [x, y] in emptyTiles:
                        self.grid[x][y].reveal()
                        self.revealAdjacent([x, y], emptyTiles)
                    else:
                        self.grid[x][y].reveal()

    def draw_grid(self, display):
        for x in range(len(self.grid)):
            for y in range(len(self.grid[0])):
                """if(self.grid[x][y].visible):"""
                self.grid[x][y].drawTile(display)
                if self.grid[x][y].flag and not self.grid[x][y].revealed:
                    position = [x, y]
                    drawFlag(display, position)