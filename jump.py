import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('JUMP')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)

sky_surf = pygame.image.load('graphics/Sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()
text_surf = test_font.render('JUMP', False, "Black")

snail_surf = pygame.image.load('graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surf.get_rect(bottomright = (600,300))

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
      
    screen.blit(sky_surf,((screen.get_width()/2-sky_surf.get_width()/2),0))
    screen.blit(ground_surf,(0,300))
    screen.blit(text_surf,(50, 50))
    snail_rect.x -= 4
    if snail_rect.right <=0: snail_rect.left = 800
    screen.blit(snail_surf,snail_rect)
    screen.blit(player_surf,player_rect)

    pygame.display.update()
    clock.tick(60)
