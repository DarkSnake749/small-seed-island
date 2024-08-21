from pygame import Surface
from game import Game

def main() -> None:
    """Main function of the script"""
    game = Game((500, 500), "App", Surface((20,20)), 120)
    game.run()

# Launch the game
if __name__ == '__main__':
    main()