import pygame as pg

class Player:
    def __init__(self, health: int = 100,) -> None:
        self.screen: pg.Surface = pg.display.get_surface()
        self.health: int = 100
        self.rect: pg.Rect = pg.Rect(0, 0, 20, 20)

        # ? Sûrement à modifer plus tard

        # * Note:
        # * On va le calculer avec en utilisant les beaux sprites qu'ON va trouver ou desing.
        # * Anyway, on en auras pas besoin à cause que la class pg.Rect les a déja built-in.
        # * Je les gardes quand même au cas où... (tu peux le suprrimer quand tu le verras)

        #self.width: int = 20 
        #self.height: int = 20

    def draw(self) -> None:
        pg.draw.rect(self.screen, (255, 255, 255), self.rect)
    
    def update(self) -> None:
        self.draw()
