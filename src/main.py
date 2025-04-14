import pygame as pg
from sys import exit

pg.init()

class Game:
    def __init__(self):
        self.screen: pg.Surface = pg.display.set_mode((1270, 720))
        self.background_color: pg.Color = pg.Color(0, 0, 0, 255)

        self.run: bool = True

        self.clock: pg.time.Clock = pg.time.Clock()
        self.max_framrate: int = 60
    
    def event_loop(self) -> None:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.run = False

    def main_loop(self):
        while self.run:
            self.event_loop()

            # Clear the background
            self.screen.fill(self.background_color)

            pg.display.update()
            self.clock.tick(self.max_framrate)
        
        pg.quit()
        exit()

if __name__ == "__main__":
    game: Game = Game()
    game.main_loop()
    