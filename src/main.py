from config import *
from game import Game

def main() -> None:
    """Main function of the script"""
    game = Game((WIDTH, HEIGHT), CAPTION, ICON, FPS, BACKDROP_COLOR, CAMERA)
    game.run()

# Launch the game
if __name__ == '__main__':
    main()