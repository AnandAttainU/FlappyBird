
import random
from util.constants import Constants
import pathlib
import pygame
import os

class Pipe:
    width = 138
    height = 793
    def __init__(self) -> None:
        self.pipePath = "assets/images/pipe.png"
        self.pipeImage = pygame.image.load(self.pipePath)
        self.pipes = list()

    def draw_pipe(self):
        dy = random.randint(10, 100)
        print(dy)

        pipe_rect = self.pipeImage.get_rect()
        pipe_rect.midbottom = (Constants.WIDTH + Pipe.width, Constants.HEIGHT - Constants.groundHeight + Pipe.height//2 + dy)
        self.pipes.append(pipe_rect)

    def move_pipe(self):
        for pipe in self.pipes:
            pipe.centerx -= 3

    def display(self, screen):
        for pipe in self.pipes:
            screen.blit(self.pipeImage, pipe)
