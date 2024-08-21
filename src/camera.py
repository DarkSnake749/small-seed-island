import pygame

class Camera:
    def __init__(self, display: pygame.Surface, sprites: list) -> None:
        self.sprites: list = sprites
        """List of all sprite that will be drawn on the screen"""

        self.__display = display
        """Surface where the sprites will be drawn"""

    def __len__(self) -> int:
        return len(self.sprites)

    def add(self, sprite) -> None:
        self.sprites.append(sprite)

    def update(self) -> None:
        """Update all sprites in the window"""
        for sprite in self.sprites:
            # Draw sprite
            self.__display.blit(sprite.image, sprite.rect)
            # Update sprite
            sprite.update()
