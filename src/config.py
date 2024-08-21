from pygame import Surface
from camera import Camera

# Window
WIDTH = 500
HEIGHT = 500
CAPTION = "Small Seed Island"
ICON = Surface(20, 20)

# Other paramters
FPS = 120
BACKDROP_COLOR = "Black"

# Camera
CAMERA: Camera = Camera([]) # TODO 3. Add the player here
