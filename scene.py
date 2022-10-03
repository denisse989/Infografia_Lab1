
import pygame
from pygame.sprite import Sprite
from pygame.locals import K_LEFT, K_RIGHT, RLEACCEL,K_UP

class Background(Sprite):
    def __init__(self):
        super().__init__()  #call Sprite initializer
        self.surf = pygame.image.load("assets/fondo1.png").convert()
        self.surf.set_colorkey((0,0,0), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (600, 600))
        self.rect = self.surf.get_rect()
        #self.rect.left, self.rect.top = [0,0]
   
class Background2(Sprite):
    def __init__(self):
        super().__init__()  #call Sprite initializer
        self.surf = pygame.image.load("assets/fondo2.png").convert()
        #self.surf.set_colorkey((0,0,0), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (600, 600))
        self.rect = self.surf.get_rect()
        self.rect.left, self.rect.top = [0,0]
        
class Heart_Black(Sprite):
    def __init__(self,pos_x,pos_y):
        # invocar la inicializacion del padre
        super().__init__()
        
        self.surf = pygame.image.load("assets/hearth_negro.png").convert()
        self.surf.set_colorkey((0,0,0), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (50, 50))
        self.rect = self.surf.get_rect(center=(
            pos_x,
            pos_y
        ))
class Player_dead(Sprite):
    def __init__(self):
        # invocar la inicializacion del padre
        super().__init__()
        
        self.surf = pygame.image.load("assets/principal_dead.png").convert()
        self.surf.set_colorkey((255, 0, 0), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (100, 100))
        self.rect = self.surf.get_rect(center=(
            270,
            450
        ))
        
    def move(self,keys):   
        if keys[K_UP]:
            self.rect.move_ip(0,-50)
        if self.rect.y==0:
            self.kill()