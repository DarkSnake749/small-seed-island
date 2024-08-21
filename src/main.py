from config import *
from game import Game

def main() -> None:
    """Main function of the script"""
    game: Game = Game((WIDTH, HEIGHT), TITLE, ICON, FPS, BACKDROP_COLOR, SPRITES)
    game.run()

# Launch the game
if __name__ == '__main__':
    main()
