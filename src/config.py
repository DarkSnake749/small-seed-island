from pygame import Surface, display
from camera import Camera
from os import environ

# Window
environ['SDL_VIDEO_CENTERED'] = '1'
info = display.Info()


class Player_config:
    COLOR: str = "white"
    WIDTH: int = 35
    HEIGTH: int = 35
    ACCELERATION: float = .5
    SPEED: float = 4.5


class Game_config:

    # size
    WIDTH = info.current_w - 10
    HEIGHT = info.current_w - 10

    TITLE = "Small Seed Island"
    ICON = Surface((20, 20))

    # Other paramters
    FPS = 120
    BACKDROP_COLOR = "Black"

    # Camera
    SPRITES: list = []