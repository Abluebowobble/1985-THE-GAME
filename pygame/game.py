# import module
import pygame
from TitleScreen.TitlePage import TitleScreen
from TitleScreen.LoadingScreen import LoadingScreen

class Main:
    def __init__(self):
        # initialize pygame
        pygame.init()

        # display the screen
        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("1985")

        # initialize entities and run loading screen
        self.entities()
        self.run_loading_screen()

        pygame.quit()

    def entities(self):
        """Initializes all the entities for the game"""

        # init background and set as black
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0, 0, 0))

    def run_loading_screen(self):
        """Runs the loading screen"""

        # create and load the loading screen
        loading_screen = LoadingScreen()
        loading_screen.load_screen()

        # transition to the title screen
        self.run_title_screen()

    def transition(self, title_page):
        """Handles the transition from loading screen to title screen"""
        
        # initializes variables
        y = 600
        speed = 30
        clock = pygame.time.Clock()

        # loops while black rectangle is visible on screen
        while y > 0:
            # refresh title page without flipping
            title_page.title_refresh(False) 

            # draw black rectangle on screen
            pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, 800, y))
            pygame.display.flip()

            # decrease y value
            y -= speed
            clock.tick(30)

    def run_title_screen(self):
        """Runs the title screen"""

        # create the title screen
        title_page = TitleScreen(self.screen)

        # transition from loading screen to title screen
        self.transition(title_page)

        # run the title screen loop
        title_page.title_loop()

        # if play button was selected, run the game
        if not title_page.play_selected:
            pygame.quit()
            exit()
        else:
            self.run_game()
            
    def run_game(self):    
        """Runs the main game loop"""    
        self.clock = pygame.time.Clock()
        
        # initializes keepGoing state
        keepGoing = True 

        # creates game loop
        while keepGoing: 
            self.clock.tick(30)
            
            # handle quit events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keepGoing = False
            
            # refresh the screen
            self.screen.blit(self.background, (0, 0))
            pygame.display.flip()

Main()