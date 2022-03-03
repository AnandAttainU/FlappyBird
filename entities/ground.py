from util.constants import Constants
import pathlib
import pygame
import os

class Ground:
    height = 128
    width = 37
    def __init__(self) -> None:
        self.groundImagePath = "assets/images/ground.png"
        self.groundImage = pygame.image.load(self.groundImagePath)
        
        self.images = [self.groundImage.get_rect() for _ in range(Constants.TotalGroundImages)]
        self.positions = list()
        self.create_ground()

    def create_ground(self):
        delta = 0
        for _ in range(Constants.TotalGroundImages):
            x = Ground.width/2 + delta
            y = Constants.HEIGHT - Ground.height/2
            self.positions.append((x, y))
            delta += Ground.width

    def move_ground(self):
        speed = 2
        for i in range(len(self.positions)):
            x, y = self.positions[i]
            if x < 0:
                x = Constants.WIDTH + Ground.width/2
            else:
                x = x - speed
            self.positions[i] = (x, y)
    
    def display(self, screen):
        self.move_ground()
        for i in range(Constants.TotalGroundImages):
            groundRect = self.images[i]
            groundRect.center = self.positions[i]
            screen.blit(self.groundImage, groundRect)
            
