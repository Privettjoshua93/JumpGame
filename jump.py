import pygame
from sys import exit
from random import randint, choice

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        player_walk1 = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
        player_walk2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
        self.player_walk = [player_walk1,player_walk2]
        self.player_index = 0
        self.player_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()
        self.image = self.player_walk[self.player_index]
        self.rect = self.image.get_rect(midbottom = (80,300))
        self.gravity = 0
        self.jump_sound = pygame.mixer.Sound('audio/jump.mp3')
        self.jump_sound.set_volume(0.1)
    def player_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE] and self.rect.bottom >= 300:
            self.gravity = -20
            self.jump_sound.play()
    def apply_gravity(self):
        self.gravity += 1
        self.rect.y += self.gravity
        if self.rect.bottom >= 300:
            self.rect.bottom = 300
    def animation_state(self):
        if self.rect.bottom < 300:
            self.image = self.player_jump
        else:
            self.player_index += 0.1
            if self.player_index >= len(self.player_walk): self.player_index = 0
            self.image = self.player_walk[int(self.player_index)]
    def update(self):
        self.player_input()
        self.apply_gravity()
        self.animation_state()

class Obstacle(pygame.sprite.Sprite):
	def __init__(self,type):
		super().__init__()
		
		if type == 'fly':
			fly_1 = pygame.image.load('graphics/fly/fly1.png').convert_alpha()
			fly_2 = pygame.image.load('graphics/fly/fly2.png').convert_alpha()
			self.frames = [fly_1,fly_2]
			y_pos = 210
		else:
			zuck1 = pygame.image.load('graphics/snail/zuck1.png').convert_alpha()
			zuck2 = pygame.image.load('graphics/snail/zuck2.png').convert_alpha()
			self.frames = [zuck1,zuck2]
			y_pos  = 300

		self.animation_index = 0
		self.image = self.frames[self.animation_index]
		self.rect = self.image.get_rect(midbottom = (randint(900,1100),y_pos))

	def animation_state(self):
		self.animation_index += 0.1 
		if self.animation_index >= len(self.frames): self.animation_index = 0
		self.image = self.frames[int(self.animation_index)]

	def update(self):
		self.animation_state()
		self.rect.x -= 6
		self.destroy()

	def destroy(self):
		if self.rect.x <= -100: 
			self.kill()

def display_score():
    current_time = int((pygame.time.get_ticks() - start_time) / 1000) 
    score_surf = test_font.render(f'Score: {current_time}',False,(64,64,64))
    score_rect = score_surf.get_rect(center = (400,50))
    screen.blit(score_surf,score_rect)
    return current_time

def obstacle_movement(obstacle_list):
    if obstacle_list:
        for obstacle_rect in obstacle_list:
            obstacle_rect.x -= 5
            if obstacle_rect.bottom == 300:
                screen.blit(zuck_surf,obstacle_rect)
            else:
                screen.blit(fly_surf,obstacle_rect)
        obstacle_list = [obstacle for obstacle in obstacle_list if obstacle.x > -100]
        return obstacle_list
    else: return []

def collisions(player,obstacles):
    if obstacles:
        for obstacle_rect in obstacles:
            if player.colliderect(obstacle_rect): return False
    return True

def collision_sprite():
     if pygame.sprite.spritecollide(player.sprite,obstacle_group,False):
          obstacle_group.empty()
          return False
     else: return True

def player_animation():
    global player_surf, player_index
    if player_rect.bottom < 300:
        player_surf = player_jump
    else:
        player_index += 0.1
        if player_index >= len(player_walk): player_index = 0
        player_surf = player_walk[int(player_index)]

def display_title():
    title_surf = test_font.render(f'JUMP THE ZUCK', False, ('Black'))
    title_rect = title_surf.get_rect(center = (130,40))
    screen.blit(title_surf,title_rect)

def display_guide():
    guide_surf = test_font.render(f'Space to jump.', False, 'Black')
    guide_rect = guide_surf.get_rect(center = (130,40))
    screen.blit(guide_surf,guide_rect)
    guide_surf = test_font.render(f'Get Zucked, idiot.-', False, 'Black')
    guide_rect = guide_surf.get_rect(center = (210,155))
    screen.blit(guide_surf,guide_rect)

