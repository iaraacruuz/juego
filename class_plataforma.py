import pygame
from archivos2 import * 
class Plataforma:
    def __init__(self, imagen, x, y, ancho, alto):
        self.imagen = imagen
        self.rect = pygame.Rect(x, y, ancho, alto)

    def dibujar(self, pantalla):
        pantalla.blit(self.imagen, self.rect)
    def obtener_lados(self):
        return obtener_rectangulos(self.rect)