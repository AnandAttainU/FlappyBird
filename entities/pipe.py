from util.constants import Constants
import pathlib
import pygame
import os

class Pipe:
    def __init__(self) -> None:
        self.pipePath = "assets/images/pipe.png"
        self.pipeImage = pygame.image.load(self.pipePath)
    
    def display(self, screen):
        screen.blit(self.pipeImage, self.pipeImage.get_rect())
