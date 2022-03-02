from util.constants import Constants
import pygame

pygame.init()

screen = pygame.display.set_mode([Constants.WIDTH, Constants.HEIGHT])

backgroundImagePath = "assets/images/background.png"
backgroundImage = pygame.image.load(backgroundImagePath)

stop = False
while not stop:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            stop = True
    
    screen.blit(backgroundImage, backgroundImage.get_rect())
    pygame.display.flip()

pygame.quit()