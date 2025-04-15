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
        self.delta_time: float = 0.0

        #variable clock
        self.clock: pg.time.Clock = pg.time.Clock()
        self.tps: int = 60
        """ Tick per seconds. Variables to control the speed of the clock """

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
            self.player.update(self.delta_time)

            pg.display.update()
            self.delta_time = self.clock.tick(self.tps) / 1000
            self.delta_time = max(0.001, min(0.1, self.delta_time))
        
        pg.quit()
        exit()

def main() -> None:
    game: Game = Game()
    game.main_loop()

if __name__ == "__main__":
    main()
