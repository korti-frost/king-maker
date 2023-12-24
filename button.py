import pygame

class Button():
    def __init__(self, screen, x, y, width, height, text, button_color=(255, 0, 0), text_color=(255, 255, 255)):
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.button = pygame.Rect(self.x, self.y, self.width, self.height)
        self.text = text
        self.button_color = button_color
        self.text_color = text_color
        self.font = pygame.font.Font(None, 32)
        self.render_text()

    def render_text(self):
        self.text_surface = self.font.render(self.text, True, self.text_color)
        self.button_center = (self.x + self.width / 2, self.y + self.height / 2)
        self.text_pos = (self.button_center[0] - self.text_surface.get_width() / 2, self.button_center[1] - self.text_surface.get_height() / 2)

    def draw(self):
        pygame.draw.rect(self.screen, self.button_color, self.button)
        self.screen.blit(self.text_surface, self.text_pos)