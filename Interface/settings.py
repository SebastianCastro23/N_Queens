import os

# Colores
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREY = (40, 40, 40)
LIGHTGREY = (180, 180, 180)

# Configuraciones del juego
SCREEN_WIDTH = 832  # Multiplos de 32
SCREEN_HEIGHT = 900
SCREEN_SIZE = (round(SCREEN_WIDTH), SCREEN_HEIGHT)
FPS = 120
TITLE = "N Queens"
TILESIZE = 32
GRIDWIDTH = SCREEN_WIDTH / TILESIZE
GRIDHEIGHT = SCREEN_HEIGHT / TILESIZE

# Direcciones de recursos
dir_game = os.path.dirname(__file__)
dir_images = os.path.join(dir_game, "img")