import random
import pygame
import config
import gamestate

VIOLET = (148, 34, 139)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (30, 144, 255)
ROSE = (243, 58, 106)
MINT = (152, 255, 152)
YELLOW = 154, 205, 50
COLORS = [VIOLET, GREEN, RED, BLUE, LIGHT_BLUE, ROSE, MINT, YELLOW]


class TileState:
    HIDDEN = 1
    FLAGGED = 2
    REVEALED = 3


class Tile:
    def __init__(self, state=TileState.HIDDEN, bomb=False):
        self.state = state
        self.is_bomb = bomb
        self.adjacent_bombs = 0

    @classmethod
    def draw_flagged_tile(self, display, position, width):
        Tile.draw_hidden_tile(display, position, width)

        #TODO make it look nicer
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

    @classmethod
    def draw_hidden_tile(cls, display, position, width):
        a = position[0] * (config.TILE_WIDTH + config.TILE_SPACING)
        b = position[1] * (config.TILE_WIDTH + config.TILE_SPACING)

        pygame.draw.rect(
            display,
            (100, 100, 100),
            (a, b, width, width),
        )

    @classmethod
    def draw_empty_tile(cls, display, position, width):
        a = position[0] * (config.TILE_WIDTH + config.TILE_SPACING)
        b = position[1] * (config.TILE_WIDTH + config.TILE_SPACING)

        pygame.draw.rect(
            display,
            (200, 200, 200),
            (a, b, width, width),
        )

    @classmethod
    def draw_bomb(cls, display, position, width):
        width = config.TILE_WIDTH
        spacing = config.TILE_SPACING
        pygame.draw.circle(
            display,
            (0, 0, 0),
            (
                position[0] * (width + spacing) + width // 2,
                position[1] * (width + spacing) + width // 2,
            ),
            7,
            0,
        )

    @classmethod
    def draw_number(cls, display, position, width, num):
        color = COLORS[num - 1]

        font = pygame.font.Font("freesansbold.ttf", 15)
        text = font.render(str(num), True, color)
        text_rect = text.get_rect()

        width = config.TILE_WIDTH
        spacing = config.TILE_SPACING
        text_rect.center = (
            position[0] * (width + spacing) + width // 2,
            position[1] * (width + spacing) + width // 2,
        )
        display.blit(text, text_rect)

    def draw(self, display, position):
        width = config.TILE_WIDTH
        if self.state is TileState.FLAGGED:
            Tile.draw_flagged_tile(display, position, width)
        elif self.state is TileState.HIDDEN:
            Tile.draw_hidden_tile(display, position, width)
        else:
            Tile.draw_empty_tile(display, position, width)
            if self.is_bomb:
                Tile.draw_bomb(display, position, width)
            elif self.adjacent_bombs > 0:
                Tile.draw_number(display, position, width, self.adjacent_bombs)


class Tiles:
    def __init__(self):
        height = config.NUMBER_OF_TILES_HEIGHT
        width = config.NUMBER_OF_TILES_WIDTH
        self.game_board = [[Tile() for j in range(height)] for i in range(width)]

        num_of_bombs = config.BOMB_COUNT
        if num_of_bombs > height * width:
            num_of_bombs = width * height // 2

        while num_of_bombs > 0:
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)

            if not self.game_board[x][y].is_bomb:
                self.game_board[x][y].is_bomb = True
                num_of_bombs -= 1

        # fmt: off
        directions = [
            (-1, -1), (0, -1), (1, -1),
            (-1,  0),          (1,  0),
            (-1,  1), (0,  1), (1,  1),
        ]
        # fmt: on

        for x in range(len(self.game_board)):
            for y in range(len(self.game_board[0])):
                for dx, dy in directions:
                    if not (
                        0 <= x + dx < len(self.game_board)
                        and 0 <= y + dy < len(self.game_board[0])
                    ):
                        continue

                    if self.game_board[x + dx][y + dy].is_bomb:
                        self.game_board[x][y].adjacent_bombs += 1

    def draw(self, display):
        for x in range(len(self.game_board)):
            for y in range(len(self.game_board[0])):
                self.game_board[x][y].draw(display, [x, y])

    def reveal_bombs(self):
        for row in self.game_board:
            for tile in row:
                if not tile.is_bomb:
                    continue
                tile.state = TileState.REVEALED

    def left_button_handler(self, event):
        x = event.pos[0] // (config.TILE_WIDTH + config.TILE_SPACING)
        y = event.pos[1] // (config.TILE_WIDTH + config.TILE_SPACING)

        if self.game_board[x][y].state is not TileState.HIDDEN:
            return

        if self.game_board[x][y].is_bomb:
            gamestate.game_state = gamestate.GameState.LOST
            self.reveal_bombs()
            return

        self.reveal_recursive([x, y])

    def right_button_handler(self, event):
        x = event.pos[0] // (config.TILE_WIDTH + config.TILE_SPACING)
        y = event.pos[1] // (config.TILE_WIDTH + config.TILE_SPACING)

        if self.game_board[x][y].state is TileState.REVEALED:
            return

        if self.game_board[x][y].state is TileState.HIDDEN:
            self.game_board[x][y].state = TileState.FLAGGED
        else:
            self.game_board[x][y].state = TileState.HIDDEN

    def mouse_event(self, event):
        if event.button == 1:
            self.left_button_handler(event)
        else:
            self.right_button_handler(event)

    def reveal_recursive(self, position):
        x = position[0]
        y = position[1]

        if self.game_board[x][y].state is not TileState.HIDDEN:
            return

        self.game_board[x][y].state = TileState.REVEALED

        if self.game_board[x][y].adjacent_bombs != 0:
            return

        for x_shift in range(-1, 2):
            for y_shift in range(-1, 2):
                x = position[0] + x_shift
                y = position[1] + y_shift

                if (
                    x < 0
                    or y < 0
                    or x >= config.NUMBER_OF_TILES_WIDTH
                    or y >= config.NUMBER_OF_TILES_HEIGHT
                ):
                    continue

                self.reveal_recursive((x, y))
