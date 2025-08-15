import pygame

import config
import random

VIOLET = (148, 34, 139)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (30, 144, 255)


class adjacentBombNumber:
    num = 0
    position = []

    def __init__(self, position, num):
        self.position = position
        self.num = num

    def drawNumber(self, display):
        color = LIGHT_BLUE
        if self.num == 1:
            color = LIGHT_BLUE
        if self.num == 2:
            color = GREEN
        if self.num == 3:
            color = RED
        if self.num == 4:
            color = VIOLET
        if self.num == 5:
            color = LIGHT_BLUE
        if self.num == 6:
            pass
        if self.num == 7:
            pass
        if self.num == 8:
            pass
        font = pygame.font.Font("freesansbold.ttf", 15)
        text = font.render(str(self.num), True, color)
        text_rect = text.get_rect()
        text_rect.center = (
            self.position[0] * (config.TILE_WIDTH + config.TILE_SPACING)
            + config.TILE_WIDTH // 2,
            (self.position[1] * (config.TILE_WIDTH + config.TILE_SPACING))
            + config.TILE_WIDTH // 2,
        )
        display.blit(text, text_rect)


class Grid:
    bombs = []
    adjacent_bombs = []
    empty = []

    def __init__(self):
        num_of_bombs = config.BOMB_COUNT
        if num_of_bombs > config.NUMBER_OF_TILES_HEIGHT * config.NUMBER_OF_TILES_WIDTH:
            num_of_bombs = (
                config.NUMBER_OF_TILES_WIDTH * config.NUMBER_OF_TILES_HEIGHT // 2
            )

        for x in range(config.NUMBER_OF_TILES_WIDTH):
            for y in range(config.NUMBER_OF_TILES_HEIGHT):
                self.empty.append([x, y])
        for i in range(num_of_bombs):
            cond = True
            while cond:
                x = random.randint(0, config.NUMBER_OF_TILES_WIDTH - 1)
                y = random.randint(0, config.NUMBER_OF_TILES_HEIGHT - 1)
                position = [x, y]
                bomb = Bomb(position)

                if bomb not in self.bombs:
                    if position in self.empty:
                        self.bombs.append(bomb)
                        self.empty.remove(position)
                        cond = False
        for position in self.empty.copy():
            self.check_for_adjacent_bombs(position)

    def get_empty(self):
        return self.empty

    def check_for_adjacent_bombs(self, position):
        num = 0
        for xShift in range(-1, 2):
            for yShift in range(-1, 2):
                if [xShift, yShift] == [0, 0]:
                    continue
                else:
                    x = position[0] + xShift
                    y = position[1] + yShift
                    for bombs in self.bombs:
                        if [x, y] == bombs.position:
                            num += 1
        if num != 0:
            self.empty.remove(position)
            new_num = adjacentBombNumber(position, num)
            self.adjacent_bombs.append(new_num)

    def draw_adj_bomb_num(self, display):
        for adjBombs in self.adjacent_bombs:
            adjBombs.drawNumber(display)

    def get_bombs(self):
        return self.bombs

    def draw_bombs(self, display):
        for bomb in self.bombs:
            bomb.draw_bomb(display)

    def draw_grid(self, display):
        self.draw_bombs(display)
        self.draw_adj_bomb_num(display)

        for x in range(0, config.WINDOW_WIDTH, config.TILE_WIDTH + config.TILE_SPACING):
            pygame.draw.line(
                display,
                (40, 40, 40),
                (x - config.TILE_SPACING, 0),
                (x - config.TILE_SPACING, config.WINDOW_HEIGHT),
                config.TILE_SPACING,
            )

        for y in range(
            0, config.WINDOW_HEIGHT, config.TILE_WIDTH + config.TILE_SPACING
        ):
            pygame.draw.line(
                display,
                (40, 40, 40),
                (0, y - config.TILE_SPACING),
                (config.WINDOW_WIDTH, y - config.TILE_SPACING),
                config.TILE_SPACING,
            )


class Bomb:
    position = []

    def __init__(self, position):
        self.position = position

    def draw_bomb(self, display):
        pygame.draw.circle(
            display,
            (0, 0, 0),
            (
                self.position[0] * (config.TILE_WIDTH + config.TILE_SPACING)
                + config.TILE_WIDTH // 2,
                self.position[1] * (config.TILE_WIDTH + config.TILE_SPACING)
                + config.TILE_WIDTH // 2,
            ),
            7,
            0,
        )


class Flag:
    def drawFlag(self, display, position):
        x = position[0] * (config.TILE_WIDTH + config.TILE_SPACING)
        y = position[1] * (config.TILE_WIDTH + config.TILE_SPACING)
        flagTopLeftX = config.TILE_WIDTH * 0.5
        flagTopLeftY = 1
        flagHeight = 4
        flagLength = 5
        pygame.draw.polygon(
            display,
            (200, 0, 0),
            [
                (x + flagTopLeftX, y + flagTopLeftY),
                (x + flagTopLeftX, y + flagTopLeftY + flagHeight),
                (x + flagTopLeftX + flagLength, y + flagTopLeftY + flagHeight / 2),
            ],
        )
        pygame.draw.rect(
            display,
            (0, 0, 0),
            (
                x + config.TILE_WIDTH * 0.5,
                y + 1,
                config.TILE_WIDTH * 0.13,
                config.TILE_WIDTH * 0.8,
            ),
        )
