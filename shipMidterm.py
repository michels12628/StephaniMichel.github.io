#things to always import when creating a game in pycharm
from vectorMidterm import Vector
import sys
import pygame as pg
from pygame.locals import *

#class ship file

class Ship:
  
  """a class that will be in charge of ship"""
  
def __int__(self, ai_game):
    self.ai_game = ai_game
    self.screen = ai_game.screen
    self.velocity = vector

    self.screen_rect = ai_game.screen.get_rect()
    self.image = pg.image.load('ship.bmp')
    self.rect = self.image.get_rect()
    self.rect.midbottom = self.screen_rect.midbottom

    self.lasers = pg.sprite.Group()
    

def center_ship(self):
    #puts ship at middle of bottom of the screen
    self.rect.midbottom = self.screen_rect.midbottom

def fire(self):
    #incharge of shooting the lasers
    laser = laser(game=self.game)
    self.lasers.add(laser)

def remove_laser(self):
    #removing lasers so they don't take up CPU time and memory
    self.lasers.remove()

def move(self):
    #in charge of how our ship will be moving left and right
    if self.velocity == Vector():
        return
        self.rect.left += self.velocity. x
        self.rect.top += self.velocity.y
        self.ai_game.limit_on_screen(self.rect)

def draw(self):
    #draws objects to screen
   self.screen.blit(self.image, self.rect)

def update(self):
    # keeps new images coming into the screen
    fleet = self.game.fleet
    self.move()
    self.draw()
    #if no more aliens then game will restatrt
    if not fleet.aliens:
        self.ai_game.restart()

