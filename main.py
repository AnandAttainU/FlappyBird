import pygame
pygame.init()

WIDTH = 550
HEIGHT = 700
COLOR_BLACK = (0, 0, 0)

# Set up the drawing window
screen = pygame.display.set_mode([WIDTH, HEIGHT])

# Run until the user asks to quit
stop = False
while not stop:

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True

    # Fill the background with white
    screen.fill(COLOR_BLACK)

pygame.quit()