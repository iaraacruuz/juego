

import pygame
from archivos2 import *
from animaciones2 import*
import random
from class_item import * 


class Personaje():
    def __init__(self,tamaño,animaciones,posicion_inicial,velocidad):
        
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
        self.rect= self.animaciones["camina_derecha"][0].get_rect()
        self.rect.x= posicion_inicial[0]
        self.rect.y= posicion_inicial[1]
        self.lados= obtener_rectangulos(self.rect)
        self.velocidad = velocidad
        #MOVIMIENTO:
        self.velocidad= velocidad
        self.desplazamiento_y = 0  
        self.desplazamiento_X=0
        #BALAS:
        self.balas = []
        #VIDA DEL PERSONAJE:
        self.salud_maxima = 10
        self.salud = self.salud_maxima
        self.direccion = "derecha"
        #enemigo:
        self.enemigo = None  # Referencia al enemigo
        self.danio_bala = 2  # Daño que causa la bala al enemigo
        self.colisiones_enemigo = 0

    

    # def check_collision_with_item(self, item):
    #     return pygame.sprite.collide_rect(self, item)
    
    def reescalar_animaciones(self):
        for clave in self.animaciones:
            reescalar_imagenes(self.animaciones[clave],(self.ancho,self.alto))


    def actualizar_rect(self):
        self.rect.x = self.lados["main"].x
        self.rect.y = self.lados["main"].y
        for lado in self.lados:
            self.lados[lado].x = self.rect.x
            self.lados[lado].y = self.rect.y

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
        pygame.draw.rect(cuadro, "Red", (self.lados["main"].x + 8, self.lados["main"].y - 50, 75, 20))
        pygame.draw.rect(cuadro, "Green", (self.lados["main"].x + 8, self.lados["main"].y - 50, 75 - (5 * (10-self.salud)), 20))
        for bala in self.balas:
            bala.draw(cuadro)


    def detectar_colisiones(self, lista_plataformas):
        for piso in lista_plataformas:
            if self.desplazamiento_y >= 0 and self.lados["bottom"].colliderect(piso["main"]):
                self.lados["main"].bottom = piso["main"].top
                self.desplazamiento_y = 0
                self.esta_saltando = False
            # Verificar si el personaje está tratando de pasar por debajo de la plataforma
            if self.desplazamiento_X > 0 and self.lados["right"].colliderect(piso["main"]) and self.lados["bottom"].right > piso["main"].left:
                    self.lados["main"].right = piso["main"].left
            elif self.desplazamiento_X < 0 and self.lados["left"].colliderect(piso["main"]) and self.lados["bottom"].left < piso["main"].right:
                    self.lados["main"].left = piso["main"].right
        if self.enemigo:
            for bala in self.balas:
                if bala.rect.colliderect(self.enemigo.rect):
                    self.enemigo.salud -= self.danio_bala
                    self.balas.remove(bala)
                    break

    def update(self,pantalla,piso):
        
        self.rect.x += self.desplazamiento_X
        
        self.rect.y += self.desplazamiento_y
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
        
        self.detectar_colisiones(piso)

        # self.actualizar_rect()


        self.aplicar_gravedad(pantalla,piso)
        self.detectar_colisiones(piso)

   
    def aplicar_gravedad(self,pantalla,lista_plataformas):
        if self.esta_saltando:
            self.animar(pantalla, "salta")
            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y
            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                self.desplazamiento_y += self.gravedad

        for piso in lista_plataformas:
            if self.lados["bottom"].colliderect(piso["main"]):
                self.desplazamiento_y =0
                self.esta_saltando= False
                self.lados["main"].bottom = piso["main"].top
                break
            else:
                self.esta_saltando = True

    def lanzar_proyectil(self):
        if len(self.balas) < 10:
            facing = 1 if self.que_hace != "izquierda" else -1

            nueva_bala = proyectiles(
                round(self.lados["main"].x + self.lados["main"].width // 2),
                round(self.lados["main"].y + self.lados["main"].height // 2),
                6, (0, 0, 0), facing
            )
            self.balas.append(nueva_bala)
            if self.direccion == "derecha":
                nueva_bala.velocidad = abs(nueva_bala.velocidad)  # Velocidad positiva para lanzar hacia la derecha
            elif self.direccion == "izquierda":
                nueva_bala.velocidad = -abs(nueva_bala.velocidad)  # Velocidad negativa para lanzar hacia la izquierda


class proyectiles(object):
    def __init__(self,  x, y, radius, color,facing):
            self.x=x
            self.y=y
            self.radius= radius
            self.color=color
            self.facing= facing
            self.velocidad= 8*facing
            self.rect = pygame.Rect(x - radius, y - radius, radius * 2, radius * 2)
        

    def draw(self, cuadro):
            pygame.draw.circle(cuadro, self.color, (self.x, self.y), self.radius)
        

    def impactar(self, alguien):
        if alguien.salud > 0:
            alguien.salud -= 1
        else:
            del alguien  # elimina el objeto

    def mover(self):
        self.x += self.velocidad
        self.rect.x = self.x - self.radius
        
    def update(self):
        self.mover()




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
        self.image = self.animaciones["camina_derecha"][self.contador_pasos]
        self.rect = self.image.get_rect()
        self.rect.x = posicion_inicial[0]
        self.rect.y = posicion_inicial[1]
        self.lados = obtener_rectangulos(self.rect)

        # Movimiento:
        self.velocidad = velocidad
        self.direccion = random.choice(["izquierda", "derecha"])

        # Vida del enemigo:
        self.salud_maxima = 10
        self.salud = self.salud_maxima
        #balas:
        self.balas= []       
        self.movimiento = 0

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
        if self.salud > 0:  
            pygame.draw.rect(cuadro, "Red", (self.lados["main"].x + 8, self.lados["main"].y - 50, 75, 20))
            pygame.draw.rect(cuadro, "Green", (self.lados["main"].x + 8, self.lados["main"].y - 50, 75 - (5 * (10-self.salud)), 20))
        for bala in self.balas:
            bala.draw(cuadro)
  

    def detectar_colisiones(self, lista_plataformas):
        for piso in lista_plataformas:
            if self.rect.colliderect(piso["main"]):
                self.cambiar_direccion()
    
    def detectar_colisiones_bala(self, balas,cantidad_dano):
        for bala in balas:
            if self.rect.colliderect(bala.rect):
                self.recibir_dano(1)  # Reducir la salud del enemigo en 1 al recibir un impacto
                balas.remove(bala)
            elif self.salud <= 0:
                self.morir()
            else:
                self.salud -= cantidad_dano
    

    def recibir_dano(self, cantidad_dano):
        if self.salud < 0:
            self.morir()
        else:
            self.salud -= cantidad_dano


    def morir(self):
        self.kill()
            


    def update(self, pantalla, lista_plataformas,balas,cantidad_dano):
        self.animar(pantalla, "camina_" + self.direccion)
        self.mover()
        self.detectar_colisiones(lista_plataformas)
        self.detectar_colisiones_bala(balas,cantidad_dano)
        # Actualizar balas
        for bala in self.balas:
            if bala.rect.colliderect(lista_plataformas):
                self.balas.remove(bala)
            else:
                bala.mover()
                bala.draw(pantalla)
                bala.update()

            if bala.rect.colliderect(self.rect):
                    self.recibir_dano(1)  # Restar 1 punto de salud al enemigo al recibir un impacto de una bala
                    self.balas.remove(bala)
            # Actualizar movimiento del enemigo
        if self.direccion == "derecha":
            self.movimiento = self.velocidad
        elif self.direccion == "izquierda":
            self.movimiento = -self.velocidad
        else:
            self.movimiento = 0
