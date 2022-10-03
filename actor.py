import pygame
import random
from pygame.sprite import Sprite
from pygame.locals import K_LEFT, K_RIGHT, RLEACCEL



class Player(Sprite):
    def __init__(self):
        # invocar la inicializacion del padre
        super().__init__()
        
        self.surf = pygame.image.load("assets/principal.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (100, 100))
        self.rect = self.surf.get_rect(center=(
            50,
            570
        ))
        
        self.projectiles = pygame.sprite.Group()
    
    def update(self, keys):
        self.projectiles.update()
        if keys[K_LEFT]:
            self.rect.move_ip(-5,0)
        if keys[K_RIGHT]:
            self.rect.move_ip(5, 0)

    def shoot(self):
        self.projectiles.add(Projectile(self.rect.x, self.rect.y))
        print("shoot!")
            

class Projectile(Sprite):
    def __init__(self, pos_x, pos_y):
        super().__init__()
        self.surf = pygame.image.load("assets/pez.png").convert()
        self.surf.set_colorkey((0,0,0), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (50, 50))
        self.rect = self.surf.get_rect(center=(pos_x+40, pos_y))
        self.speed = 15

    def update(self):
        self.rect.move_ip(0, -self.speed )

class Enemy(Sprite):
    def __init__(self):
        # invocar la inicializacion del padre
        super().__init__()
        # crear una superficie
        self.surf = pygame.image.load("assets/enemy.png").convert()
        self.surf.set_colorkey((0,0,0), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (90, 90))
        
        self.rect = self.surf.get_rect(center=(
            random.randint(0, 750),
            random.randint(0, 30)
        ))
        self.speed = random.randint(2, 8)
        
        

    def update(self):
        self.rect.move_ip(0,self.speed)
        if self.rect.right< 0:
            self.kill()

class Heart(Sprite):
    def __init__(self,pos_x,pos_y):
        # invocar la inicializacion del padre
        super().__init__()
        
        self.surf = pygame.image.load("assets/hearth.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (50, 50))
        self.rect = self.surf.get_rect(center=(
            pos_x,
            pos_y
        ))
    def update(self):
        self.speed = random.randint(2, 6)
        self.rect.move_ip(0,-self.speed)
        if self.rect.right< 0:
            self.kill()
        