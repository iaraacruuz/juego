import pygame
from class_personaje import *
from pygame.rect import Rect
class Item(pygame.sprite.Sprite):
    def __init__(self, image, x,y):
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
    def draw(self, surface):
        surface.blit(self.image, self.rect)

    def check_collision(self,mi_personaje: Personaje): 

        return self.rect.colliderect(mi_personaje)

    
    def obtener_rectangulos(self, principal: pygame.Rect) -> dict:
        diccionario = {}
        diccionario["main"] = principal
        diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom - 10, principal.width, 10)
        diccionario["right"] = pygame.Rect(principal.right - 2, principal.top, 2, principal.height)
        diccionario["left"] = pygame.Rect(principal.left, principal.top, 2, principal.height)
        diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 10)
        return diccionario