pygame.init()
screen = pygame.display.set_mode((800,400))
pygame.display.set_caption('JUMP THE ZUCK')
clock = pygame.time.Clock()
test_font = pygame.font.Font('font/Pixeltype.ttf', 50)
game_active = True
start_time = 0
bg_music = pygame.mixer.Sound('audio/music.wav')
bg_music.play(loops = -1)
bg_music.set_volume(0.1)

#Groups
player = pygame.sprite.GroupSingle()
player.add(Player())

obstacle_group = pygame.sprite.Group()


#Obstacles
sky_surf = pygame.image.load('graphics/Sky.png').convert()
ground_surf = pygame.image.load('graphics/ground.png').convert()

#fly
fly1 = pygame.image.load('graphics/Fly/Fly1.png').convert_alpha()
fly2 = pygame.image.load('graphics/Fly/Fly2.png').convert_alpha()
fly_frames = [fly1,fly2]
fly_frame_index = 0
fly_surf = fly_frames[fly_frame_index]

#Zuck
zuck1 = pygame.image.load('graphics/snail/zuck1.png').convert_alpha()
zuck2 = pygame.image.load('graphics/snail/zuck2.png').convert_alpha()
zuck_frames = [zuck1,zuck2]
zuck_frame_index = 0
zuck_surf = zuck_frames[zuck_frame_index]

obstacle_rect_list = []

player_walk1 = pygame.image.load('graphics/player/player_walk_1.png').convert_alpha()
player_walk2 = pygame.image.load('graphics/player/player_walk_2.png').convert_alpha()
player_walk = [player_walk1,player_walk2]
player_index = 0
player_jump = pygame.image.load('graphics/player/jump.png').convert_alpha()
player_surf = player_walk[player_index]
player_rect = player_surf.get_rect(midbottom = (80,300))
player_gravity = 20

#Intro screen
player_stand = pygame.image.load('graphics/snail/bigzuck.png').convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand,0,3)
player_stand_rect = player_stand.get_rect(center = (400,200))

#Timer
obstacle_timer = pygame.USEREVENT = 1
pygame.time.set_timer(obstacle_timer,1500)

zuck_animation_timer = pygame.USEREVENT + 2
pygame.time.set_timer(zuck_animation_timer,500)

fly_animation_timer = pygame.USEREVENT + 3
pygame.time.set_timer(fly_animation_timer,200)

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
                start_time = pygame.time.get_ticks()

        if game_active:    
            if event.type == obstacle_timer:
                obstacle_group.add(Obstacle(choice(['fly','zuck','zuck','zuck'])))
                #if randint(0,2):
                #    obstacle_rect_list.append(zuck_surf.get_rect(bottomright = (randint(900,1100),300)))
                #else:
                #    obstacle_rect_list.append(_surf.get_rect(bottomright = (randint(900,1100),210)))
            if event.type == zuck_animation_timer:
                if zuck_frame_index == 0: zuck_frame_index = 1
                else: zuck_frame_index = 0
                zuck_surf = zuck_frames[zuck_frame_index]
            if event.type == fly_animation_timer:
                if fly_frame_index == 0: fly_frame_index = 1
                else: fly_frame_index = 0
                fly_surf = fly_frames[fly_frame_index]

    if game_active:      
        screen.blit(sky_surf,((screen.get_width()/2-sky_surf.get_width()/2),0))
        screen.blit(ground_surf,(0,300))
        score = display_score()
        display_title()

        #zuck_rect.x -= 4
        #if zuck_rect.right <=0: zuck_rect.left = 800
        #screen.blit(zuck_surf,zuck_rect)

        #player
        #player_gravity += 1
        #player_rect.y = (player_rect.y + player_gravity)
        #if player_rect.bottom >= 300: player_rect.bottom = 300
        #player_animation()
        #screen.blit(player_surf,player_rect)
        player.draw(screen)
        player.update()

        obstacle_group.draw(screen)
        obstacle_group.update()

        #Obstacle movement
        #obstacle_rect_list = obstacle_movement(obstacle_rect_list)

        #collision
        game_active = collision_sprite()
        #game_active = collisions(player_rect,obstacle_rect_list)

    else:
        screen.fill((84,129,162))
        screen.blit(player_stand,player_stand_rect)
        obstacle_rect_list.clear()
        player_rect.midbottom = (80,300)
        player_gravity = 0
        score_message = test_font.render(f'Your score: {score}', False, ('Black'))
        score_message_rect = score_message.get_rect(center = (670, 40))
        screen.blit(score_message,score_message_rect)
        display_guide()
        
    pygame.display.update()
    clock.tick(60)
