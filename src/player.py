import pygame as pg

class Player:
    def __init__(self, health: int = 100,) -> None:
        self.screen: pg.Surface = pg.display.get_surface()
        self.health: int = 100

        # Display and collision
        self.rect: pg.Rect = pg.Rect(0, 0, 20, 20)

        #self.width: int = 20 
        #self.height: int = 20

        # Spatial variables
        self.direction: pg.Vector2 = pg.Vector2(0, 0)
        self.velocity: pg.Vector2 = pg.Vector2(0, 0)
        self.position: pg.Vector2 = pg.Vector2(0, 0)

        # TODO: verifier si c good pour le rouquin
        self.acceleration: float = 1.53
        self.deceleration: float = 0.82
        self.max_speed: float = 17.0
    
    def update_direction(self) -> None:
        key = pg.key.get_pressed()

        # Y axis direction
        if key[pg.K_w]:
            self.direction.y = -1
        elif key[pg.K_s]:
            self.direction.y = 1
        else: 
            self.direction.y = 0
        
        # X axis direction
        if key[pg.K_a]:
            self.direction.x = -1
        elif key[pg.K_d]:
            self.direction.x = 1
        else: 
            self.direction.x = 0
        
        # Normalize the direction for a lenght of 1 (bybass the diagonal bug)
        if self.direction.length() != 0: self.direction = self.direction.normalize()
    
    def update_velocity(self) -> None:
        # Acceleration
        self.velocity.x += self.acceleration * self.direction.x
        self.velocity.y += self.acceleration * self.direction.y

        # Deceleration
        self.velocity.x *= self.deceleration
        self.velocity.y *= self.deceleration
    
    def update_position(self) -> None:
        self.rect.x += self.velocity.x 
        self.rect.y += self.velocity.y

    def draw(self) -> None:
        pg.draw.rect(self.screen, (255, 255, 255), self.rect)
    
    def update(self) -> None:
        # Update components
        self.update_direction()
        self.update_velocity()
        self.update_position()

        self.draw()
