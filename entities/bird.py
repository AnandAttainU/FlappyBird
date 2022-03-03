from util.constants import Constants
import pathlib
import pygame
import os

class Bird:
    width = 276/3
    height = 64
    birdFrame = 0
    def __init__(self) -> None:
        self.birdImagePath = "assets/images/bird.png"
        self.birdImage = pygame.image.load(self.birdImagePath)
        self.dy = 0
        
    def fly_bird(self):
        Bird.birdFrame = (Bird.birdFrame + 1) % 3
    
    def jump(self):
        self.dy -= 60

    def applyGravity(self):
        gravity = 10
        self.dy += gravity
    
    def display(self, screen):
        birdRect = self.birdImage.get_rect()
        x = Constants.WIDTH // 2
        y = Constants.HEIGHT//2 + self.dy
        birdRect.center = x, y
        screen.blit(self.birdImage, birdRect, (Bird.birdFrame * Bird.width, 0, Bird.width, Bird.height))
