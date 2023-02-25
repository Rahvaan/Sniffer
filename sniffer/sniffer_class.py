import pygame
import os


class Sniffer(pygame.sprite.Sprite):
    
    def __init__(self, pos_x, pos_y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("sniffer_sprite/sniffer_front.png")
        self.rect = self.image.get_rect()
        self.rect.center = [pos_x, pos_y]
        self.walking = False
        self.vel = 0
        
    def walk(self):
        self.walking = True
        
    def update(self):
        if self.walking == True:
            pass