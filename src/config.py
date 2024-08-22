from pygame import Surface, display
from camera import Camera
from os import environ

# Window
environ['SDL_VIDEO_CENTERED'] = '1'
info = display.Info()


class Game_config:

    # size
    WIDTH = info.current_w
    HEIGHT = info.current_h

    TITLE = "Small Seed Island"
    ICON = Surface((20, 20))

    # Other paramters
    FPS = 120
    BACKDROP_COLOR = "Black"

    # Camera
    SPRITES: list = []


class Player_config:
    COLOR: str = "white"
    WIDTH: int = ((Game_config.WIDTH + Game_config.HEIGHT) / 2) / 35
    HEIGTH: int = WIDTH
    ACCELERATION: float = .5
    SPEED: float = WIDTH / 10
