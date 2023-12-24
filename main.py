import pygame
from main_menu import *
import main_menu
from state import *
import state
from option import *
import option
from sound import *

def change_state(state_manager, new_state):
    if new_state == "Options":
        state_manager.set_state(option.OptionState(settings))
    elif new_state == "MainMenu":
        state_manager.set_state(main_menu.MainMenuState(settings.screen))

# Initialize Pygame
pygame.init()

# Create the settings object, load the settings, and apply them
settings = Settings()
settings.load()
apply_settings(settings)

# Create the sound manager and load the sounds
sound_manager = SoundManager()

# Create the state manager and set the initial state to MainMenuState
state_manager = StateManager()
state_manager.set_state(main_menu.MainMenuState(settings.screen))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            new_state = state_manager.handle_event(event)

    # Check if the state should be changed
    if new_state is not None:
        print(f"Changing state to {new_state}")
        change_state(state_manager, new_state)
        new_state = None

    state_manager.update()
    state_manager.draw()

    pygame.display.flip()

pygame.quit()