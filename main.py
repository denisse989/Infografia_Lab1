from pickle import TRUE

from numpy import place
import pygame 
from pygame.locals import K_SPACE,K_RETURN
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
        self.backGround: Background =None 
        pygame.init()
     
        self.hearts: Heart =None
        self.screen = pygame.display.set_mode([self.width, self.height])
        self.is_running = False
        # self.sprites es para renderizar
        self.sprites = pygame.sprite.Group()
        # self.enemies es para detectar colisiones
        self.enemies = pygame.sprite.Group()
        self.ADD_ENEMY_EVENT = pygame.USEREVENT + 1
        self.SHOOT_EVENT = pygame.USEREVENT + 2
        self.player: Player = None
        self.clock = pygame.time.Clock()
        self.life=3
        
    def add_background(self, background):
        self.backGround = background
        self.sprites.add(background)
    def add_heart(self, heart):
        self.hearts=heart
        self.sprites.add(heart)
        
    def add_player(self, player):
        self.player = player
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
        
        pygame.time.set_timer(self.ADD_ENEMY_EVENT, 250)
        while self.is_running:
            
            blocks_hit_list= pygame.sprite.spritecollide(self.player, self.enemies,True)
            
            for block in blocks_hit_list:
                if(self.life>1):
                    print("bloque 3")
                    self.life-=1
                    for heart in list_hearts:
                        self.hearts.kill()
                        self.hearts.kill()
                        self.hearts.kill()
                    print(self.life)
                    
                else:
                    self.player.kill()
                    self.is_running = False
                    break
                     
            
        
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.is_running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == K_SPACE:
                        self.player.shoot()
                elif event.type == self.ADD_ENEMY_EVENT:
                    self.add_enemy(Enemy())

            keys = pygame.key.get_pressed()
            self.update(keys)
        
        pygame.quit()


if __name__ == "__main__":
    app = App(SCREEN_WIDTH, SCREEN_HEIGHT)
    app.add_background(Background())
     
    list_hearts.append(Heart(20,20))
    list_hearts.append(Heart(60,20))
    list_hearts.append(Heart(100,20))
    for heart in list_hearts:
        app.add_heart(heart)
    app.add_player(Player())
    app.run()
    