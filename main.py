import pygame
from main_menu import *
import main_menu
from state import *
import state

# Initialize Pygame and create a window
pygame.init()
screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)

# Create the state manager and set the initial state to MainMenuState
state_manager = StateManager()
state_manager.set_state(main_menu.MainMenuState(screen))

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        else:
            state_manager.handle_event(event)

    state_manager.update()
    state_manager.draw()

    pygame.display.flip()

pygame.quit()