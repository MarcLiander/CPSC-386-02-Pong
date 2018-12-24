import pygame

class Paddle():

    def __init__(self, settings, screen, x, y, width, height, is_player_controlled, is_vertical, right_side):

        super(Paddle, self).__init__()

        self.rect = pygame.Rect((x, y), (width, height))
        self.screen_rect = screen.get_rect()

        self.player_control = is_player_controlled
        self.is_vertical = is_vertical
        self.right_side = right_side

        self.x = float(self.rect.x)
        self.y = float(self.rect.y)

        self.x_vel = 0
        self.y_vel = 0
        self.max_speed = 3.5

    def draw_rect(self, settings, screen):
        pygame.draw.rect(screen, settings.item_color, self.rect)

    def update(self, ball):
        if self.player_control:
            True
        else:
            if self.is_vertical:
                if self.rect.top < self.screen_rect.top:
                    self.y = 1
                    self.rect.y = self.y
                    self.y_vel = 0
                elif self.rect.bottom > self.screen_rect.bottom:
                    self.y = self.screen_rect.height - self.rect.height - 1
                    self.rect.y = self.y
                    self.y_vel = 0
                elif abs(self.y_vel) < self.max_speed:
                    if self.rect.centery <= ball.rect.centery:
                        if ball.y_vel > 0:
                            self.y_vel = ball.y_vel
                        else:
                            self.y_vel = -ball.y_vel
                    else:
                        if ball.y_vel > 0:
                            self.y_vel = -ball.y_vel
                        else:
                            self.y_vel = ball.y_vel
                else:
                    if self.rect.centery <= ball.rect.centery:
                        self.y_vel = self.max_speed
                    else:
                        self.y_vel = -self.max_speed
            else:
                if self.right_side:
                    if self.rect.left < self.screen_rect.width / 2:
                        self.x = (self.screen_rect.width / 2)
                        self.rect.x = self.x
                        self.x_vel = 0
                    elif self.rect.right > self.screen_rect.right:
                        self.x = self.screen_rect.right - self.rect.width
                        self.rect.x = self.x
                        self.x_vel = 0
                    elif abs(self.x_vel) < self.max_speed:
                        if self.rect.centerx <= ball.rect.centerx and self.rect.right != self.screen_rect.right:
                            if ball.x_vel > 0:
                                self.x_vel = ball.x_vel
                            else:
                                self.x_vel = -ball.x_vel
                        elif self.rect.left != self.screen_rect.width / 2:
                            if ball.x_vel > 0:
                                self.x_vel = -ball.x_vel
                            else:
                                self.x_vel = ball.x_vel
                    else:
                        if self.rect.centerx <= ball.rect.centerx:
                            self.x_vel = self.max_speed
                        else:
                            self.x_vel = -self.max_speed
                else:
                    if self.rect.right > self.screen_rect.width / 2:
                        self.x = (self.screen_rect.width / 2) - self.rect.width
                        self.rect.x = self.x
                        print(self.rect.x)
                        self.x_vel = 0
                    elif self.rect.left < self.screen_rect.left:
                        self.x = 0
                        self.rect.x = self.x
                        self.x_vel = 0
                    elif abs(self.x_vel) < self.max_speed:
                        print(self.rect.x)
                        if self.rect.centerx <= ball.rect.centerx and self.rect.right != self.screen_rect.centerx:
                            if ball.x_vel > 0:
                                self.x_vel = ball.x_vel
                            else:
                                self.x_vel = -ball.x_vel
                        elif self.rect.left != self.screen_rect.left:
                            if ball.x_vel > 0:
                                self.x_vel = -ball.x_vel
                            else:
                                self.x_vel = ball.x_vel
                    else:
                        if self.rect.centerx <= ball.rect.centerx:
                            self.x_vel = self.max_speed
                        else:
                            self.x_vel = -self.max_speed

        self.x += self.x_vel
        self.rect.x = self.x
        self.y += self.y_vel
        self.rect.y = self.y