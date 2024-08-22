import pygame

class Tree:
    def __init__(self, color: str =  "blue", starting_pos: tuple[int, int] = (0,0)):
        self.id: str = "tree"
        # Image
        self.image: pygame.Surface = pygame.Surface((50, 20))
        self.image.fill(color)
        # Collider
        self.rect: pygame.Rect = self.image.get_rect(center = starting_pos)
    
    def update(self) -> None:
        pass