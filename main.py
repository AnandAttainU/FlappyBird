from entities.pipe import Pipe
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
    pipe = Pipe()

    GRAVITYEVENT = pygame.USEREVENT + 1

    pygame.time.set_timer(pygame.USEREVENT, 150)
    pygame.time.set_timer(GRAVITYEVENT, 80)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.USEREVENT:
                bird.fly_bird()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE or pygame.K_UP:
                    bird.jump()
            if event.type == GRAVITYEVENT:
                bird.applyGravity()
        
        background.display(screen)
        
        bird.display(screen)
        ground.display(screen)
        pipe.display(screen)
        pygame.display.flip()

if __name__ == "__main__":
    run()
