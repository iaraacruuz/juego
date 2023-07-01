import pygame
from class_personaje import Personaje
import random

class Item(pygame.sprite.Sprite):
    def __init__(self, posicion, tamaño, imagen, valor_puntaje):
        super().__init__()
        self.image = pygame.image.load(imagen)
        self.image = pygame.transform.scale(self.image, tamaño)
        self.rect = self.image.get_rect()
        self.rect.topleft = posicion
        self.valor_puntaje = valor_puntaje
    
    items_group = pygame.sprite.Group()

    def update(self,personaje, items_group):
        if self.rect.colliderect(personaje.rect):
            personaje.puntaje += self.valor_puntaje
            items_group.remove(self)
            self.kill()
 
    def update_posicion(self, posicion):
        self.rect.topleft = posicion

    def colision_con_personaje(self, personaje):
        if self.rect.colliderect(personaje.rect):
            personaje.puntaje += self.valor_puntaje
            self.update_posicion((random.randint(100, 1000), random.randint(100, 500)))

    
    lista_items = []
    
    def agregar_item(lista_items):
        posicion_item = (300, 500)  # Aquí puedes usar una posición aleatoria si prefieres
        tamaño_item = (40, 40)  # Ajusta el tamaño según tus necesidades
        imagen_item = "14.png"  # Ruta de la imagen del item
        valor_puntaje_item = 10  # Valor que suma al puntaje del jugador al recoger el item
        nuevo_item = Item(posicion_item, tamaño_item, imagen_item, valor_puntaje_item)
        lista_items.append(nuevo_item)
    
    @classmethod
    def detectar_colision_items(cls, un_personaje: Personaje, lista_items):
        for item in lista_items:
            if un_personaje.rect.colliderect(item.rect):
                # Aquí podrías agregar efectos o animaciones al recoger el item, si lo deseas
                un_personaje.puntaje += item.valor_puntaje
                lista_items.remove(item)
                un_personaje.puntaje += 10  
    def dibujar_y_actualizar_items(pantalla, items):
            # for item in items:
            #     item.update()
            #     pantalla.blit(item.image, item.rect)
            Item.items_group.update()
            Item.items_group.draw(pantalla)