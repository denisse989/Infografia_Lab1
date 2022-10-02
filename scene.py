import pygame
from pygame.sprite import Sprite
from pygame.locals import K_LEFT, K_RIGHT, RLEACCEL

class Background(Sprite):
    def __init__(self):
        super().__init__()  #call Sprite initializer
        self.surf = pygame.image.load("assets/fondo1.png").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.surf = pygame.transform.scale(self.surf, (600, 600))
        self.rect = self.surf.get_rect()
        #self.rect.left, self.rect.top = [0,0]
   
class Background2(Sprite):
    def __init__(self):
        super().__init__()  #call Sprite initializer
        self.surf = pygame.image.load("assets/fondo.jpg").convert()
        self.surf.set_colorkey((255, 255, 255), RLEACCEL)
        self.rect = self.surf.get_rect()
        self.rect.left, self.rect.top = [0,0]