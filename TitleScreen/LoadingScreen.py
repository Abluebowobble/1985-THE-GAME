import pygame

class LoadingScreen:
    """A loading screen that displays a message for a specified duration before transitioning to the title screen."""
    def __init__(self):
        """Initializes the loading screen with necessary properties and settings."""
        pygame.init()
        pygame.mixer.init()

        # Initialize screen and font
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("1985")
        self.font = pygame.font.Font("fonts/load_Font.ttf", 160)
        self.message = self.font.render("BIG BROTHER IS", True, (255, 255, 255))
        self.message2 = self.font.render("WATCHING  YOU", True, (255, 255, 255))

        # Initialize variables
        self.current_screen = "title"
        self.show_message = True
        self.done = False
        self.flash_interval = 250
        self.flash_duration = 2000

    def load_screen(self):
        """Displays the loading screen with a flashing message for a specified duration."""

        # initialize variables
        clock = pygame.time.Clock()
        start_time = pygame.time.get_ticks()
        last_flash_time = start_time

        # Main loop for the loading screen
        while not self.done:
            # handle events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            # get current time
            current_time = pygame.time.get_ticks()

            # check if message has finished flashing
            if current_time - start_time < self.flash_duration:
                
                # check if it's time to toggle the message visibility
                if current_time - last_flash_time >= self.flash_interval:
                    self.show_message = not self.show_message
                    last_flash_time = current_time
            
            # if not, finish displaying message and update variables
            else:
                self.show_message = False
                self.done = True

            # fill the screen with black
            self.screen.fill((0, 0, 0)) 
            
            # draw message according to show_message state
            if self.show_message:
                self.screen.blit(self.message, (40, 130))
                self.screen.blit(self.message2, (40, 250))

            pygame.display.flip()
            clock.tick(30)