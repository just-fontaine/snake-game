import pygame, sys
from constants import *
from game import MainGame
from pygame.math import Vector2

def main():
    pygame.init()
    screen = pygame.display.set_mode((CELL_SIZE * CELL_NUMBER, CELL_SIZE * CELL_NUMBER))
    pygame.display.set_caption("Snake Game")
    clock = pygame.time.Clock()
    font = pygame.font.Font(FONT_PATH, 25)

    pygame.time.set_timer(SCREEN_UPDATE, 150)

    main_game = MainGame()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == SCREEN_UPDATE:
                main_game.update()
            if event.type == pygame.KEYDOWN and not main_game.key_pressed:
                main_game.key_pressed = True
                if event.key == pygame.K_UP and main_game.snake.direction.y != 1:
                    main_game.snake.direction = Vector2(0, -1)
                elif event.key == pygame.K_DOWN and main_game.snake.direction.y != -1:
                    main_game.snake.direction = Vector2(0, 1)
                elif event.key == pygame.K_LEFT and main_game.snake.direction.x != 1:
                    main_game.snake.direction = Vector2(-1, 0)
                elif event.key == pygame.K_RIGHT and main_game.snake.direction.x != -1:
                    main_game.snake.direction = Vector2(1, 0)

        screen.fill(BACKGROUND_COLOR)
        main_game.draw_elements(screen, font)
        pygame.display.update()
        clock.tick(60)

if __name__ == "__main__":
    main()
