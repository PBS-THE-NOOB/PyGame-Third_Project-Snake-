import pygame,sys
from settings.constants import SCREEN_SIZE,CHARCOAL
from Game.game_logic import GAME_LOGIC

pygame.init()
screen = pygame.display.set_mode((SCREEN_SIZE,SCREEN_SIZE))
pygame.display.set_caption('Snake_2D')
clock = pygame.time.Clock()

Game_logic = GAME_LOGIC(screen)
snake_move = pygame.USEREVENT + 1 
pygame.time.set_timer(snake_move,250)
run = True

GAMEACTIVE = True

def game_quit():
    pygame.quit()
    sys.exit()

if __name__ == '__main__' :

    while run:
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                run = False 
            if event.type == snake_move and GAMEACTIVE:
                Game_logic.snake.move_snake()
        if GAMEACTIVE :
            screen.fill(CHARCOAL)

            # Game logics 
            Game_logic.fruit.draw_fruit()
            Game_logic.snake.draw_snake()
            Game_logic.update()

            #Game Ending Logic
            if Game_logic.check_self_collision():
                GAMEACTIVE = False
        else : 
            GAMEACTIVE =  Game_logic.game_over()
            

        pygame.display.update()
        clock.tick(60)

    game_quit()