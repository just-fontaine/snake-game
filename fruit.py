import random, pygame
from pygame.math import Vector2
from constants import CELL_NUMBER

class Fruit:
    def __init__(self):
        self.randomize([])

    def draw_fruit(self, screen):
        from constants import CELL_SIZE, FOOD_COLOR
        fruit_rect = pygame.Rect(self.pos.x * CELL_SIZE, self.pos.y * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, FOOD_COLOR, fruit_rect)

    def randomize(self, snake_body):
        self.x = random.randint(0, CELL_NUMBER - 1)
        self.y = random.randint(0, CELL_NUMBER - 1)
        self.pos = Vector2(self.x, self.y)
        while self.pos in snake_body:
            self.randomize(snake_body)
