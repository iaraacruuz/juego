import pygame
class Plataforma:
    def __init__(self, x, y, ancho, alto, imagen):
        self.rectangulo = pygame.Rect(x, y, ancho, alto)
        self.imagen = pygame.transform.scale(imagen, (ancho, alto))
        
                                            