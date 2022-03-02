from util.constants import Constants
import pathlib
import pygame
import os

class Ground:
    def __init__(self) -> None:
        self.groundImagePath = "assets/images/ground.png"
        self.groundImage = pygame.image.load(self.groundImagePath)
        self.groundImageHeight = 128
        self.groundImageWidth = 37
        self.images = [pygame.image.load(self.groundImagePath) for _ in range(Constants.TotalGroundImages)]
    
    def display(self, screen):
        count = 0
        for i in range(Constants.TotalGroundImages):
            groundRect = self.images[i].get_rect()
            groundRect.centery = groundRect.centery + Constants.HEIGHT - self.groundImageHeight
            groundRect.centerx = self.groundImageWidth + count
            screen.blit(self.images[i], groundRect)
            count += self.groundImageWidth
