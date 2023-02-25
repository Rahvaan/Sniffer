import pygame, sys, os
from sniffer_class import Sniffer
pygame.init()
pygame.display.set_caption("Sniffer")

size = width, height = 640*2, 480*2
green = 144, 238, 144
fpsclock = pygame.time.Clock()
screen = pygame.display.set_mode(size)

surface = pygame.display.get_surface()
x, y = surface.get_width(), surface.get_height()

sniffer = Sniffer(x/2, y/2)

sprite_group = pygame.sprite.Group()
sprite_group.add(sniffer)

sniffer_speed = 3

render = True
while render:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            render = False
            sys.exit()
    

    keys = pygame.key.get_pressed()
    
    if keys[pygame.K_LEFT]:
        sniffer.rect.x -= sniffer_speed
    if keys[pygame.K_RIGHT]:
        sniffer.rect.x += sniffer_speed
    #todo: change to jump
    if keys[pygame.K_UP]:
        sniffer.rect.y -= sniffer_speed
    if keys[pygame.K_DOWN]:
        sniffer.rect.y += sniffer_speed
    else:
        sniffer.walk = False
    
    
    fpsclock.tick(30)
    screen.fill(green)
    sprite_group.draw(screen)
    pygame.display.flip()
