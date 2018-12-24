import pygame

class Ball():

    def __init__(self, settings, screen, x, y, size, init_x_vel, init_y_vel):

        super(Ball, self).__init__()

        self.rect = pygame.Rect((x, y), (size, size))
        self.screen_rect = screen.get_rect()

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.x_vel = init_x_vel
        self.y_vel = init_y_vel
        self.max_speed = 4.9

    def draw_rect(self, settings, screen):
        pygame.draw.rect(screen, settings.item_color, self.rect)

    def update(self, settings, paddles):
        if abs(self.x_vel) > self.max_speed:
            self.x_vel = (self.x_vel / abs(self.x_vel)) * self.max_speed
        if abs(self.y_vel) > self.max_speed:
            self.y_vel = (self.y_vel / abs(self.y_vel)) * self.max_speed
        self.x += self.x_vel
        self.rect.x = self.x
        self.y += self.y_vel
        self.rect.y = self.y

        if self.rect.right > self.screen_rect.right or self.rect.left < self.screen_rect.left or self.rect.top < self.screen_rect.top or self.rect.bottom > self.screen_rect.bottom:
            print(settings.ball_touch_edge)
            settings.ball_touch_edge = True

        self.collide_with_paddles(settings, paddles)

    def collide_with_paddles(self, settings, paddles):
        for paddle in paddles:
            if paddle.rect.collidepoint((self.rect.left, self.rect.bottom - 5)) or paddle.rect.collidepoint((self.rect.left, self.rect.top + 5)):
                self.x = paddle.x + paddle.rect.width + 1
                self.rect.x = self.x
                self.x_vel *= -settings.ball_speedup
                self.y_vel *= settings.ball_speedup
            if paddle.rect.collidepoint((self.rect.right, self.rect.bottom - 5)) or paddle.rect.collidepoint((self.rect.right, self.rect.top + 5)):
                self.x = paddle.x - self.rect.width - 1
                self.rect.x = self.x
                self.x_vel *= -settings.ball_speedup
                self.y_vel *= settings.ball_speedup
            if paddle.rect.collidepoint((self.rect.left + 5, self.rect.top)) or paddle.rect.collidepoint((self.rect.right - 5, self.rect.top)):
                self.y = paddle.y + paddle.rect.height + 1
                self.rect.y = self.y
                self.y_vel *= -settings.ball_speedup
                self.x_vel *= settings.ball_speedup
            if paddle.rect.collidepoint((self.rect.left + 5, self.rect.bottom)) or paddle.rect.collidepoint((self.rect.right - 5, self.rect.bottom)):
                self.y = paddle.y - self.rect.height - 1
                self.rect.y = self.y
                self.y_vel *= -settings.ball_speedup
                self.x_vel *= settings.ball_speedup