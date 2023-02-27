import pygame

pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set up the font
font = pygame.font.Font(None, 32)

# Set up the initial position
x = 50
y = 50

# Main game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            # Handle arrow key presses
            if event.key == pygame.K_LEFT:
                x -= 10
            elif event.key == pygame.K_RIGHT:
                x += 10
            elif event.key == pygame.K_UP:
                y -= 10
            elif event.key == pygame.K_DOWN:
                y += 10

    # Clear the screen
    screen.fill((255, 255, 255))

    # Draw the text and rectangle
    text = font.render("Press arrow keys to move", True, (0, 0, 0))
    rect = pygame.Rect(x, y, 50, 50)
    pygame.draw.rect(screen, (0, 0, 255), rect)
    screen.blit(text, (10, 10))

    # Update the screen
    pygame.display.update()

# Quit pygame
pygame.quit()
