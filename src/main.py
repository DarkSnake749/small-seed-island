import pygame as pg
from sys import exit

from player import *

pg.init()

class Game:
    def __init__(self) -> None:
        #variable visuel
        self.screen: pg.Surface = pg.display.set_mode((1270, 720))
        self.background_color: pg.Color = pg.Color(0, 0, 0, 255)

        #variable loop
        self.run: bool = True

        #variable clock
        self.clock: pg.time.Clock = pg.time.Clock()
        self.max_framerate: int = 60

        #variable player
        self.player: Player = Player()
    
    def event_loop(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.run = False

    def main_loop(self) -> None:
        while self.run:
            self.event_loop()

            # Clear the background
            self.screen.fill(self.background_color)

            # Update the player
            self.player.update()

            pg.display.update()
            self.clock.tick(self.max_framerate)
        
        pg.quit()
        exit()

if __name__ == "__main__":
    game: Game = Game()
    game.main_loop()
