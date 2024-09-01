import pygame

class PNG:
    def __init__(self, color: str = "green", starting_pos: tuple[int, int] = (0,0), id: str = ""):
        self.id = 'npc' + id
        # Image
        self.image: pygame.Surface = pygame.Surface((35, 35))
        self.image.fill(color)
        # Collider
        self.rect: pygame.Rect = self.image.get_rect(center = starting_pos)
        # Toogle area
        self.area: pygame.Rect = self.rect.copy().inflate(120, 120)
    
    def update(self):
        self.area.centerx = self.rect.centerx 
        self.area.centery = self.rect.centery

class Tree:
    def __init__(self, color: str =  "blue", starting_pos: tuple[int, int] = (0,0)):
        self.id: str = "tree"
        # Image
        self.image: pygame.Surface = pygame.Surface((35, 50))
        self.image.fill(color)
        # Collider
        self.rect: pygame.Rect = self.image.get_rect(center = starting_pos)
        # Hitbox
        self.hitbox_offset: int = 10
        self.hitbox: pygame.Rect = self.rect.copy().inflate(-self.rect.width * .2, -self.rect.height * .9)
        self.hitbox.centery = self.rect.centery + self.hitbox_offset
    
    def update(self) -> None: ...
