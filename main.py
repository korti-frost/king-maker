import pygame
from main_menu import *

pygame.init()

screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)  # Creates a game window of 800x600 pixels
print("test")
main_menu(screen)
print("test2")
pygame.quit()