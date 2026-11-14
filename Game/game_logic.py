import pygame
from Game.snake import SNAKE
from Game.fruit import FRUIT
from settings.constants import BLUE,SCREEN_SIZE

class GAME_LOGIC() : 
    def __init__(self,screen):
        self.screen = screen
        self.snake = SNAKE(screen)
        self.fruit = FRUIT(screen)
        self.score = 0
        self.text_font = pygame.font.Font(None,45)

    def check_collision(self):
        if self.snake.position[0]  == self.fruit.vector : 
            self.snake.position.append(self.snake.delete)
            self.score += 1
            self.fruit.relocalize_fruit()

    def display_score(self) :
        surface = self.text_font.render(f'Score : {self.score}',0,BLUE)
        rect = surface.get_rect(topright = (SCREEN_SIZE,0))
        self.screen.blit(surface,rect)

    def update(self):
        self.check_collision()
        self.display_score()