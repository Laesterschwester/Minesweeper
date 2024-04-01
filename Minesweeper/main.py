import pygame
import bombNumberDisplayGrid
import config
import grid

pygame.init()
size = (config.WINDOW_WIDTH, config.WINDOW_HEIGHT)
display = pygame.display.set_mode(size)

clock = pygame.time.Clock()
new_tileGrid = grid.Grid()
new_grid = bombNumberDisplayGrid.Grid()

display.fill(
        (255, 255, 255, 255)
)
new_grid.drawGrid(display)

emptyTiles = new_grid.getEmpty()

mouseButtonPressed = False

while 1:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()

    pygame.event.get()
    if event.type == pygame.MOUSEBUTTONDOWN and not mouseButtonPressed:
        new_tileGrid.clickOnGrid(event, emptyTiles, new_grid.bombs)
        mouseButtonPressed = True
    else:
        if event.type == pygame.MOUSEBUTTONUP:
            mouseButtonPressed = False
            display.fill(
                (255, 255, 255, 255)
            )
            new_grid.drawGrid(display)

    new_tileGrid.draw_grid(display)




    clock.tick(60)
    pygame.display.update()