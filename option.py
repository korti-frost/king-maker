import pygame
import json
from button import Button
from button2 import SliderButton

def apply_settings(settings):
    # Apply the settings
    if settings.fullscreen:
        settings.screen = pygame.display.set_mode(settings.screen_size, pygame.FULLSCREEN)
    else:
        settings.screen = pygame.display.set_mode(settings.screen_size)

def option_buttons(screen, sound_manager):
    # Get the size of the screen
    infoObject = pygame.display.Info()

    # Create buttons
    button_width = 120
    button_height = 50
    button_margin = 20  # Space between buttons
    total_button_height = 9 * button_height + 8 * button_margin  # Total height of all buttons and margins
    button_y_start = infoObject.current_h / 2 - total_button_height / 2  # Start y-position so buttons are centered

    explication_texts = ["Screen Size: ", "Fullscreen: "]
    button_texts = ["1920x1080", "FULLSCREEN"]

    # Create the text buttons closer to the middle of the screen
    text_buttons = [Button(screen, sound_manager, infoObject.current_w / 2 - button_width - 50, button_y_start + i * (button_height + button_margin), button_width, button_height, text) for i, text in enumerate(explication_texts)]

    # Create the extra buttons for Screen Size
    extra_button_texts = ["840x600", "1024x768", "1280x720"]
    extra_buttons = [Button(screen, sound_manager, infoObject.current_w / 2 + 50 + (j+1) * (button_width + button_margin), button_y_start, button_width, button_height, text, r'data\images\buttons\Button_middle_red.png', r'data\images\buttons\Button_middle.png', r'data\images\buttons\Button_middle_Fr.png') for j, text in enumerate(extra_button_texts)]

    # Create the actual buttons closer to the middle of the screen
    buttons = [Button(screen, sound_manager, infoObject.current_w / 2 + 50, button_y_start + i * (button_height + button_margin), button_width, button_height, text, r'data\images\buttons\Button_middle_red.png', r'data\images\buttons\Button_middle.png', r'data\images\buttons\Button_middle_Fr.png') for i, text in enumerate(button_texts)]
    
    # Create the Sound Slider Button
    sound_slider_button = SliderButton(screen, sound_manager, infoObject.current_w / 2 + 50, button_y_start + len(button_texts) * (button_height + button_margin), button_width, button_height, sound_manager.volume_sounds, 0, 1, 0.1)
    buttons.append(sound_slider_button)

    # Create the Apply and Return buttons at the bottom of the screen
    bottom_button_texts = ["APPLY", "RETURN"]
    bottom_buttons = [Button(screen, sound_manager, infoObject.current_w / 2 - button_width - 50 if text == "APPLY" else infoObject.current_w / 2 + 50, infoObject.current_h - button_height - 50, button_width, button_height, text, r'data\images\buttons\Button_middle_red.png', r'data\images\buttons\Button_middle.png', r'data\images\buttons\Button_middle_Fr.png') for text in bottom_button_texts]

    # Add the extra buttons and the bottom buttons to the buttons list
    buttons.extend(extra_buttons)
    buttons.extend(bottom_buttons)

    # Add the text buttons and the actual buttons to the same list
    buttons.extend(text_buttons)

    return buttons

class Settings:
    def __init__(self):
        self.screen = None
        self.screen_size = (840, 600)  # Default screen size
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
    def __init__(self, settings, sound_manager):
        self.settings = settings
        self.sound_manager = sound_manager
        # Initialize buttons, etc.
        self.buttons= option_buttons(self.settings.screen, self.sound_manager)

        # Load the background image
        self.background = pygame.image.load(r'data\images\background\Settings_desk.png')

        # Get the size of the screen
        infoObject = pygame.display.Info()

        # Resize the background image
        self.background = pygame.transform.scale(self.background, (infoObject.current_w, infoObject.current_h))


    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            for button in self.buttons:
                button.handle_event(event)
        elif event.type == pygame.MOUSEBUTTONUP:
            # Check if the mouse click was within any of the buttons
            for button in self.buttons:
                if button.button.collidepoint(event.pos):
                    # Change the corresponding setting
                    if button.text == '840x600': 
                        self.settings.screen_size = (840, 600)
                    if button.text == '1024x768':  
                        self.settings.screen_size = (1024, 768)
                    if button.text == '1280x720':  
                        self.settings.screen_size = (1280, 720)
                    if button.text == '1920x1080':  
                        self.settings.screen_size = (1920, 1080)
                    if button.text == 'FULLSCREEN':   
                        self.settings.fullscreen = not self.settings.fullscreen
                    if button.text == 'APPLY':
                        apply_settings(self.settings)
                        # Save the settings
                        self.settings.save()
                        # Update the screen
                        pygame.display.flip()
                        self.draw()
                    if button.text == 'RETURN':
                        return "MainMenu"
                    
    def update(self):
        # Update option here
        pass
    
    def draw(self):
        # Draw the background
        self.settings.screen.blit(self.background, (0, 0))

        # Draw the buttons and their text
        for button in self.buttons:
            button.draw()