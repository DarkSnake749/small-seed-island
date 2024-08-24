import pygame

class Tree:
    def __init__(self, color: str =  "blue", starting_pos: tuple[int, int] = (0,0)):
        self.id: str = "tree"
        # Image
        self.image: pygame.Surface = pygame.Surface((35, 50))
        self.image.fill(color)
        # Collider
        self.rect: pygame.Rect = self.image.get_rect(center = starting_pos)
        # Hitbox
        self.hitbox: pygame.Rect = self.rect.copy().inflate(-self.rect.width * .2, -self.rect.height * .75)
        self.hitbox_offset: int = 27
    
    def update(self) -> None:
        # Update the hitbox offset
        self.hitbox.y = self.rect.y + self.hitbox_offset
