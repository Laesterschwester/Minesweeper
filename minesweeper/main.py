import pygame
import config
import game
import gamestate


def start():
    pygame.init()

    size = (config.WINDOW_WIDTH, config.WINDOW_HEIGHT)
    display = pygame.display.set_mode(size)
    display.fill((255, 255, 255, 255))
    clock = pygame.time.Clock()

    tiles = game.Tiles()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONUP and (
                event.button == 1 or event.button == 3
            ):
                if gamestate.game_state is gamestate.GameState.PLAYING:
                    tiles.mouse_event(event)

            if event.type == pygame.QUIT:
                pygame.quit()
                raise SystemExit

        tiles.draw(display)
        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    start()
