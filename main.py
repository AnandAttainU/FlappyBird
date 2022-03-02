from entities.ground import Ground
from entities.bird import Bird
import sys
from entities.background import Background
from util.constants import Constants
import pygame

def run():
    pygame.init()
    screen = pygame.display.set_mode([Constants.WIDTH, Constants.HEIGHT])

    background = Background()
    bird = Bird()
    ground = Ground()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        
        background.display(screen)
        bird.display(screen)
        ground.display(screen)
        pygame.display.flip()

if __name__ == "__main__":
    run()
