import pygame, sys, os
from sniffer_class import Sniffer

# initializing the game 
pygame.init()

# game setup 
fps = 30
fpsclock = pygame.time.Clock()
background_green = (144, 238, 144)
sniffer_speed = 3

# display
pygame.display.set_caption("Sniffer")
pygame.display.set_icon(pygame.image.load(os.path.join("images", "sniffer_front.png")))
window_size = window_width, window_height = 640*2, 480*2
game_window = pygame.display.set_mode(window_size)

# Sniffer
sniffer = Sniffer(window_width/2, window_height/2)
sprite_group = pygame.sprite.Group()
sprite_group.add(sniffer)

# main game loop 
render = True
while render:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            render = False
            pygame.quit()
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
    
    # rendering the elements 
    fpsclock.tick(fps)
    game_window.fill(background_green)
    sprite_group.draw(game_window)
    pygame.display.flip() # there's also update