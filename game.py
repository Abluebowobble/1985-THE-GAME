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
        pygame.display.set_caption("tetris")

        self.entities()

        self.run_loading_screen()

        pygame.quit()

    def entities(self):
        self.background = pygame.Surface(self.screen.get_size())
        self.background = self.background.convert()
        self.background.fill((0, 0, 0))

    def run_loading_screen(self):
        loading_screen = LoadingScreen()
        loading_screen.load_screen()
        self.run_title_screen()

    def transition(self, title_page):
        y = 600
        speed = 20
        clock = pygame.time.Clock()

        while y > 0:
            title_page.title_refresh(False) 
            pygame.draw.rect(self.screen, (0, 0, 0), (0, 0, 800, y))
            pygame.display.flip()
            y -= speed
            clock.tick(30)

    def run_title_screen(self):
        title_page = TitleScreen(self.screen)
        self.transition(title_page)
        title_page.title_loop()
        if not title_page.play_selected:
            pygame.quit()
            exit()
        else:
            self.run_game()
            
    def run_game(self):        
        self.clock = pygame.time.Clock()
        
        keepGoing = True 
        while keepGoing: 

            self.clock.tick(30)
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    keepGoing = False
            
            self.screen.blit(self.background, (0, 0))
            pygame.display.flip()

Main()