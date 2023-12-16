import pygame
from main_menu import *

pygame.init()

screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)  # Creates a game window of 800x600 pixels
print("test")

# Main menu
main_menu(screen)

# Main game loop
running = True
while running:
    pass
    
print("test2")
pygame.quit()