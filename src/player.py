import pygame as pg

class Player:
    def __init__(self):
        self.health: int = 100
        self.width: int = 20 #surement a modifier plus tard
        self.height: int = 20 #surement a modifier plus tard
        self.rect: tuple = (0, 0, self.width, self.height)

    def draw(self, screen):
        pg.draw.rect(screen, (255, 255, 255), self.rect)