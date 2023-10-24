# import pygame
# from mainnuevo import *
# from class_personaje import *
# import random
# import os

# class Enemigos(pygame.sprite.Sprite):
#     def __init__(self):
#         super().__init__()
#         carpeta_movimiento = os.path.join(os.getcwd() ,"snake" ,"movimiento")
#         archivos_imagenes = os.listdir(carpeta_movimiento)
#         self.images = []
#         for archivo in archivos_imagenes:
#             ruta_completa = os.path.join(carpeta_movimiento, archivo)
#             imagen = pygame.image.load(ruta_completa).convert()
#             self.images.append(imagen)
#         self.image_index = 0
#         self.image = self.images[self.image_index]
#         self.rect = self.image.get_rect()
#         BLANCO = (0, 0, 0)
#         # self.image.set_colorkey(BLANCO)
#         self.rect.x = random.randrange(W- self.rect.width)
#         self.rect.y= random.randrange(500 - self.rect.height)  # Posición aleatoria en el eje x
#         self.velocidad_x=5
#         self.velocidad_y= 5

#     def update(self):
#         self.rect.x+= self.velocidad_x
#         self.rect.y+= self.velocidad_y
    

#         if self.rect.left<0:
#             self.velocidad_x +=1

#         if self.rect.right>W:
#             self.velocidad_x-=1
        
#         if self.rect.top<0:
#             self.rect.top=0

# import pygame
# import os
# import random
# from class_personaje import *
# from mainnuevo import *

