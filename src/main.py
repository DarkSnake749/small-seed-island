from pygame import init

# Init pygame
init()

from config import Game_config as gc
from game import Game

def main() -> None:
    """Main function of the script"""
    game: Game = Game((gc.WIDTH, gc.HEIGHT), gc.TITLE, gc.ICON, gc.FPS, gc.BACKDROP_COLOR, gc.SPRITES)
    game.run()

# Launch the game
if __name__ == '__main__':
    main()
