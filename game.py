import pygame
import sys
from snake import Snake
from fruit import Fruit
from constants import *

class MainGame:
    def __init__(self):
        self.snake = Snake()
        self.fruit = Fruit()
        self.fruit.randomize(self.snake.body)
        self.key_pressed = False

    def update(self):
        self.snake.move_snake()
        self.check_collision()
        self.check_fail()
        self.check_win()
        self.key_pressed = False

    def draw_elements(self, screen, font):
        self.fruit.draw_fruit(screen)
        self.snake.draw_snake(screen)
        self.draw_score(screen, font)

    def check_collision(self):
        if self.fruit.pos == self.snake.body[0]:
            self.fruit.randomize(self.snake.body)
            self.snake.add_block()

    def check_fail(self):
        head = self.snake.body[0]
        if not 0 <= head.x < CELL_NUMBER or not 0 <= head.y < CELL_NUMBER:
            self.game_over()
        for block in self.snake.body[1:]:
            if block == head:
                self.game_over()

    def check_win(self):
        if len(self.snake.body) >= (CELL_NUMBER * CELL_NUMBER) // 2:
            self.game_win()

    def game_over(self):
        print("Game Over!")
        pygame.quit()
        sys.exit()

    def game_win(self):
        print("You Win!")
        pygame.quit()
        sys.exit()

    def draw_score(self, screen, font):
        score = str(len(self.snake.body) - 3)
        text = font.render(score, True, SCORE_COLOR)
        text_rect = text.get_rect(center=(CELL_SIZE * CELL_NUMBER - 50, CELL_SIZE * CELL_NUMBER - 30))
        screen.blit(text, text_rect)
