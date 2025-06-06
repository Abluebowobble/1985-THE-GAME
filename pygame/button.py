# import module
import pygame

# ------------------------------------------------------------------------------------
# THIS BUTTON WORKS FOR MOSTLY EVERYTHING RELATED TO PRESSING AND CALLING FUNCTIONS
# ------------------------------------------------------------------------------------

class Button:
    """Creates button that can be used throughout the game"""
    def __init__(self, x, y, width, height, text, color, hover_color, text_color, action=None):
        """Initalizes properties"""
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.color = color
        self.hover_color = hover_color
        self.text_color = text_color
        self.action = action 

    def draw(self, screen):
        """Draws button onto screen"""

        # Get the mouse position
        mouse_pos = pygame.mouse.get_pos()

        # Check if the mouse is hovering over the button
        current_color = self.hover_color if self.rect.collidepoint(mouse_pos) else self.color
        pygame.draw.rect(screen, current_color, self.rect)

        # Render the text
        font = pygame.font.Font("fonts/alternate_font.otf", 25)
        text_surface = font.render(self.text, True, self.text_color)
        text_rect = text_surface.get_rect(center=self.rect.center)

        # Draw the text on the button
        screen.blit(text_surface, text_rect)

    def handle_event(self, event):
        """Handles button events"""

        # Check if the button is clicked
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1: 
            if self.rect.collidepoint(event.pos):  
                # If the button is clicked, call the action if it exists
                if self.action:
                    self.action() 
