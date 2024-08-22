from pygame import Surface, display
from camera import Camera
from os import environ

# Window
environ['SDL_VIDEO_CENTERED'] = '1'
info = display.Info()


class Game_config:

    # size
    WIDTH: int = info.current_w
    HEIGHT: int = info.current_h

    TITLE: str= "Small Seed Island"
    ICON: Surface = Surface((20, 20))

    # Other paramters
    FPS: int = 120
    BACKDROP_COLOR: str = "Black"

    # Camera
    SPRITES: list = []


class Player_config:
    COLOR: str = "white"
    WIDTH: int = 35
    HEIGTH: int = WIDTH
    ACCELERATION: float = .5
    SPEED: float = WIDTH / 10
