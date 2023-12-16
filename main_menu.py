import pygame

def main_menu_buttons():
    # Get the size of the screen
    infoObject = pygame.display.Info()

    # Create buttons
    button_width = 200
    button_height = 50
    button_margin = 20  # Space between buttons
    total_button_height = 4 * button_height + 3 * button_margin  # Total height of all buttons and margins
    button_y_start = infoObject.current_h / 2 - total_button_height / 2  # Start y-position so buttons are centered
    buttons = [pygame.Rect(20, button_y_start + i * (button_height + button_margin), button_width, button_height) for i in range(4)]
    button_texts = ["START", "LOAD", "OPTIONS", "EXIT"]

    return buttons, button_texts

def main_menu_events(screen, buttons, button_texts):
    # Check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return False, screen, buttons, button_texts
        elif event.type == pygame.VIDEORESIZE:
            # Window has been resized, so update the display surface to match the new size
            screen = pygame.display.set_mode((event.w, event.h), pygame.RESIZABLE)
            buttons, button_texts = main_menu_buttons()
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # Check if the mouse click was within any of the buttons
            for i, button in enumerate(buttons):
                if button.collidepoint(event.pos):
                    print(f"{button_texts[i]} button clicked!")
    return True, screen, buttons, button_texts

def main_menu_draw(screen, buttons, button_texts):
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

    pygame.display.flip()  # Update the display

def main_menu(screen):
    # Create buttons
    buttons, button_texts = main_menu_buttons()

    # Main menu loop
    running = True
    while running:

        # Check for events
        running, screen, buttons, button_texts = main_menu_events(screen, buttons, button_texts)

        # Draw the background and buttons
        main_menu_draw(screen, buttons, button_texts)