import pygame
from pygame.locals import *

# Initialization
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Screen dimensions
WIDTH, HEIGHT = 640, 480

# Create the screen and clock
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')
clock = pygame.time.Clock()

# Define the ball and paddles
ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
ball_dx = 1
ball_dy = 1
ball_speed = 5

left_paddle = pygame.Rect(10, HEIGHT // 2 - 70, 10, 140)
right_paddle = pygame.Rect(WIDTH - 20, HEIGHT // 2 - 70, 10, 140)
paddle_speed = 5


def move_ball():
    global ball_dx, ball_dy
    ball.x += ball_dx * ball_speed
    ball.y += ball_dy * ball_speed

    # Ball collision with top and bottom
    if ball.top <= 0 or ball.bottom >= HEIGHT:
        ball_dy = -ball_dy

    # Ball collision with paddles
    if ball.colliderect(left_paddle) or ball.colliderect(right_paddle):
        ball_dx = -ball_dx

    # Ball out of bounds
    if ball.left <= 0 or ball.right >= WIDTH:
        ball.center = (WIDTH // 2, HEIGHT // 2)
        ball_dx = -ball_dx


def move_paddle():
    keys = pygame.key.get_pressed()
    if keys[K_UP] and right_paddle.top > 0:
        right_paddle.y -= paddle_speed
    if keys[K_DOWN] and right_paddle.bottom < HEIGHT:
        right_paddle.y += paddle_speed
    if keys[K_w] and left_paddle.top > 0:
        left_paddle.y -= paddle_speed
    if keys[K_s] and left_paddle.bottom < HEIGHT:
        left_paddle.y += paddle_speed


# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    screen.fill(BLACK)
    pygame.draw.ellipse(screen, WHITE, ball)
    pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
    pygame.draw.rect(screen, WHITE, left_paddle)
    pygame.draw.rect(screen, WHITE, right_paddle)

    move_ball()
    move_paddle()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
