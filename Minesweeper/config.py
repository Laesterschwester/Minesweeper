TILE_WIDTH = 15
TILE_COLOR = (150, 150, 150)
TILE_SPACING = 3


WINDOW_RATIO = 1
NUMBER_OF_TILES_HEIGHT = 20
NUMBER_OF_TILES_WIDTH = NUMBER_OF_TILES_HEIGHT*WINDOW_RATIO
WINDOW_HEIGHT = NUMBER_OF_TILES_HEIGHT*TILE_WIDTH + (NUMBER_OF_TILES_HEIGHT-1)*TILE_SPACING
WINDOW_WIDTH = NUMBER_OF_TILES_HEIGHT*WINDOW_RATIO*TILE_WIDTH + (WINDOW_RATIO*NUMBER_OF_TILES_HEIGHT-1)*TILE_SPACING

VIOLET = (148, 34, 139)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
LIGHT_BLUE = (30, 144, 255)

BOMB_COUNT = NUMBER_OF_TILES_HEIGHT*NUMBER_OF_TILES_WIDTH//8
BOMB_COLOR = (255, 0, 0)
BOMB_WIDTH = TILE_WIDTH-TILE_WIDTH*0.8