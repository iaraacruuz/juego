

import pygame
from archivos2 import *
from animaciones2 import*
import random

# from mainnuevo import *
class Personaje:
    def __init__(self,tamaño,animaciones,posicion_incial,velocidad):
        #CONFECCION:
        self.ancho= tamaño[0]
        self.alto=tamaño[1]

        #GRAVEDAD:
        self.gravedad= 1
        self.potencia_salto= -15
        self.limite_velocidad_caida=15
        self.esta_saltando= False
        #animaciones:
        self.contador_pasos=0
        self.que_hace="quieto"
        self.animaciones=animaciones
        self.reescalar_animaciones()
        #RECTANGULOS:
        rectangulo= self.animaciones["camina_derecha"][0].get_rect()
        rectangulo.x= posicion_incial[0]
        rectangulo.y= posicion_incial[1]
        self.lados= obtener_rectangulos(rectangulo)
        self.velocidad = velocidad
        #MOVIMIENTO:
        self.velocidad= velocidad
        self.desplazamiento_y=0
        self.desplazamiento_X=0
        #BALAS:
        self.balas = []
        #VIDA DEL PERSONAJE:
        self.salud= 10


    
    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagenes(self.animaciones[clave],(self.ancho,self.alto))


        

    def mover(self,velocidad):
        for lado in self.lados:
            self.lados[lado].x += velocidad

    def animar(self,pantalla, que_animacion):
        animacion= self.animaciones[que_animacion]
        largo= len(animacion)

        if self.contador_pasos>=largo:
            self.contador_pasos=0
        
        pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
        self.contador_pasos +=1

    def dibujar(self,cuadro):
        pygame.draw.rect(cuadro,"Red",(self.x+5, self.y-20,50,30))

    def detectar_colisiones(self, lista_plataformas):
        for piso in lista_plataformas:
            if self.lados["main"].colliderect(piso["main"]):
                if self.que_hace == "derecha":
                    self.lados["main"].right = piso["main"].left
                elif self.que_hace == "izquierda":
                    self.lados["main"].left = piso["main"].right


    def update(self,pantalla,piso):
        match self.que_hace:
            case "derecha":
                if not self.esta_saltando:
                    self.animar(pantalla,"camina_derecha")
                self.mover(self.velocidad)
            case "izquierda":
                if not self.esta_saltando:
                    self.animar(pantalla,"camina_izquierda")
                self.mover(self.velocidad *-1)
            case "salta":
                if not self.esta_saltando:
                    self.esta_saltando= True
                    self.desplazamiento_y= self.potencia_salto
            case "quieto":
                if not self.esta_saltando:
                    self.animar(pantalla,"quieto")

        self.aplicar_gravedad(pantalla,piso)

   


    def aplicar_gravedad(self,pantalla,lista_plataformas):
        if self.esta_saltando:
            self.animar(pantalla, "salta")
            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                self.desplazamiento_y += self.gravedad
        for piso in lista_plataformas:
            if self.lados["bottom"].colliderect(piso["top"]):
                self.desplazamiento_y =0
                self.esta_saltando= False
                self.lados["main"].bottom= piso["main"].top
                break
            else:
                self.esta_saltando = True

    def lanzar_proyectil(self):
        if len(self.balas) < 10:
            facing = 1 if self.que_hace != "izquierda" else -1
            # nueva_bala = proyectiles(
            #     round(self.lados["main"].x + self.lados["main"].width // 2),
            #     round(self.lados["main"].y + self.lados["main"].height // 2),
            #     6, (0, 0, 0), facing
            # )
            # self.balas.append(nueva_bala)
            nueva_bala = proyectiles(
                round(self.lados["main"].x + self.lados["main"].width // 2),
                round(self.lados["main"].y + self.lados["main"].height // 2),
                6, (0, 0, 0), facing
            )
            self.balas.append(nueva_bala)
            

class proyectiles(object):
    def __init__(self,  x, y, radius, color,facing):
            self.x=x
            self.y=y
            self.radius= radius
            self.color=color
            self.facing= facing
            self.velocidad= 8*facing
    
    def draw(self, win):
        pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)


import pygame
from archivos2 import *
from animaciones2 import *
import random

# class Enemigo():
    # enemigo_camina_derecha=[pygame.image.load("C:/Users/PC/Desktop/Juego/snake/movimiento/4.png"),
    #                     pygame.image.load("C:/Users/PC/Desktop/Juego/snake/movimiento/5.png"),
    #                     pygame.image.load("C:/Users/PC/Desktop/Juego/snake/movimiento/6.png"),
    #                     pygame.image.load("C:/Users/PC/Desktop/Juego/snake/movimiento/7.png"),
    #                     pygame.image.load("C:/Users/PC/Desktop/Juego/snake/movimiento/8.png"),
    #                     pygame.image.load("C:/Users/PC/Desktop/Juego/snake/movimiento/10.png"),
    #                     pygame.image.load("C:/Users/PC/Desktop/Juego/snake/movimiento/11.png"),
    #                     pygame.image.load("C:/Users/PC/Desktop/Juego/snake/movimiento/12.png"),
    #                     pygame.image.load("C:/Users/PC/Desktop/Juego/snake/movimiento/31.png"),
    #                     pygame.image.load("C:/Users/PC/Desktop/Juego/snake/movimiento/32.png"),
    #                     pygame.image.load("C:/Users/PC/Desktop/Juego/snake/movimiento/33.png"),
    #                     pygame.image.load("C:/Users/PC/Desktop/Juego/snake/movimiento/34.png"),
    #                     pygame.image.load("C:/Users/PC/Desktop/Juego/snake/movimiento/35.png"),
    #                     pygame.image.load("C:/Users/PC/Desktop/Juego/snake/movimiento/36.png")] 

    # enemigo_camina_izquierda= girar_imagenes(enemigo_camina_derecha,True,False)
    # def __init__(self, x,y,width,height,end):
    #     # CONFECCION:
    #     self.x=x
    #     self.y=y
    #     self.width=width
    #     self.height=height
    #     self.path=[x,end]
    #     self.walkCount=0
    #     self.vel=3

    # def draw(self,win):
    #     self.move()
    #     if self.walkCount +1>= 33:
    #         self.walkCount=0
        
    #     if self.vel >0:
    #         win.blit(self.enemigo_camina_derecha[self.walkCount]// 3, (self.x,self.y))
    #         self.walkCount+=1
    #     else:
    #         win.blit(self.enemigo_camina_izquierda[self.walkCount//3], (self.x,self.y))
    #         self.walkCount+=1
    
    # def move(self):
    #     if self.vel> 0:
    #         if self.path[1] + self.vel > self.x:
    #             self.x+=self.vel
    #         else:
    #             self.vel=self.vel *-1
    #             self.x+=self.vel
    #             self.walkCount=0
    #     else:
    #         if self.x > self.path[0] - self.vel:
    #                 self.x+=self.vel
    #         else:
    #             self.vel=self.vel *-1
    #             self.x +=self.vel
    #             self.walkCount=0

 
# import pygame
# from archivos2 import *
# from animaciones2 import *
# import random

# class Enemigo(pygame.sprite.Sprite):
#     def __init__(self, tamaño, animaciones, posicion_inicial, velocidad):
#         super().__init__()
#         # CONFECCION:
#         self.ancho = tamaño[0]
#         self.alto = tamaño[1]

#         # Animaciones:
#         self.contador_pasos = 0
#         self.animaciones = animaciones
#         self.reescalar_animaciones()
#         self.image = self.diccionario_animaciones["camina_derecha"][self.index_animacion]
#         # Rectángulos:
#         rectangulo = self.animaciones["camina_derecha"][0].get_rect()
#         rectangulo.x = posicion_inicial[0]
#         rectangulo.y = posicion_inicial[1]
#         self.lados = obtener_rectangulos(rectangulo)

#         # Movimiento:
#         self.velocidad = velocidad
#         self.direccion = random.choice(["izquierda", "derecha"])

#         # Vida del enemigo:
#         self.salud = 5

#     def reescalar_animaciones(self):
#         for clave in self.animaciones:
#             reescalar_imagenes(self.animaciones[clave], (self.ancho, self.alto))

#     def mover(self):
#         if self.direccion == "derecha":
#             self.lados["main"].x += self.velocidad
#         elif self.direccion == "izquierda":
#             self.lados["main"].x -= self.velocidad

#     def cambiar_direccion(self):
#         if self.direccion == "derecha":
#             self.direccion = "izquierda"
#         elif self.direccion == "izquierda":
#             self.direccion = "derecha"

#     def animar(self, pantalla, que_animacion):
#         animacion = self.animaciones[que_animacion]
#         largo = len(animacion)

#         if self.contador_pasos >= largo:
#             self.contador_pasos = 0

#         pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
#         self.contador_pasos += 1

#     def dibujar(self, cuadro):
#         pygame.draw.rect(cuadro, "Red", (self.x + 5, self.y - 20, 50, 30))

#     def detectar_colisiones(self, lista_plataformas):
#         for piso in lista_plataformas:
#             if self.lados["main"].colliderect(piso["main"]):
#                 self.cambiar_direccion()

#     def recibir_dano(self, cantidad_dano):
#         self.salud -= cantidad_dano
#         if self.salud <= 0:
#             self.morir()

#     def morir(self):
#         # Acciones a realizar cuando el enemigo muere
#         pass

#     def update(self, pantalla, piso):
#         self.animar(pantalla, "camina_" + self.direccion)
#         self.mover()
#         self.detectar_colisiones(piso)
# import pygame
# from archivos2 import *
# from animaciones2 import *
# import random

# class Enemigo(pygame.sprite.Sprite):
#     def __init__(self, tamaño, animaciones, posicion_inicial, velocidad):
#         super().__init__()
#         # CONFECCION:
#         self.ancho = tamaño[0]
#         self.alto = tamaño[1]

#         # Animaciones:
#         self.contador_pasos = 0
#         self.animaciones = animaciones
#         self.reescalar_animaciones()
#         self.image = self.animaciones["camina_derecha"][self.contador_pasos]
#         self.rect = self.image.get_rect()
#         self.rect.x = posicion_inicial[0]
#         self.rect.y = posicion_inicial[1]
#         self.lados = obtener_rectangulos(self.rect)

#         # Movimiento:
#         self.velocidad = velocidad
#         self.direccion = random.choice(["izquierda", "derecha"])

#         # Vida del enemigo:
#         self.salud = 5

#     def reescalar_animaciones(self):
#         for clave in self.animaciones:
#             reescalar_imagenes(self.animaciones[clave], (self.ancho, self.alto))

#     def mover(self):
#         if self.direccion == "derecha":
#             self.rect.x += self.velocidad
#         elif self.direccion == "izquierda":
#             self.rect.x -= self.velocidad

#     def cambiar_direccion(self):
#         if self.direccion == "derecha":
#             self.direccion = "izquierda"
#         elif self.direccion == "izquierda":
#             self.direccion = "derecha"

#     def animar(self, pantalla, que_animacion):
#         animacion = self.animaciones[que_animacion]
#         largo = len(animacion)

#         if self.contador_pasos >= largo:
#             self.contador_pasos = 0

#         pantalla.blit(animacion[self.contador_pasos], self.rect)
#         self.contador_pasos += 1

#     def dibujar(self, cuadro):
#         pygame.draw.rect(cuadro, "Red", (self.rect.x + 5, self.rect.y - 20, 50, 30))

#     def detectar_colisiones(self, lista_plataformas):
#         for piso in lista_plataformas:
#             if self.rect.colliderect(piso["main"]):
#                 self.cambiar_direccion()

#     def recibir_dano(self, cantidad_dano):
#         self.salud -= cantidad_dano
#         if self.salud <= 0:
#             self.morir()

#     def morir(self):
#         # Acciones a realizar cuando el enemigo muere
#         pass

#     def update(self, pantalla, piso):
#         self.animar(pantalla, "camina_" + self.direccion)
#         self.mover()
#         self.detectar_colisiones(piso)
import pygame
from archivos2 import *
from animaciones2 import *
import random

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, tamaño, animaciones, posicion_inicial, velocidad):
        super().__init__()
        # CONFECCION:
        self.ancho = tamaño[0]
        self.alto = tamaño[1]

        # Animaciones:
        self.contador_pasos = 0
        self.animaciones = animaciones
        self.reescalar_animaciones()
        self.image = self.diccionario_animaciones["camina_derecha"][self.contador_pasos]
        
        # Rectángulo:
        self.rect = self.image.get_rect()
        self.rect.x = posicion_inicial[0]
        self.rect.y = posicion_inicial[1]
        
        # Lados:
        self.lados = obtener_rectangulos(self.rect)

        # Movimiento:
        self.velocidad = velocidad
        self.direccion = random.choice(["izquierda", "derecha"])

        # Vida del enemigo:
        self.salud = 5

    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagenes(self.animaciones[clave], (self.ancho, self.alto))

    def mover(self):
        if self.direccion == "derecha":
            self.rect.x += self.velocidad
        elif self.direccion == "izquierda":
            self.rect.x -= self.velocidad

    def cambiar_direccion(self):
        if self.direccion == "derecha":
            self.direccion = "izquierda"
        elif self.direccion == "izquierda":
            self.direccion = "derecha"

    def animar(self, pantalla, que_animacion):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)

        if self.contador_pasos >= largo:
            self.contador_pasos = 0

        pantalla.blit(animacion[self.contador_pasos], self.rect)
        self.contador_pasos += 1

    def dibujar(self, cuadro):
        pygame.draw.rect(cuadro, "Red", (self.rect.x + 5, self.rect.y - 20, 50, 30))

    def detectar_colisiones(self, lista_plataformas):
        for piso in lista_plataformas:
            if self.rect.colliderect(piso.rect):
                self.cambiar_direccion()

    def recibir_dano(self, cantidad_dano):
        self.salud -= cantidad_dano
        if self.salud <= 0:
            self.morir()

    def morir(self):
        # Acciones a realizar cuando el enemigo muere
        pass

    def update(self, pantalla, piso):
        self.animar(pantalla, "camina_" + self.direccion)
        self.mover()
        self.detectar_colisiones(piso)
