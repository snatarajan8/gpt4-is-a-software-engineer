import pygame
from pygame.locals import *
import pong_game
import highscores

pygame.init()

WIDTH, HEIGHT = 640, 480
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Pong')

font = pygame.font.Font(None, 36)


def game_loop(single_player=True):
    game = pong_game.Pong()
    clock = pygame.time.Clock()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        game.move_ball()

        keys = pygame.key.get_pressed()
        if keys[K_UP]:
            game.right_paddle.y -= pong_game.paddle_speed
        if keys[K_DOWN]:
            game.right_paddle.y += pong_game.paddle_speed

        if single_player:
            game.move_ai_paddle()
        else:
            if keys[K_w]:
                game.left_paddle.y -= pong_game.paddle_speed
            if keys[K_s]:
                game.left_paddle.y += pong_game.paddle_speed

        game.draw(screen)
        pygame.display.flip()
        clock.tick(60)


def landing_screen():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False

        # Render text and buttons
        text = font.render('Welcome to Pong!', True, (255, 255, 255))
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, 50))

        # And so on for other buttons and screens...
        # You can use mouse events to detect button clicks.

        pygame.display.flip()


landing_screen()
pygame.quit()
