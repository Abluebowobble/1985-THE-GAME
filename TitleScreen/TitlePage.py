import pygame
import button

class TitleScreen:
    def __init__(self, screen):
        pygame.init()
        pygame.mixer.init()

        self.screen = screen
        pygame.display.set_caption("tetris")
        self.font = pygame.font.Font("fonts/Tetris.ttf", 30)

        self.current_screen = "title"
        self.play_selected = False

        self.title_entities()

    def title_entities(self):
        self.background_image = pygame.image.load("images/bg_image.jpg").convert()
        self.background = pygame.transform.scale(self.background_image, (self.screen.get_width(), self.screen.get_height()))
        self.screen.blit(self.background, (0, 0))

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
            text="Settings", 
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
        title_font = pygame.font.Font("fonts/Tetris.ttf", 150)
        title_text = title_font.render("TETRIS", True, (255, 255, 255))

        smaller_font = pygame.font.Font("fonts/alternate_font.otf", 40)
        smaller_text = smaller_font.render("Made by people", True, (255, 255, 255))

        self.screen.blit(title_text, (80, 20))
        self.screen.blit(smaller_text, (200, 150))

        self.play_button.draw(self.screen)
        self.exit_button.draw(self.screen)
        self.settings_button.draw(self.screen)

    def title_loop(self):
        clock = pygame.time.Clock()
        keepGoing = True
        while keepGoing:
            clock.tick(30)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keepGoing = False

                if self.current_screen == "title":
                    self.play_button.handle_event(event)
                    self.exit_button.handle_event(event)
                    self.settings_button.handle_event(event)
                elif self.current_screen == "settings":
                    self.back_button.handle_event(event)

            self.title_refresh(True)
            if self.play_selected:
                keepGoing = False

    def title_refresh(self, flip=True):
        self.screen.blit(self.background, (0, 0))

        if self.current_screen == "title":
            self.title_screen()
        elif self.current_screen == "settings":
            self.settings_screen()
        if flip:
            pygame.display.flip()

    def settings_screen(self):
        title_font = pygame.font.Font("fonts/Tetris.ttf", 100)
        self.awaiting_key = None
        title_text = title_font.render("SETTINGS", True, (255, 255, 255))
        self.screen.blit(title_text, (120, 20))
        self.back_button.draw(self.screen)

    def show_title(self):
        self.current_screen = "title"

    def show_settings(self):
        self.current_screen = "settings"

    def start_game(self):
        self.play_selected = True

    def exit_game(self):
        exit()