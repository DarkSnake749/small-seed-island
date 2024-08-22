import pygame
from config import Player_config as pc
from config import Game_config as gc

class Player:
    def __init__(self) -> None:

        self.id: str = "player"
        """Identification of the player"""

        # Paramters
        self.__color: str = pc.COLOR
        self.__width: int = pc.WIDTH
        self.__height: int = pc.HEIGTH
        self.__acceleration: float = pc.ACCELERATION
        self.__speed: float = pc.SPEED

        # Image of the player
        self.image: pygame.Surface = pygame.Surface((self.__width, self.__height))
        self.image.fill(self.__color)
        # Player collider
        self.rect: pygame.Rect = self.image.get_rect(center = (gc.WIDTH/2, gc.HEIGHT/2))
    
    def movement(self) -> None:
        """Move the player"""
        velocity: pygame.math.Vector2 = pygame.math.Vector2(0 , 0)

        # Listen for inputs
        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            velocity.y -= self.__speed
        if key[pygame.K_s]:
            velocity.y += self.__speed
        if key[pygame.K_a]:
            velocity.x -= self.__speed
        if key[pygame.K_d]:
            velocity.x += self.__speed
        
        if (key[pygame.K_a] ^ key[pygame.K_d]) and (key[pygame.K_w] ^ key[pygame.K_s]):
            velocity.x /= (2**0.5)
            velocity.y /= (2**0.5)

        # Add acceleration
        if not key[pygame.K_w] and not key[pygame.K_s]:
            velocity.y *= self.__acceleration
        if not key[pygame.K_a] and not key[pygame.K_d]:
            velocity.x *= self.__acceleration

        # Update position
        self.rect.x += velocity.x
        self.rect.y += velocity.y
    
    def update(self) -> None:
        """Update the player"""
        self.movement()
