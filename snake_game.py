import pygame
import random
import sys

pygame.init()

# Screen
WIDTH = 600
HEIGHT = 400
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Snake
size = 20
x = 100
y = 100
dx = 0
dy = 0
speed = 10

snake_body = []
length = 1

# Food
food_x = random.randrange(0, WIDTH, size)
food_y = random.randrange(0, HEIGHT, size)

# Score
score = 0
font = pygame.font.SysFont(None, 35)

clock = pygame.time.Clock()

running = True
while running:

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                dx = -speed
                dy = 0
            elif event.key == pygame.K_RIGHT:
                dx = speed
                dy = 0
            elif event.key == pygame.K_UP:
                dx = 0
                dy = -speed
            elif event.key == pygame.K_DOWN:
                dx = 0
                dy = speed

    # Move Snake
    x += dx
    y += dy

    # Game Over (Wall Collision)
    if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT:
        running = False

    # Snake Body
    head = [x, y]
    snake_body.append(head)

    if len(snake_body) > length:
        del snake_body[0]

    # Self Collision
    if head in snake_body[:-1]:
        running = False

    # Food Collision
    if x == food_x and y == food_y:
        food_x = random.randrange(0, WIDTH, size)
        food_y = random.randrange(0, HEIGHT, size)
        score += 1
        length += 1

    # Draw
    screen.fill(WHITE)

    pygame.draw.rect(screen, RED, (food_x, food_y, size, size))

    for block in snake_body:
        pygame.draw.rect(screen, GREEN, (block[0], block[1], size, size))

    text = font.render("Score: " + str(score), True, BLACK)
    screen.blit(text, (10, 10))

    pygame.display.update()
    clock.tick(10)

# Game Over Screen
screen.fill(WHITE)
game_over = font.render("Game Over! Score: " + str(score), True, RED)
screen.blit(game_over, (120, 180))
pygame.display.update()

pygame.time.wait(3000)

pygame.quit()
sys.exit()