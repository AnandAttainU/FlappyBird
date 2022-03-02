from util.constants import Constants
import pathlib
import pygame
import os

class Bird:
    def __init__(self) -> None:
        self.birdImagePath = "assets/images/bird.png"
        self.birdImage = pygame.image.load(self.birdImagePath)
        self.speed = 0
    
    def display(self, screen):
        birdRect = self.birdImage.get_rect()
        birdRect.center = Constants.WIDTH // 2 + self.speed, Constants.HEIGHT//2
        screen.blit(self.birdImage, birdRect)
        self.speed += 2
