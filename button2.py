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
        self.sound_manager = sound_manager

        # Create the increase and decrease buttons
        self.increase_button = Button(screen, sound_manager, x + width, y, width, height, "+")
        self.decrease_button = Button(screen, sound_manager, x - width, y, width, height, "-")

        self.button = self.increase_button.button

        # Initialize the text
        self.text = str(self.variable)
        self.text_color = text_color
        self.font = pygame.font.Font(None, 32)
        self.text_surface = self.font.render(self.text, True, self.text_color)

    def handle_event(self, event):
        # Handle the button events and update the variable
        if self.increase_button.button.collidepoint(event.pos) and self.variable < self.max_val:
            self.variable += self.step
            print(self.sound_manager.volume_sounds)
            self.sound_manager.set_sound_volume(self.variable)
        elif self.decrease_button.button.collidepoint(event.pos) and self.variable > self.min_val:
            self.variable -= self.step
            self.sound_manager.set_sound_volume(self.variable)

        # Update the text
        self.text = str(self.variable)
        self.text_surface = self.font.render(self.text, True, self.text_color)

    def draw(self):
        # Draw the buttons and the text
        self.increase_button.draw()
        self.decrease_button.draw()
        self.screen.blit(self.text_surface, (self.x, self.y))


