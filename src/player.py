class Player:
    def __init__(self):
        self.color: str = "Black"
        self.__width: int = 35
        self.__height: int = 35
        self.__pos_x: float = 0.0
        self.__pos_y: float = 0.0
        self.__speed: int = 5
    
    def movement(self):
        pass