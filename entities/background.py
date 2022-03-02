from util.constants import Constants
import pathlib
import pygame
import os

class Background:
    def __init__(self) -> None:
        self.backgroundImagePath = "assets/images/background.png"
        self.backgroundImage = pygame.image.load(self.backgroundImagePath)
        self.backgroundImage = pygame.transform.scale(self.backgroundImage, (Constants.WIDTH, Constants.HEIGHT))
    
    def display(self, screen):
        screen.blit(self.backgroundImage, self.backgroundImage.get_rect())
