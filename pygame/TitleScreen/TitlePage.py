import pygame
import button

class TitleScreen:
    """Creates cool looking Title Screen for our game"""
    def __init__(self, screen):
        """Initializes properties"""
        pygame.init()
        pygame.mixer.init()

        # initalize screen and font
        self.screen = screen
        pygame.display.set_caption("1985")
        self.font = pygame.font.Font("fonts/load_font.ttf", 30)

        # initialize current screen and play state
        self.current_screen = "title"
        self.play_selected = False

        # loads title entities
        self.title_entities()

    def title_entities(self):
        """Initializes all the entities for the title screen"""

        # init background 
        self.background_image = pygame.image.load("images/bg_image.webp").convert()
        self.background = pygame.transform.scale(self.background_image, (self.screen.get_width(), self.screen.get_height()))

        # blit image to background
        self.screen.blit(self.background, (0, 0))

        # initialize buttons
        self.play_button = button.Button(
            x=250, y=340, width=300, height=60, 
            text="Play", 
            color=(0, 128, 0), 
            hover_color=(0, 200, 0), 
            text_color=(255, 255, 255), 
            action=self.start_game
        )

        self.settings_button = button.Button(
            x=250, y=420, width=300, height=60, 
            text="Instructions", 
            color=(100, 100, 100), 
            hover_color=(160, 160, 160), 
            text_color=(255, 255, 255), 
            action=self.show_settings
        )

        self.exit_button = button.Button(
            x=250, y=500, width=300, height=60, 
            text="Exit", 
            color=(128, 0, 0), 
            hover_color=(200, 0, 0), 
            text_color=(255, 255, 255), 
            action=self.exit_game
        )

        self.back_button = button.Button(
            x=250, y=480, width=300, height=60,
            text="Back", 
            color=(0, 128, 255), 
            hover_color=(0, 200, 255),
            text_color=(255, 255, 255), 
            action=self.show_title
        )

    def title_screen(self):
        """Initializes title screen"""

        # init fonts
        title_font = pygame.font.Font("fonts/load_font.ttf", 200)
        title_text = title_font.render("1985", True, (0, 0, 0))
        smaller_font = pygame.font.Font("fonts/alternate_font.otf", 40)
        smaller_text = smaller_font.render("Made by Goldstein", True, (0, 0, 0))

        # blit title text and smaller text
        self.screen.blit(title_text, (230, 10))
        self.screen.blit(smaller_text, (210, 200))

        # draw buttons
        self.play_button.draw(self.screen)
        self.exit_button.draw(self.screen)
        self.settings_button.draw(self.screen)

    def title_loop(self):
        """Init title loop"""

        # initialize clock and keepGoing state
        clock = pygame.time.Clock()
        keepGoing = True

        # while user has not quit
        while keepGoing:
            clock.tick(30)
            
            # control events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keepGoing = False

                # allow buttons to handle events
                if self.current_screen == "title":
                    self.play_button.handle_event(event)
                    self.exit_button.handle_event(event)
                    self.settings_button.handle_event(event)
                elif self.current_screen == "settings":
                    self.back_button.handle_event(event)

            # refresh title page
            self.title_refresh(True)

            # if play button was selected, exit loop
            if self.play_selected:
                keepGoing = False

    def title_refresh(self, flip=True):
        """Refreshes title page"""

        # blit background
        self.screen.blit(self.background, (0, 0))

        # draw current screen
        if self.current_screen == "title":
            self.title_screen()
        elif self.current_screen == "settings":
            self.settings_screen()
        
        # if flip boolean passed to function is True, continuously update display
        if flip:
            pygame.display.flip()

    def settings_screen(self):
        """Initializes settings screen"""
        
        # creates fonts
        title_font = pygame.font.Font("fonts/load_font.ttf", 100)
        title_text = title_font.render("INSTRUCTIONS", True, (255, 255, 255))

        # blit onto screen and draw back button
        self.screen.blit(title_text, (120, 20))
        self.back_button.draw(self.screen)

    def show_title(self):
        """Shows title screen"""
        self.current_screen = "title"

    def show_settings(self):
        """Shows settings screen"""
        self.current_screen = "settings"

    def start_game(self):
        """Starts the game"""
        self.play_selected = True

    def exit_game(self):
        """Exits the game"""
        exit()