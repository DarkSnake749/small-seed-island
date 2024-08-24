import pygame
from config import *
from camera import Camera
from items import Apple

class Player:
    def __init__(self, camera: Camera) -> None:

        self.id: str = "player"
        """Identification of the player"""

        self.camera: Camera = camera
        """Can cycle through all the element of the window. Useful for collision"""

        self.apple: Apple = Apple()

        # Paramters
        self.__color: str = Player_config.COLOR
        self.__width: int = Player_config.WIDTH
        self.__height: int = Player_config.HEIGTH
        self.__acceleration: float = Player_config.ACCELERATION
        self.__speed: float = Player_config.SPEED
        self.__direction: pygame.math.Vector2 = pygame.math.Vector2(0, 0)
        self.inventory = [["", "", "", "", ""], 
                          ["", "", "", "", ""], 
                          ["", "", "", "", ""],
                          ["", "", "", "", ""]]

        #state of the player
        self.inventory_state: bool = False

        # Image of the player
        self.image: pygame.Surface = pygame.Surface((self.__width, self.__height))
        self.image.fill(self.__color)
        # Player collider
        self.rect: pygame.Rect = self.image.get_rect(center = (Game_config.WIDTH/2, Game_config.HEIGHT/2))
    
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
        self.collision("horizontal")
        self.rect.y += velocity.y
        self.collision("vertical")
    
    def collision(self, axis: str) -> None:
        # Collisions loop
        for sprite in self.camera.sprites:
            if (sprite.id == "tree" and 
                pygame.Rect.colliderect(self.rect, sprite.hitbox)):
                if axis == "horizontal":
                    # Left collision
                    if self.__direction.x > 0:
                        self.rect.right = sprite.hitbox.left
                    
                     # Right collision
                    if self.__direction.x < 0:
                        self.rect.left = sprite.hitbox.right
                
                if axis == "vertical":
                    # Left collision
                    if self.__direction.y > 0:
                        self.rect.bottom = sprite.hitbox.top
                    
                     # Right collision
                    if self.__direction.y < 0:
                        self.rect.top = sprite.hitbox.bottom
    
    def draw_inventory(self, screen):
        pygame.draw.rect(screen, (200, 200, 200), ((Game_config.WIDTH / 2) - (524 / 2), (Game_config.HEIGHT / 2) - (360 / 2), 524, 360))
        for i in range(len(self.inventory)):
            for j in range(len(self.inventory[i])):
                if self.inventory[i][j] != "":
                    pygame.draw.rect(screen, self.inventory[i][j].color, ((Game_config.WIDTH / 2) - (524 / 2) + 32, 
                                                                          (Game_config.HEIGHT / 2) - (360 / 2) + 32, 50, 50))
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if self.inventory_state == True:
                    if event.key == pygame.K_e:
                        self.inventory_state = False

    def update(self) -> None:
        """Update the player"""
        self.direction()
        self.movement()
