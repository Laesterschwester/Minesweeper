import pygame
import game_grid as g_grid
import config
import grid


def start():
    pygame.init()

    size = (config.WINDOW_WIDTH, config.WINDOW_HEIGHT)
    display = pygame.display.set_mode(size)

    clock = pygame.time.Clock()

    overlay_tiles = grid.Grid()
    game_grid = g_grid.Grid()

    display.fill((255, 255, 255, 255))
    game_grid.draw_grid(display)

    empty_tiles = game_grid.get_empty()

    mouse_down = False

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()

        pygame.event.get()
        if event.type == pygame.MOUSEBUTTONDOWN and not mouse_down:
            overlay_tiles.click_on_grid(event, empty_tiles, game_grid.bombs)
            mouse_down = True
        else:
            if event.type == pygame.MOUSEBUTTONUP:
                mouse_down = False
                display.fill((255, 255, 255, 255))
                game_grid.draw_grid(display)
        overlay_tiles.draw_grid(display)

        clock.tick(60)
        pygame.display.update()


if __name__ == "__main__":
    start()
