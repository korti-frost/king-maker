import pygame

class Button():
    def __init__(self, screen, x, y, width, height, text, image_path=None, image_path_clicked=None, image_path_frame=None, button_color=(255, 0, 0), text_color=(255, 255, 255)):
        # Initialize the button
        self.screen = screen
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        # Create the button and text
        self.button = pygame.Rect(self.x, self.y, self.width, self.height)
        self.text = text
        self.button_color = button_color
        self.text_color = text_color
        self.font = pygame.font.Font(None, 32)
        self.render_text()

        # Load the button images if provided
        if image_path is not None:
            self.image = pygame.image.load(image_path)
            self.image = pygame.transform.scale(self.image, (self.width, self.height))
        else:
            self.image = None

        if image_path_clicked is not None:
            self.image_clicked = pygame.image.load(image_path_clicked)
            self.image_clicked = pygame.transform.scale(self.image_clicked, (self.width, self.height))
        else:
            self.image_clicked = None

        if image_path_frame is not None:
            self.image_frame = pygame.image.load(image_path_frame)
            self.image_frame = pygame.transform.scale(self.image_frame, (self.width, self.height))
        else:
            self.image_frame = None

        # Initialize the click state
        self.clicked = False

    def render_text(self):
        # Render the text
        self.text_surface = self.font.render(self.text, True, self.text_color)
        self.button_center = (self.x + self.width / 2, self.y + self.height / 2)
        self.text_pos = (self.button_center[0] - self.text_surface.get_width() / 2, self.button_center[1] - self.text_surface.get_height() / 2)

    def handle_event(self, event):
        # Check if the button was clicked
        print(f"{self.text} button clicked!")
        if event.type == pygame.MOUSEBUTTONDOWN and self.button.collidepoint(pygame.mouse.get_pos()):
            self.clicked = True
        else:
            self.clicked = False

    def draw(self):
        # Draw the button
        if self.clicked and self.image_clicked is not None:
            self.screen.blit(self.image_clicked, (self.x, self.y))
        elif self.image is not None:
            self.screen.blit(self.image, (self.x, self.y))
        else:
            pygame.draw.rect(self.screen, self.button_color, self.button)

        # Draw the frame
        if self.image_frame is not None:
            self.screen.blit(self.image_frame, (self.x, self.y))

        # Draw the text
        self.screen.blit(self.text_surface, self.text_surface.get_rect(center=self.button_center))
