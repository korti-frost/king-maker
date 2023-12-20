import pygame
import state
import json

def apply_settings(settings):
    # Apply the settings
    if settings.fullscreen:
        settings.screen = pygame.display.set_mode(settings.screen_size, pygame.FULLSCREEN)
    else:
        settings.screen = pygame.display.set_mode(settings.screen_size)

def option_draw(screen, buttons, button_texts):
    # Draw the background
    screen.fill((0, 0, 0))

    # Create a font object
    font = pygame.font.Font(None, 32)  # You can adjust the size as needed

    # Draw the buttons and their text
    for i, button in enumerate(buttons):
        pygame.draw.rect(screen, (255, 0, 0), button)

        # Render the text
        text_surface = font.render(button_texts[i], True, (255, 255, 255))  # White text

        # Get the center of the button
        button_center = (button.x + button.width / 2, button.y + button.height / 2)

        # Get the top-left position of the text surface so it's centered on the button
        text_pos = (button_center[0] - text_surface.get_width() / 2, button_center[1] - text_surface.get_height() / 2)

        # Draw the text on the screen
        screen.blit(text_surface, text_pos)

def option_buttons():
    # Get the size of the screen
    infoObject = pygame.display.Info()

    # Create buttons
    button_width = 200
    button_height = 50
    button_margin = 20  # Space between buttons
    total_button_height = 4 * button_height + 3 * button_margin  # Total height of all buttons and margins
    button_y_start = infoObject.current_h / 2 - total_button_height / 2  # Start y-position so buttons are centered
    buttons = [pygame.Rect(20, button_y_start + i * (button_height + button_margin), button_width, button_height) for i in range(3)]
    button_texts = ["FULLSCREEN", "SAVE", "RETURN"]

    return buttons, button_texts

class Settings:
    def __init__(self):
        self.screen = None
        self.screen_size = (800, 600)  # Default screen size
        self.fullscreen = False
        self.sound = True

    def save(self):
        # Save the settings to a file
        with open('settings.json', 'w') as f:
            json.dump(self.__dict__, f)

    def load(self):
        # Load the settings from a file
        try:
            with open('settings.json', 'r') as f:
                self.__dict__ = json.load(f)
        except FileNotFoundError:
            pass  # If the settings file doesn't exist, just use the default settings

class OptionState(Settings):
    def __init__(self, settings):
        self.settings = settings
        # Initialize buttons, etc.
        self.buttons, self.button_texts = option_buttons()

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse click was within any of the buttons
            for i, button in enumerate(self.buttons):
                if button.collidepoint(event.pos):
                    # Change the corresponding setting
                    if self.button_texts[i] == 'FULLSCREEN':
                        print(f"{self.button_texts[i]} button clicked!")
                        self.settings.fullscreen = not self.settings.fullscreen
                    if self.button_texts[i] == 'SAVE':
                        print(f"{self.button_texts[i]} button clicked!")
                        apply_settings(self.settings)
                        # Save the settings
                        self.settings.save()
                    if self.button_texts[i] == 'RETURN':
                        print(f"{self.button_texts[i]} button clicked!")
                        return "MainMenu"

    def update(self):
        # Update option here
        pass
    
    def draw(self):
        # Draw option here
        option_draw(self.settings.screen, self.buttons, self.button_texts)