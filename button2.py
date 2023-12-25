import pygame
from button import Button

class SliderButton():
    def __init__(self, screen, sound_manager, x, y, width, height, variable, min_val, max_val, step, text_color=(255, 255, 255)):
        self.screen = screen
        self.variable = variable
        self.min_val = min_val
        self.max_val = max_val
        self.step = step
        self.x = x
        self.y = y

        # Create the increase and decrease buttons
        self.increase_button = Button(screen, sound_manager, x + width, y, width, height, "+")
        self.decrease_button = Button(screen, sound_manager, x - width, y, width, height, "-")

        # Initialize the text
        self.text = str(self.variable)
        self.text_color = text_color
        self.font = pygame.font.Font(None, 32)
        self.text_surface = self.font.render(self.text, True, self.text_color)

    def handle_event(self, event):
        # Handle the button events and update the variable
        if self.increase_button.handle_event(event) and self.variable < self.max_val:
            self.variable += self.step
        elif self.decrease_button.handle_event(event) and self.variable > self.min_val:
            self.variable -= self.step

        # Update the text
        self.text = str(self.variable)
        self.text_surface = self.font.render(self.text, True, self.text_color)

    def draw(self):
        # Draw the buttons and the text
        self.increase_button.draw()
        self.decrease_button.draw()
        self.screen.blit(self.text_surface, (self.x, self.y))