import pygame
import sys
import state
from button import Button
import sound

def main_menu_buttons(screen, sound_manager):
    # Get the size of the screen
    infoObject = pygame.display.Info()

    # Create buttons
    button_width = 200
    button_height = 50
    button_margin = 20  # Space between buttons
    total_button_height = 4 * button_height + 3 * button_margin  # Total height of all buttons and margins
    button_y_start = infoObject.current_h / 2 - total_button_height / 2  # Start y-position so buttons are centered
    button_texts = ["START", "LOAD", "OPTIONS", "EXIT"]

    buttons = [Button(screen, sound_manager, 50, button_y_start + i * (button_height + button_margin), button_width, button_height, text, r'data\images\buttons\Button_middle_red.png', r'data\images\buttons\Button_middle.png', r'data\images\buttons\Button_middle_Fr.png') for i, text in enumerate(button_texts)]

    return buttons

def main_menu_events(event, buttons):
    # Check for events
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN:
        for button in buttons:
            button.handle_event(event)
    elif event.type == pygame.MOUSEBUTTONUP:
        # Check if the mouse click was within any of the buttons
        for button in buttons:
            if button.button.collidepoint(event.pos):
                if button.text == "START":
                    button.handle_event(event)
                if button.text == "LOAD":
                    button.handle_event(event)
                if button.text == "OPTIONS":
                    button.handle_event(event)
                    return "Options"
                if button.text == "EXIT":
                    button.handle_event(event)
                    pygame.quit()
                    sys.exit()
    return None
    
class MainMenuState():
    def __init__(self, setting, sound_manager):
        self.screen = setting.screen
        self.sound_manager = sound_manager
        # Initialize the main menu here
        # Create buttons
        self.buttons = main_menu_buttons(self.screen, self.sound_manager)

        # Load the background image
        self.background = pygame.image.load(r'data\images\background\Castle.png')

        # Get the size of the screen
        infoObject = pygame.display.Info()

        # Resize the background image
        self.background = pygame.transform.scale(self.background, (infoObject.current_w, infoObject.current_h))

    def handle_event(self, event):
        # Handle events for the main menu here
        new_state = main_menu_events(event, self.buttons)
        return new_state
    
    def update(self):
        # Update the main menu here
        pass

    def draw(self):
        # Draw the background
        self.screen.blit(self.background, (0, 0))

        # Draw the buttons and their text
        for button in self.buttons:
            button.draw()