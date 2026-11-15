import pygame
from Game.snake import SNAKE
from Game.fruit import FRUIT
from settings.constants import BLUE,SCREEN_SIZE,WINE_RED,CRIMSON

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

    def check_self_collision(self):
        if self.snake.position[0] in self.snake.position[1:] :
            return True
        return False

    def game_over(self):
            self.screen.fill(CRIMSON)
            surf = self.text_font.render('GAME OVER',0,WINE_RED)
            surf = pygame.transform.scale(surf,(surf.get_width() * 2 , surf.get_height() * 2))
            rect = surf.get_rect(center = (SCREEN_SIZE//2,SCREEN_SIZE//2))
            self.screen.blit(surf,rect)
            self.display_score()
            enter_surf = self.text_font.render('Enter to continue next game',0,WINE_RED)
            enter_rect = enter_surf.get_rect(midtop = (rect.midbottom))
            self.screen.blit(enter_surf,enter_rect)
            return self.check_enter()
        
    def check_enter(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN] :
            self.reset()
            return True
        return False
    
    def reset(self):
        self.fruit.reset()
        self.snake.reset()
        self.score = 0

    def update(self):
        self.check_collision()
        self.display_score()
