import pygame

class LoadingScreen:
    def __init__(self):
        pygame.init()
        pygame.mixer.init()

        self.screen = pygame.display.set_mode((800, 600))
        pygame.display.set_caption("tetris")
        self.font = pygame.font.Font("fonts/load_Font.ttf", 160)
        self.message = self.font.render("BIG BROTHER IS", True, (255, 255, 255))
        self.message2 = self.font.render("WATCHING  YOU", True, (255, 255, 255))

        self.current_screen = "title"
        self.show_message = True
        self.done = False
        self.flash_interval = 250
        self.flash_duration = 2000

    def load_screen(self):
        clock = pygame.time.Clock()
        start_time = pygame.time.get_ticks()
        last_flash_time = start_time

        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()

            current_time = pygame.time.get_ticks()

            if current_time - start_time < self.flash_duration:
                if current_time - last_flash_time >= self.flash_interval:
                    self.show_message = not self.show_message
                    last_flash_time = current_time
            else:
                self.show_message = False
                self.done = True

            self.screen.fill((0, 0, 0)) 
            
            if self.show_message:
                self.screen.blit(self.message, (40, 130))
                self.screen.blit(self.message2, (40, 250))

            pygame.display.flip()
            clock.tick(30)