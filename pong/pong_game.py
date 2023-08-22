import pygame
from pygame.locals import *

# Colors
WHITE = (255, 255, 255)

# Screen dimensions
WIDTH, HEIGHT = 640, 480

# Ball and paddle parameters
ball_speed = 5
paddle_speed = 5


class Pong:
    def __init__(self):
        self.ball = pygame.Rect(WIDTH // 2 - 15, HEIGHT // 2 - 15, 30, 30)
        self.ball_dx = 1
        self.ball_dy = 1

        self.left_paddle = pygame.Rect(10, HEIGHT // 2 - 70, 10, 140)
        self.right_paddle = pygame.Rect(WIDTH - 20, HEIGHT // 2 - 70, 10, 140)

    def move_ball(self):
        self.ball.x += self.ball_dx * ball_speed
        self.ball.y += self.ball_dy * ball_speed

        if self.ball.top <= 0 or self.ball.bottom >= HEIGHT:
            self.ball_dy = -self.ball_dy

        if self.ball.colliderect(self.left_paddle) or self.ball.colliderect(self.right_paddle):
            self.ball_dx = -self.ball_dx

        if self.ball.left <= 0 or self.ball.right >= WIDTH:
            return False
        return True

    def move_ai_paddle(self):
        if self.ball_dx < 0:
            if self.left_paddle.centery < self.ball.centery:
                self.left_paddle.y += paddle_speed
            else:
                self.left_paddle.y -= paddle_speed

    def draw(self, screen):
        screen.fill((0, 0, 0))
        pygame.draw.ellipse(screen, WHITE, self.ball)
        pygame.draw.aaline(screen, WHITE, (WIDTH // 2, 0), (WIDTH // 2, HEIGHT))
        pygame.draw.rect(screen, WHITE, self.left_paddle)
        pygame.draw.rect(screen, WHITE, self.right_paddle)
