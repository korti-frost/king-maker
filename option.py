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
    total_button_width = 4 * button_width + 3 * button_margin  # Total width of all buttons and margins
    button_x_start = infoObject.current_w / 2 - total_button_width / 2 + button_margin # Start x-position so buttons are centered
    total_button_height = 7 * button_height + 6 * button_margin  # Total height of all buttons and margins
    button_y_start = infoObject.current_h / 2 - total_button_height / 2  # Start y-position so buttons are centered

    buttons = [pygame.Rect(button_x_start + i * (button_width + button_margin), button_y_start, button_width, button_height) for i in range(4)]
    button_texts = ["800x600", "1024x768", "1280x720", "1920x1080"]

    # Overlap "FULLSCREEN" with the first button in the horizontal list
    buttons.extend([pygame.Rect(button_x_start, button_y_start + (i+1) * (button_height + button_margin), button_width, button_height) for i in range(3)])
    button_texts.extend(["FULLSCREEN", "APPLY", "RETURN"])

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
            json.dump({
                'screen_size': self.screen_size,
                'fullscreen': self.fullscreen,
                'sound': self.sound
        }, f)

    def load(self):
        # Load the settings from a file
        try:
            with open('settings.json', 'r') as f:
                data = json.load(f)
                self.screen_size = data.get('screen_size', self.screen_size)
                self.fullscreen = data.get('fullscreen', self.fullscreen)
                self.sound = data.get('sound', self.sound)
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
                    if self.button_texts[i] == '800x600':
                        print(f"{self.button_texts[i]} button clicked!")
                        self.settings.screen_size = (800, 600)
                    if self.button_texts[i] == '1024x768':
                        print(f"{self.button_texts[i]} button clicked!")
                        self.settings.screen_size = (1024, 768)
                    if self.button_texts[i] == '1280x720':
                        print(f"{self.button_texts[i]} button clicked!")
                        self.settings.screen_size = (1280, 720)
                    if self.button_texts[i] == '1920x1080':
                        print(f"{self.button_texts[i]} button clicked!")
                        self.settings.screen_size = (1920, 1080)
                    if self.button_texts[i] == 'FULLSCREEN':
                        print(f"{self.button_texts[i]} button clicked!")
                        self.settings.fullscreen = not self.settings.fullscreen
                    if self.button_texts[i] == 'APPLY':
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