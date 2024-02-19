import pygame
from sys import exit

def display_score():
    current_time = int((pygame.time.get_ticks() - start_time) / 1000) 
    score_surf = test_font.render(f'Score: {current_time}',False,(64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)
    return current_time

def display_title():
    title_surf = test_font.render(f'JUMP THE ZUCK', False, ('Black'))
    title_rect = title_surf.get_rect(center = (130,40))
    screen.blit(title_surf,title_rect)

def display_guide():
    guide_surf = test_font.render(f'Space to jump.', False, 'Black')
    guide_rect = guide_surf.get_rect(center = (130,40))
    screen.blit(guide_surf,guide_rect)

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('JUMP THE ZUCK')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = True
start_time = 0

sky_surf = pygame.image.load('graphics/Sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()

zuck_surf = pygame.image.load('graphics/snail/zuck1.png').convert_alpha()
zuck_rect = zuck_surf.get_rect(bottomright = (600,300))

player_surf = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 20

#Intro screen
player_stand = pygame.image.load('graphics/snail/bigzuck.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,3)
player_stand_rect = player_stand.get_rect(center = (400,200))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        
        if game_active:
            if event.type == pygame.MOUSEBUTTONDOWN:
                if player_rect.collidepoint(event.pos):
                        if player_rect.bottom == 300:
                            player_gravity = -20

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if player_rect.bottom == 300:
                        player_gravity = -20    

        else:
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                game_active = True
                zuck_rect.left = 800
                start_time = pygame.time.get_ticks()  
            
    if game_active:      
        screen.blit(sky_surf,((screen.get_width()/2-sky_surf.get_width()/2),0))
        screen.blit(ground_surf,(0,300))
        score = display_score()
        display_title()

        zuck_rect.x -= 4
        if zuck_rect.right <=0: zuck_rect.left = 800
        screen.blit(zuck_surf,zuck_rect)

        #player
        player_gravity += 1
        player_rect.y = (player_rect.y + player_gravity)
        if player_rect.bottom >= 300: player_rect.bottom = 300
        screen.blit(player_surf,player_rect)

        #collision and end the game
        if zuck_rect.colliderect(player_rect):
            game_active = False
    else:
        screen.fill((84,129,162))
        screen.blit(player_stand,player_stand_rect)
        score_message = test_font.render(f'Your score: {score}', False, ('Black'))
        score_message_rect = score_message.get_rect(center = (670, 40))
        screen.blit(score_message,score_message_rect)
        display_guide()
        
    pygame.display.update()
    clock.tick(60)
