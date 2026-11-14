import pygame
from pygame.math import Vector2
from random import randint
from settings.constants import SQUARE_WIDTH,SQUARE_NUMBER,RED

class FRUIT():
    def __init__(self,screen):
        self.screen = screen
        self.x_pos = randint(0,SQUARE_NUMBER - 1)
        self.y_pos = randint(0,SQUARE_NUMBER - 1)
        self.vector = Vector2(self.x_pos,self.y_pos)

    def get_fruit_rect(self):
        x_position = self.vector.x * SQUARE_WIDTH
        y_position = self.vector.y * SQUARE_WIDTH
        fruit_rect = pygame.Rect(x_position,y_position,SQUARE_WIDTH,SQUARE_WIDTH)
        return fruit_rect
    
    def draw_fruit(self):
        rect = self.get_fruit_rect()
        pygame.draw.rect(self.screen,RED,rect)

    def relocalize_fruit(self):
        self.x_pos = randint(0,SQUARE_NUMBER - 1)
        self.y_pos = randint(0,SQUARE_NUMBER - 1)
        self.vector = Vector2(self.x_pos,self.y_pos)
