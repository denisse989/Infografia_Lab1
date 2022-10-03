from os import remove
from pickle import TRUE

from numpy import place
import pygame 
from pygame.locals import K_SPACE,K_RETURN,K_UP
import random
from actor import *
from scene import *

# configuraciones
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
list_hearts = [] 

class App:
    def __init__(self, screen_width, screen_height):
        self.width = screen_width
        self.height = screen_height
        #self.bg_color = bg_color
        
        pygame.init()
        pygame.display.set_caption('GHOST INVASION')
        pygame.mixer.music.load("assets/it.mp3")
        pygame.mixer.music.set_volume(0.2)
        self.musica=pygame.mixer.music.play(0,0)
        self.logo = pygame.image.load("assets/icon.png")
        pygame.display.set_icon(self.logo)
        self.backGround: Background =None
        self.backGround2: Background2 =None
        self.hearts: Heart =None
        self.hearts_black: Heart_Black =None
        self.screen = pygame.display.set_mode([self.width, self.height])
        self.is_running = False
        # self.sprites es para renderizar
        self.sprites = pygame.sprite.Group()
        # self.enemies es para detectar colisiones
        self.enemies = pygame.sprite.Group()
        self.ADD_ENEMY_EVENT = pygame.USEREVENT + 1
        self.SHOOT_EVENT = pygame.USEREVENT + 2
        self.player: Player = None
        self.player_dead: Player_dead = None
        self.clock = pygame.time.Clock()
        self.life=3
        
    def add_background(self, background):
        self.backGround = background
        self.sprites.add(background)
        
    def add_background2(self, background):
        self.backGround2 = background
        self.sprites.add(background)
        
    def add_heart(self, heart):
        self.hearts=heart
        self.sprites.add(heart)
    def add_heart_black(self, heart):
        self.hearts_black=heart
        self.sprites.add(heart)
        
    def add_player(self, player):
        self.player = player
        self.sprites.add(player)
    def add_player_dead(self, player):
        self.player_dead = player
        self.sprites.add(player)
        
    def add_enemy(self, enemy):
        self.enemies.add(enemy)
        self.sprites.add(enemy)
        

    def update(self, keys):
        # self.screen.blit(self.backGround.surf, self.backGround.rect)   
        
        self.screen.blit(self.player.surf, self.player.rect)
        self.player.update(keys)
       
        # sprite group
        self.enemies.update()
        
        # dibujar todos los sprites
        for sprite in self.sprites:
             self.screen.blit(sprite.surf, sprite.rect)
        
         
        # dibujar proyectiles
        for projectile in self.player.projectiles:
            self.screen.blit(projectile.surf, projectile.rect)
              
        # detectar colisiones entre el player y enemies
        colisiones= pygame.sprite.spritecollide(self.player, self.enemies,True)
            
        for colision in colisiones:
            if(self.life>1):
                print("bloque 3")
                self.life-=1
                if(self.life==2):
                    self.add_heart_black(Heart_Black(100,20))
                    self.screen.blit(self.hearts_black.surf, (100,20))
                if(self.life==1):
                    self.add_heart_black(Heart_Black(60,20))
                    self.screen.blit(self.hearts_black.surf, (60,20))
                    
                print(self.life) 
            elif self.life==1:
                self.life-=1
                self.add_heart_black(Heart_Black(20,20))
                self.screen.blit(self.hearts_black.surf, (20,20))
                self.player.kill()
                
            else:    
                self.add_background2(Background2())
                pygame.mixer.music.stop()
                #self.screen.blit(self.player_dead.surf, self.player_dead.rect)
                self.add_player_dead(Player_dead())
                break
                #self.player_dead.update(keys)
                #self.is_running = False
            
        # detectar colisiones entre proyectiles y enemies
        pygame.sprite.groupcollide(
            self.player.projectiles,    # primer sprite group
            self.enemies,               # segundo sprite group
            True,                       # True = invocar kill() si sprites del grupo 1 colisionan
            True                        # igual que arriba pero para el 2do grupo
            )
        pygame.display.flip()
        # para mantener 30 frames por segundo
        self.clock.tick(30)
        
    def run(self):
        
        self.is_running = True
        
        pygame.time.set_timer(self.ADD_ENEMY_EVENT, 350)
        while self.is_running:
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                if event.type == pygame.KEYDOWN: 
                    if event.key == K_SPACE:
                        self.player.shoot()
                        
                    if event.key == K_UP:
                        keys = pygame.key.get_pressed()
                        self.player_dead.move(keys)
                elif event.type == self.ADD_ENEMY_EVENT:
                    self.add_enemy(Enemy())
            keys = pygame.key.get_pressed()        
            
        
            
            self.update(keys)
            
        
        pygame.quit()


if __name__ == "__main__":
    app = App(SCREEN_WIDTH, SCREEN_HEIGHT)
    app.add_background(Background())
    app.add_heart(Heart(20,20))
    app.add_heart(Heart(60,20))
    app.add_heart(Heart(100,20))
    app.add_player(Player())
    app.run()
    