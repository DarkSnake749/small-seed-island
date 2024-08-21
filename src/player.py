import pygame

class Player:
    def __init__(
            self, color: str = "white", width: int = 35, height: 
            int = 35, acceleration: float = .5, speed: float = 4.5
        ) -> None:
        self.id: str = "player"
        """Identification of the player"""

        # Paramters
        self.__color: str = color
        self.__width: int = width
        self.__height: int = height
        self.__acceleration: float = acceleration
        self.__speed: float = speed

        # Image of the player
        self.image: pygame.Surface = pygame.Surface((self.__width, self.__height))
        self.image.fill(self.__color)
        # Player collider
        self.rect: pygame.Rect = self.image.get_rect()
    
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
        