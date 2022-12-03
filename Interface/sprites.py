from settings import *
import pygame as pg

class Player(pg.sprite.Sprite):
    def __init__(self, game, x, y, size):
        pg.sprite.Sprite.__init__(self)
        self.game = game
        self.image = pg.Surface((size, size))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.size = size

    def move(self, dx=0, dy=0):
        pass
        #if not self.collide_with_walls(dx, dy):
        #    self.x += dx
        #    self.y += dy

    def collide_with_walls(self, dx=0, dy=0):
        for wall in self.game.walls:
            if wall.x == self.x + dx and wall.y == self.y + dy:
                return True
        return False

    def update(self):
        self.rect.x = self.x * self.size
        self.rect.y = self.y * self.size


class Wall(pg.sprite.Sprite):
    def __init__(self, game, x, y, size, color):
        pg.sprite.Sprite.__init__(self)
        self.size = size
        self.game = game
        self.image = pg.Surface((size, size))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.x = x * size
        self.rect.y = y * size
        self.x = x
        self.y = y

    def update(self):
        pass