import sys
import pygame
import time

def check_events(paddles):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event, paddles)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event, paddles)

def check_keydown_events(event, paddles):
    for paddle in paddles:
        if event.key == pygame.K_q:
            sys.exit()
        if event.key == pygame.K_LEFT:
            paddle.move_left = True
        if event.key == pygame.K_RIGHT:
            paddle.move_right = True
        if event.key == pygame.K_UP:
            paddle.move_up = True
        if event.key == pygame.K_DOWN:
            paddle.move_down = True
        if event.key == pygame.K_q:
            sys.exit()

def check_keyup_events(event, paddles):
    for paddle in paddles:
        if event.key == pygame.K_LEFT:
            paddle.move_left = False
        if event.key == pygame.K_RIGHT:
            paddle.move_right = False
        if event.key == pygame.K_UP:
            paddle.move_up = False
        if event.key == pygame.K_DOWN:
            paddle.move_down = False

def update(settings, screen, paddles, balls):
    for ball in balls:
        ball.update(settings, paddles)
        for paddle in paddles:
            paddle.update(ball)

def update_screen(settings, screen, paddles, balls, line):
    screen.fill(settings.bg_color)
    for rectangle in line:
        pygame.draw.rect(screen, settings.item_color, rectangle)
    for paddle in paddles:
        paddle.draw_rect(settings, screen)
    for ball in balls:
        ball.draw_rect(settings, screen)
    pygame.display.flip()
