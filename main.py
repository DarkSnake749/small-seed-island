import pygame as pg
from sys import exit

pg.init()

class Game:
    def __init__(self):
        self.screen = pg.display.set_mode((800, 800))

    def main(self):
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    exit()

if __name__ == "__main__":
    main: Game = Game()
    main.main()