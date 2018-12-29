import sys
import pygame
import game_functions as gf
import random
from game_settings import Settings
from paddles import Paddle
from ball import Ball

def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode((settings.screen_width, settings.screen_height))

    paddles = []
    paddles.append(Paddle(settings, screen, 0, settings.screen_height / 2 - settings.paddle_long / 2, settings.paddle_short, settings.paddle_long, True, True, False))
    paddles.append(Paddle(settings, screen, settings.screen_width - settings.paddle_short, settings.screen_height / 2 - settings.paddle_long / 2, settings.paddle_short, settings.paddle_long, False, True, True))
    paddles.append(Paddle(settings, screen, settings.screen_width / 4 - settings.paddle_long / 2, 0, settings.paddle_long, settings.paddle_short, True, False, False))
    paddles.append(Paddle(settings, screen, (settings.screen_width / 4) * 3 - settings.paddle_long / 2, 0, settings.paddle_long, settings.paddle_short, False, False, True))
    paddles.append(Paddle(settings, screen, settings.screen_width / 4 - settings.paddle_long / 2, settings.screen_height - settings.paddle_short, settings.paddle_long, settings.paddle_short, True, False, False))
    paddles.append(Paddle(settings, screen, (settings.screen_width / 4) * 3 - settings.paddle_long / 2, settings.screen_height - settings.paddle_short, settings.paddle_long, settings.paddle_short, False, False, True))

    random_position = random.randint(int(settings.screen_height / 3), int((2 * settings.screen_height) / 3))
    init_x_vel = random.choice([-2, -1, 1, 2])
    init_y_vel = random.choice([-2, -1, 1, 2])

    balls = []
    balls.append(Ball(settings, screen, settings.screen_width / 2 - settings.ball_size / 2, random_position, settings.ball_size, init_x_vel, init_y_vel))
    
    line = []
    line.append(pygame.Rect((settings.screen_width / 2 - 4, 25), (8, 50)))
    line.append(pygame.Rect((settings.screen_width / 2 - 4, 125), (8, 50)))
    line.append(pygame.Rect((settings.screen_width / 2 - 4, 225), (8, 50)))
    line.append(pygame.Rect((settings.screen_width / 2 - 4, 325), (8, 50)))
    line.append(pygame.Rect((settings.screen_width / 2 - 4, 425), (8, 50)))
    line.append(pygame.Rect((settings.screen_width / 2 - 4, 525), (8, 50)))
    line.append(pygame.Rect((settings.screen_width / 2 - 4, 625), (8, 50)))
    line.append(pygame.Rect((settings.screen_width / 2 - 4, 725), (8, 50)))
    
    clock = pygame.time.Clock()

    while True:
        if settings.ball_touch_edge:
            for ball in balls:
                balls.remove(ball)
            random_position = random.randint(int(settings.screen_height / 3), int((2 * settings.screen_height) / 3))
            init_x_vel = random.choice([-2, -1, 1, 2])
            init_y_vel = random.choice([-2, -1, 1, 2])
            balls.append(Ball(settings, screen, settings.screen_width / 2 - settings.ball_size / 2, random_position, settings.ball_size, init_x_vel, init_y_vel))
            settings.ball_touch_edge = False
        gf.check_events(paddles)
        gf.update(settings, screen, paddles, balls)
        gf.update_screen(settings, screen, paddles, balls, line)
        clock.tick(75)

run_game()