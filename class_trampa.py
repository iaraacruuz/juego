<<<<<<< HEAD
import pygame
import random

class Trampa(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.puede_colisionar = True  # Bandera para indicar si puede colisionar
        self.recogido = False  #bandera para indicar si lo recogio o no

    def dibujar(self, surface):
        if self.puede_colisionar:  # Verificar si puede colisionar antes de dibujarlo
            surface.blit(self.image, self.rect) #lo dibuja


    
    
    def obtener_rectangulos(self, principal: pygame.Rect) -> dict:
        diccionario = {}
        diccionario["main"] = principal
        diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom - 10, principal.width, 10)
        diccionario["right"] = pygame.Rect(principal.right - 2, principal.top, 2, principal.height)
        diccionario["left"] = pygame.Rect(principal.left, principal.top, 2, principal.height)
        diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 10)
        return diccionario
    
    
    def check_colision(self, personaje, puntaje):

        if personaje.rect.colliderect(self.rect) and not self.recogido:
            self.recogido = True
            puntaje += 10   #agrega 10 ptos por item
        return puntaje
    
    
    def generar_trampa(num_trampas, min_x, max_x, min_y, max_y, trampa_image):
        trampa_list = []

        for _ in range(num_trampas):
            x = random.randint(min_x, max_x)  # Genera una coordenada X aleatoria
            y = random.randint(min_y, max_y)  # Genera una coordenada Y aleatoria

            trampa = Trampa(trampa_image, x, y)
            trampa_list.append(trampa)

        return trampa_list
=======
import pygame
import random

class Trampa(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.puede_colisionar = True  # Bandera para indicar si puede colisionar
        self.recogido = False  #bandera para indicar si lo recogio o no

    def dibujar(self, surface):
        if self.puede_colisionar:  # Verificar si puede colisionar antes de dibujarlo
            surface.blit(self.image, self.rect) #lo dibuja


    
    
    def obtener_rectangulos(self, principal: pygame.Rect) -> dict:
        diccionario = {}
        diccionario["main"] = principal
        diccionario["bottom"] = pygame.Rect(principal.left, principal.bottom - 10, principal.width, 10)
        diccionario["right"] = pygame.Rect(principal.right - 2, principal.top, 2, principal.height)
        diccionario["left"] = pygame.Rect(principal.left, principal.top, 2, principal.height)
        diccionario["top"] = pygame.Rect(principal.left, principal.top, principal.width, 10)
        return diccionario
    
    
    def check_colision(self, personaje, puntaje):

        if personaje.rect.colliderect(self.rect) and not self.recogido:
            self.recogido = True
            puntaje += 10   #agrega 10 ptos por item
        return puntaje
    
    
    def generar_trampa(num_trampas, min_x, max_x, min_y, max_y, trampa_image):
        trampa_list = []

        for _ in range(num_trampas):
            x = random.randint(min_x, max_x)  # Genera una coordenada X aleatoria
            y = random.randint(min_y, max_y)  # Genera una coordenada Y aleatoria

            trampa = Trampa(trampa_image, x, y)
            trampa_list.append(trampa)

        return trampa_list
>>>>>>> 52117411583005a06c67a216e64fbb0df54ceb61
