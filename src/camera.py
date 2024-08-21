import pygame

class Camera:
    def __init__(self, sprites: list) -> None:
        self.sprites: list = list
        """List of all sprite that will be drawn on the screen"""

        self.__win = pygame.display.get_surface()
        """Surface where the sprites will be drawn"""

    def __len__(self) -> int:
        return len(self.sprites)

    def update(self) -> None:
        """Update all sprites in the window"""
        for sprite in self.sprites:
            # Draw sprite
            self.__win.blit(sprite.image, sprite.rect)
            # Update sprite
            sprite.update()
