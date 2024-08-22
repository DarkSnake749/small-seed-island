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
    
    def center_target(self, target) -> pygame.math.Vector2:
        offset: pygame.math.Vector2 = pygame.math.Vector2()
        offset.x = target.rect.centerx - self.__display.get_width() // 2
        offset.y = target.rect.centery - self.__display.get_height() // 2
        return offset

    def update(self) -> None:
        """Update all sprites in the window"""

        # Find the player in all the sprites
        player = None
        for sprite in self.sprites:
            player = sprite if sprite.id == "player" else player
        
        # Update the offset
        offset: pygame.math.Vector2 = self.center_target(player) if player else pygame.math.Vector2(0, 0)

        for sprite in sorted(self.sprites, key = lambda sprite: sprite.rect.centery):
            # Draw sprite
            offset_pos: pygame.Rect = sprite.rect.bottomleft - offset
            self.__display.blit(sprite.image, offset_pos)
            # Update sprite
            sprite.update()
