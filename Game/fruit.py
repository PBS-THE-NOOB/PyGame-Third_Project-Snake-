import pygame
from pygame.math import Vector2
from random import randint
from settings.constants import SQUARE_WIDTH,SCREEN_SIZE,RED

class FRUIT():
    def __init__(self,screen):
        self.screen = screen
        self.x_pos = randint(0,SCREEN_SIZE - 1)
        self.y_pos = randint(0,SCREEN_SIZE - 1)
        self.vector = Vector2(self.x_pos,self.y_pos)

    def get_fruit_rect(self):
        fruit_rect = pygame.Rect(self.vector.x,self.vector.y,SQUARE_WIDTH,SQUARE_WIDTH)
        return fruit_rect
    
    def draw_fruit(self):
        rect = self.get_fruit_rect()
        pygame.draw.rect(self.screen,RED,rect)
