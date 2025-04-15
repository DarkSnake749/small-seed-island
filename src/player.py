import pygame as pg

class Player:
    def __init__(self, health: int = 100,) -> None:
        self.screen: pg.Surface = pg.display.get_surface()
        self.health: int = 100
        self.rect: pg.Rect = pg.Rect(0, 0, 20, 20)

        self.direction: pg.Vector2 = pg.Vector2(0, 0)
        self.velocity: pg.Vector2 = pg.Vector2(0, 0)
        self.position: pg.Vector2 = pg.Vector2(0, 0)

        #self.width: int = 20 
        #self.height: int = 20

    def draw(self) -> None:
        pg.draw.rect(self.screen, (255, 255, 255), self.rect)
    
    def update(self) -> None:
        self.draw()

    def move(self) -> None: #g pas pu faire plus doit aller manger
        key = pg.key.get_pressed()

        if key[pg.K_w]:
            pass
        if key[pg.K_s]:
            pass
        if key[pg.K_a]:
            pass
        if key[pg.K_d]:
            pass
