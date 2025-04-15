import pygame as pg

pg.init()

class Items:
    def __init__(self, durability: int):
        self.durability: int = 1
        self.durability = durability

class Apple(Items):
    def __init__(self, durability):
        super().__init__(durability)
        self.durability: int = 1
        self.surface = pg.image.load("asset/apple.png").convert()