import sys
import pygame
import time

def check_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown_events(event)
        elif event.type == pygame.KEYUP:
            check_keyup_events(event)

def check_keydown_events(event):
    if event.key == pygame.K_q:
        sys.exit()

def check_keyup_events(event):
    True

def update(settings, screen, paddles, balls):
    for ball in balls:
        ball.update(settings, paddles)
        for paddle in paddles:
            paddle.update(ball)

def update_screen(settings, screen, paddles, balls):
    screen.fill(settings.bg_color)
    for paddle in paddles:
        paddle.draw_rect(settings, screen)
    for ball in balls:
        ball.draw_rect(settings, screen)
    pygame.display.flip()
