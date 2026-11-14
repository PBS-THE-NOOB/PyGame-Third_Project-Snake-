import pygame
from pygame.math import Vector2
from settings.constants import SQUARE_WIDTH,SQUARE_NUMBER,GREEN

class SNAKE():
    def __init__(self,screen):
        self.screen = screen
        self.position = [Vector2(5,3),Vector2(6,3),Vector2(7,3)] #initial snake position
        self.right = Vector2(1,0)
        self.up = Vector2(0,-1)
        self.direction = self.right

    def draw_snake(self):
        for i in self.position :
            rect = pygame.Rect(i.x * SQUARE_WIDTH,i.y * SQUARE_WIDTH,SQUARE_WIDTH,SQUARE_WIDTH)
            pygame.draw.rect(self.screen,GREEN,rect)
    
    def movement_handeling(self):
        keys =  pygame.key.get_pressed()
        if keys[pygame.K_a] and self.direction != self.right: 
            self.direction = -self.right
        elif keys[pygame.K_d] and self.direction != -self.right:
            self.direction = self.right
        elif keys[pygame.K_w] and self.direction != -self.up:
            self.direction = self.up
        elif keys[pygame.K_s] and self.direction != self.up:
            self.direction = -self.up
            

    def move_snake(self):
        self.movement_handeling()
    
        head = self.position[0] + self.direction
        self.position.insert(0,head) 
        self.position.pop()


    def update(self):
        pass
        