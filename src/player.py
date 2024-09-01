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
        self.inventory: list[list] = [
            ["", "", "", "", ""], 
            ["", "", "", "", ""], 
            ["", "", "", "", ""],
            ["", "", "", "", ""]
        ]

        #state of the player
        self.inventory_state: bool = False

        # Image of the player
        self.image: pygame.Surface = pygame.Surface((self.__width, self.__height))
        self.image.fill(self.__color)
        # Player collider
        self.rect: pygame.Rect = self.image.get_rect(center = (Game_config.WIDTH/2, Game_config.HEIGHT/2))
        # Hitbox
        self.hitbox: pygame.Rect = self.rect.copy().inflate(-17.5, -17.5)
    
    def direction(self) -> None:
        # Listen for inputs
        key: pygame.key.ScancodeWrapper = pygame.key.get_pressed()
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

        # Diagonal movement TODO
        if self.__direction.x and self.__direction.y:
            velocity.x /= (2**0.22239242) # I know what you're thinking. But This value is the right one I swear to god. Seriously, I'm not joking
            velocity.y /= (2**0.22239242)

        # Add acceleration 
        velocity.y *= self.__acceleration
        velocity.x *= self.__acceleration

        # Update position
        self.rect.x += velocity.x
        self.hitbox.centerx = self.rect.centerx
        self.collision("horizontal")
        self.rect.y += velocity.y
        self.hitbox.centery = self.rect.centery
        self.collision("vertical")
    
    def collision(self, axis: str) -> None:
        # Collisions loop
        for sprite in self.camera.sprites:
            if (
                sprite.id == "tree" and 
                pygame.Rect.colliderect(self.hitbox, sprite.hitbox)
            ):
                if axis == "horizontal":
                    # Left collision
                    if self.__direction.x > 0:
                        self.hitbox.right = sprite.hitbox.left
                        self.rect.centerx = self.hitbox.centerx
                        self.rect.centery = self.hitbox.centery
                    
                     # Right collision
                    if self.__direction.x < 0:
                        self.hitbox.left = sprite.hitbox.right
                        self.rect.centerx = self.hitbox.centerx
                        self.rect.centery = self.hitbox.centery
                
                if axis == "vertical":
                    # Left collision
                    if self.__direction.y > 0:
                        self.hitbox.bottom = sprite.hitbox.top
                        self.rect.centerx = self.hitbox.centerx
                        self.rect.centery = self.hitbox.centery
                    
                     # Right collision
                    if self.__direction.y < 0:
                        self.hitbox.top = sprite.hitbox.bottom
                        self.rect.centerx = self.hitbox.centerx
                        self.rect.centery = self.hitbox.centery

    def interaction(self) -> None: 
        keys: pygame.key.ScancodeWrapper = pygame.key.get_pressed()
        for sprite in self.camera.sprites:
            if (
                sprite.id.startswith("npc") and 
                pygame.Rect.colliderect(self.hitbox, sprite.area) and
                keys[pygame.K_e]
            ):
                print(True)
    
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
                    if event.key == pygame.K_ESCAPE:
                        self.inventory_state = False

    def update(self) -> None:
        """Update the player"""
        self.direction()
        if not self.inventory_state:
            self.interaction() 
            self.movement()
