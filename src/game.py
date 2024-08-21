import pygame

# Init pygame library
pygame.init()

class Game:
    """
    Game class. Manage window, events and rendering.
    """

    def __init__(
            self, win_size: tuple[int, int], caption: str, icon: pygame.Surface, FPS: int,
            backdrop_color: str
    ) -> None:
        self.__win: pygame.Surface = pygame.display.set_mode(win_size)
        """Variable that contain the surface of the window"""

        # Change the title of the window
        pygame.display.set_caption(caption)

        pygame.display.set_icon(icon)

        self.__clock: pygame.time.Clock = pygame.time.Clock()
        """Frame rate controller. The framerate is 120 fps"""

        self.__fps = FPS
        """Framereate of the game"""

        self.backdrop_color: str = backdrop_color
        """Color of the default background"""

    def __event_loop(self) -> None:
        """
        Loop through all the events and execute the instructions for specefic events.
        For exemple, if the quit event is detected, the program will close.
        """
        for event in pygame.event.get():
            # Quit event
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
    
    def __reset(self) -> None:
        """Reset the game window"""
        backdrop: pygame.Surface = pygame.Surface(self.__win.get_size())
        backdrop.fill()
        self.__win.blit(backdrop, (0,0))
    
    def __draw(self) -> None:
        """Draw all element in the window"""
        # Reset the screen
        self.__reset()
    
    def __update(self) -> None:
        """Update the all element of the window"""
        # Draw element on the window
        self.__draw()

        # Update other element on the screen

        # Update the display
        pygame.display.update()
        # Set the framerate
        self.__clock.tick(self.__fps)
    
    def __game_loop(self) -> None:
        """Main loop of the game"""
        while True:
            # Event loop
            self.__event_loop()

            # Update the screen
            self.__update()
    
    def run(self) -> None:
        """Run the game"""
        self.__game_loop()
