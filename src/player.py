import pygame

class Player:
    def __init__(self) -> None:
        self.__color: str = "Black"
        self.__width: int = 35
        self.__height: int = 35
        self.__pos_x: float = 0.0
        self.__pos_y: float = 0.0
        self.player_rect = (self.__pos_x, self.__pos_y, self.__width, self.__height)
    
    def movement(self) -> None:
        acceleration: float = 0.5
        vel_x: float = 0
        vel_y: float = 0

        key = pygame.key.get_pressed()
        if key[pygame.K_w]:
            vel_y -= 4.5
        if key[pygame.K_s]:
            vel_y += 4.5
        if key[pygame.K_a]:
            vel_x -= 4.5
        if key[pygame.K_d]:
            vel_x += 4.5

        if key[pygame.K_w] == False and key[pygame.K_s] == False:
            vel_y = vel_y * acceleration
        if key[pygame.K_a] == False and key[pygame.K_d] == False:
            vel_x = vel_x * acceleration
        self.__pos_x += vel_x
        self.__pos_y += vel_y
        self.player_rect = (self.__pos_x, self.__pos_y, self.__width, self.__height)
    
    def draw_player(self, screen) -> None:
        pygame.draw.rect(screen, self.__color, self.player_rect)