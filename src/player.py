import pygame
from config import Player_config as pc
from config import Game_config as gc
from camera import Camera

class Player:
    def __init__(self, camera: Camera) -> None:

        self.id: str = "player"
        """Identification of the player"""

        self.camera: Camera = camera
        """Can cycle through all the element of the window. Useful for collision"""

        # Paramters
        self.__color: str = pc.COLOR
        self.__width: int = pc.WIDTH
        self.__height: int = pc.HEIGTH
        self.__acceleration: float = pc.ACCELERATION
        self.__speed: float = pc.SPEED
        self.__direction: pygame.math.Vector2 = pygame.math.Vector2(0, 0)

        #state of the player
        self.draw_inventory_state: bool = False

        # Image of the player
        self.image: pygame.Surface = pygame.Surface((self.__width, self.__height))
        self.image.fill(self.__color)
        # Player collider
        self.rect: pygame.Rect = self.image.get_rect(center = (gc.WIDTH/2, gc.HEIGHT/2))
    
    def direction(self) -> None:
        # Listen for inputs
        key = pygame.key.get_pressed()
        # Y axis
        if key[pygame.K_w]:
            self.__direction.y = -1
        elif key[pygame.K_s]:
            self.__direction.y = 1
        else: self.__direction.y = 0
        # X axis
        if key[pygame.K_a]:
            self.__direction.x = -1
        elif key[pygame.K_d]:
            self.__direction.x = 1
        else: self.__direction.x = 0

    def movement(self) -> None:
        """Move the player"""
        velocity = pygame.math.Vector2(
            self.__direction.x * self.__speed,
            self.__direction.y * self.__speed
        )
        key = pygame.key.get_pressed()

        # Diagonal movement
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
    
    def collision(self) -> None:
        # Collisions loop
        for sprite in self.camera.sprites:
            if (sprite.id == "tree" and 
                pygame.Rect.colliderect(self.rect, sprite.rect)):
                # Calculate the distance between the player and the tree
                distance: pygame.math.Vector2 = pygame.math.Vector2(
                    self.rect.centerx - sprite.rect.centerx,
                    self.rect.centery - sprite.rect.centery
                )
                
                # Collision from front (+20 is an offset for cleaner collision)
                if distance.y <= self.__speed + 20 and not distance.y < 0 and self.__direction.y < 0: 
                   self.__direction.y = 0
               
                # Collision from back
                elif distance.y >= -self.__speed and not distance.y > 0 and self.__direction.y > 0:
                   self.__direction.y = 0
    
    def draw_inventory(self, screen):
        pass

    def update(self) -> None:
        """Update the player"""
        self.direction()
        self.collision()
        self.movement()
