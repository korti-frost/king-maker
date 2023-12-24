import pygame
import sys
import state
from button import Button

def main_menu_buttons(screen):
    # Get the size of the screen
    infoObject = pygame.display.Info()

    # Create buttons
    button_width = 200
    button_height = 50
    button_margin = 20  # Space between buttons
    total_button_height = 4 * button_height + 3 * button_margin  # Total height of all buttons and margins
    button_y_start = infoObject.current_h / 2 - total_button_height / 2  # Start y-position so buttons are centered
    button_texts = ["START", "LOAD", "OPTIONS", "EXIT"]

    buttons = [Button(screen, 20, button_y_start + i * (button_height + button_margin), button_width, button_height, text) for i, text in enumerate(button_texts)]

    return buttons

def main_menu_events(event, buttons):
    # Check for events
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    elif event.type == pygame.MOUSEBUTTONDOWN:
        # Check if the mouse click was within any of the buttons
        for button in buttons:
            if button.button.collidepoint(event.pos):
                print(f"{button.text} button clicked!")
                if button.text == "OPTIONS":
                    return "Options"
                if button.text == "EXIT":
                    pygame.quit()
                    sys.exit()
    return None
    
class MainMenuState(state.State):
    def __init__(self, screen):
        self.screen = screen
        # Initialize the main menu here
        # Create buttons
        self.buttons = main_menu_buttons(screen)

    def handle_event(self, event):
        # Handle events for the main menu here
        new_state = main_menu_events(event, self.buttons)
        return new_state
    
    def draw(self):
        # Draw the background
        self.screen.fill((0, 0, 0))

        # Draw the buttons and their text
        for button in self.buttons:
            button.draw()