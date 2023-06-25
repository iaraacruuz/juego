import pygame
from archivos import *
from animaciones import *
from modo import *
import sys
import os
import random


def obtener_rectangulos(principal: pygame.Rect):
    diccionario= {}
    #main - bottom- left - top- right(top parte de arriba del rect, bottom parte de abajo, right derecha left izq)
    diccionario["main"]= principal
    diccionario["bottom"]= pygame.Rect(principal.left,  principal.bottom - 10, principal.width,10)
    
    diccionario["right"]= pygame.Rect(principal.right -2, principal.top,2, principal.height)

    diccionario["left"]=  pygame.Rect(principal.left,principal.top,2,principal.height)
    diccionario["top"]= pygame.Rect(principal.left,principal.top, principal.width, 6)
    return diccionario

def aplicar_gravedad(pantalla, personaje_animacion, rectangulo_personaje: pygame.Rect, pisos: pygame.Rect):
    global desplazamiento_y, esta_saltando

    if esta_saltando:
        animar_personaje(pantalla, rectangulo_personaje, personaje_animacion)

    rectangulo_personaje.y += desplazamiento_y

    if desplazamiento_y + gravedad < limite_velocidad_caida:
        desplazamiento_y += gravedad


    for plataforma in pisos:
        if rectangulo_personaje.colliderect(plataforma):
            esta_saltando = False
            desplazamiento_y = 0
            rectangulo_personaje.bottom = plataforma.top + 5
            break
        else:
            esta_saltando = True


def animar_personaje(pantalla, rectangulo_personaje,accion_personaje):
    global contador_pasos

    largo= len(accion_personaje)
    if contador_pasos >= largo:
        contador_pasos=0
    #el contador va animando y moviendo el personaje, nos dice que secuencia es
    pantalla.blit(accion_personaje[contador_pasos],rectangulo_personaje)
    contador_pasos +=1 #va pasando de la imagen en movimiento 0 a la 1 a la 2 y asi sucesivamente
    
def mover_personaje(rectangulo_personaje: pygame.Rect , velocidad):
    rectangulo_personaje.x += velocidad



W, H = 1200, 600
FPS = 10

limite_superior = H/4
limite_inferior = 3*H/4


pygame.init()

RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((W, H))

# Fondo
fondo = pygame.image.load("ciudad.jpg")
fondo = pygame.transform.scale(fondo, (W, H))

lista_animaciones=[personaje_quieto,personaje_camina,personaje_camina_izquierda,personaje_salta]
reescalar_imagenes(lista_animaciones,75,85)

#Personaje:
x_inicial= W/10 
y_inicial= H-100
contador_pasos=0
velocidad= 10
rectangulo_personaje= personaje_camina[0].get_rect()
rectangulo_personaje.x= x_inicial
rectangulo_personaje.y= y_inicial



posicion_actual_x=0



que_hace= "Quieto"

#SALTO:
gravedad= 1
potencia_salto= -15 #mientras mas chico sea valor mas alto va a saltar
limite_velocidad_caida= 15
esta_saltando= False
desplazamiento_y= 0


#SUPERFICIE:
#piso:
piso= pygame.Rect(0,0,W,20)
piso.top= rectangulo_personaje.bottom


#PLATAFORMA:
plataforma= pygame.image.load("plataforma5.png.png")
plataforma= pygame.transform.scale(plataforma, (300,75))
rectangulo_plataforma= plataforma.get_rect()
rectangulo_plataforma.x= 500
rectangulo_plataforma.y= 400



nueva_plataforma= pygame.image.load("plataforma5.png.png")
nueva_plataforma= pygame.transform.scale(nueva_plataforma, (300,75))
rectangulo_plataforma_nueva= nueva_plataforma.get_rect()
rectangulo_plataforma_nueva.x= 800
rectangulo_plataforma_nueva.y= 350

nueva_plataforma_2= pygame.image.load("plataforma5.png.png")
nueva_plataforma_2= pygame.transform.scale(nueva_plataforma_2, (200,75))
rectangulo_plataforma_nueva_2= nueva_plataforma_2.get_rect()
rectangulo_plataforma_nueva_2.x= 220
rectangulo_plataforma_nueva_2.y= 480

nueva_plataforma_3= pygame.image.load("plataforma5.png.png")
nueva_plataforma_3= pygame.transform.scale(nueva_plataforma_3, (200,75))
rectangulo_plataforma_nueva_3= nueva_plataforma_3.get_rect()
rectangulo_plataforma_nueva_3.x= 120
rectangulo_plataforma_nueva_3.y= 280

lista_plataformas=[piso,rectangulo_plataforma,rectangulo_plataforma_nueva,rectangulo_plataforma_nueva_2]


class Enemigos(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        carpeta_movimiento = os.path.join(os.getcwd() ,"snake" ,"movimiento")
        archivos_imagenes = os.listdir(carpeta_movimiento)
        self.images = []
        for archivo in archivos_imagenes:
            ruta_completa = os.path.join(carpeta_movimiento, archivo)
            imagen = pygame.image.load(ruta_completa).convert()
            self.images.append(imagen)
        self.image_index = 0
        self.image = self.images[self.image_index]
        self.rect = self.image.get_rect()
        BLANCO = (0, 0, 0)
        # self.image.set_colorkey(BLANCO)
        self.rect.x = random.randrange(W- self.rect.width)
        self.rect.y= random.randrange(500 - self.rect.height)  # Posición aleatoria en el eje x
        self.velocidad_x=5
        self.velocidad_y= 5

    def update(self):
        self.rect.x+= self.velocidad_x
        self.rect.y+= self.velocidad_y
    

        if self.rect.left<0:
            self.velocidad_x +=1

        if self.rect.right>W:
            self.velocidad_x-=1
        
        if self.rect.top<0:
            self.rect.top=0




sprites = pygame.sprite.Group()
for enemigo in range(random.randrange(3) + 1):
    enemigo = Enemigos()
    sprites.add(enemigo)
sprites.update()


def actualizar_pantalla(pantalla, que_hace,rectangulo_personaje, velocidad, plataformas): 
    global desplazamiento_y, esta_saltando
    pantalla.blit(fondo, (0, 0))

    pantalla.blit(plataforma,(rectangulo_plataforma.x, rectangulo_plataforma.y))
    pantalla.blit(nueva_plataforma,(rectangulo_plataforma_nueva.x, rectangulo_plataforma_nueva.y))
    pantalla.blit(nueva_plataforma_2,(rectangulo_plataforma_nueva_2.x, rectangulo_plataforma_nueva_2.y))
    pantalla.blit(nueva_plataforma_3,(rectangulo_plataforma_nueva_3.x, rectangulo_plataforma_nueva_3.y))
    match que_hace: #si lo que esta haciendo...
        case "Derecha": #esta a la derecha
            if not esta_saltando:
                #animar:
                animar_personaje(pantalla,rectangulo_personaje,personaje_camina)
                #mover
                mover_personaje(rectangulo_personaje, velocidad)
        case "Izquierda":
            if not esta_saltando:
            #animar:
                animar_personaje(pantalla,rectangulo_personaje,personaje_camina_izquierda)
                #mover
            mover_personaje(rectangulo_personaje, velocidad*-1)
        case "Salta":
            if not esta_saltando:
                esta_saltando=True
                desplazamiento_y=potencia_salto
        case "Quieto":
            if not esta_saltando:
            #analizarlo
                animar_personaje(pantalla,rectangulo_personaje, personaje_quieto)

    aplicar_gravedad(pantalla, personaje_quieto, rectangulo_personaje, plataformas)  # Llamada inicial a la función de gravedad

# class Enemigos(pygame.sprite.Sprite):
#         def __init__(self):
#             super().__init__()
#             self.image= pygame.image.load("snake").convert()
#             self.rect=self.image.get_rect()

# sprites= pygame.sprite.Group()
# enemigo= Enemigos()
# sprites.add(enemigo)


while True:
    RELOJ.tick(FPS)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_TAB:
                cambiar_modo()

    keys = pygame.key.get_pressed() # Teclas presionadas
    if keys[pygame.K_RIGHT] and rectangulo_personaje.right < W - velocidad : # Va hacia la derecha
        que_hace = "Derecha"
    elif keys[pygame.K_LEFT]and rectangulo_personaje.left > velocidad:
        que_hace = "Izquierda"
    elif keys[pygame.K_UP]:
        que_hace = "Salta"
    else:
        que_hace = "Quieto" # Si no se realiza ninguna acción, está quieto
    
    aplicar_gravedad(PANTALLA, personaje_quieto, rectangulo_personaje, lista_plataformas)  # Llamada a la función de gravedad


    PANTALLA.blit(fondo,(0,0))
    PANTALLA.blit(plataforma, rectangulo_plataforma)
    actualizar_pantalla(PANTALLA, que_hace, rectangulo_personaje, velocidad, lista_plataformas)
    sprites.update()
    sprites.draw(PANTALLA)  # Dibujar los sprites en la pantalla
    pygame.display.flip()
    pygame.draw.rect(PANTALLA, "Red", rectangulo_personaje, 2)
    pygame.draw.rect(PANTALLA, "Green", piso, 2)
    pygame.draw.rect(PANTALLA, "Green", rectangulo_plataforma, 2)
    pygame.draw.rect(PANTALLA, "Green", rectangulo_plataforma_nueva, 2)
    pygame.draw.rect(PANTALLA, "Green", rectangulo_plataforma_nueva_2, 2)
    pygame.draw.rect(PANTALLA, "Green", rectangulo_plataforma_nueva_3, 2)

    pygame.display.update()



# while True:
#     RELOJ.tick(FPS)

#     for evento in pygame.event.get():
#         if evento.type == pygame.QUIT:
#             pygame.quit()
#             sys.exit(0)
#         elif evento.type == pygame.KEYDOWN:
#             if evento.key == pygame.K_TAB:
#                 cambiar_modo()

#     keys = pygame.key.get_pressed() # Teclas presionadas
#     if keys[pygame.K_RIGHT] and rectangulo_personaje.right < W - velocidad : # Va hacia la derecha
#         que_hace = "Derecha"
#     elif keys[pygame.K_LEFT]and rectangulo_personaje.left > velocidad:
#         que_hace = "Izquierda"
#     elif keys[pygame.K_UP]:
#         que_hace = "Salta"
#     else:
#         que_hace = "Quieto" # Si no se realiza ninguna acción, está quieto
    
   
#     sprites.update()
#     sprites.draw(PANTALLA)
#     pygame.display.flip()
#     PANTALLA.blit(fondo,(0,0))
#     PANTALLA.blit(plataforma, rectangulo_plataforma)
#     actualizar_pantalla(PANTALLA, que_hace, rectangulo_personaje, velocidad, lista_plataformas)
#     pygame.draw.rect(PANTALLA, "Red", rectangulo_personaje, 2)
#     pygame.draw.rect(PANTALLA, "Green", piso, 2)
#     pygame.draw.rect(PANTALLA, "Green", rectangulo_plataforma, 2)
#     pygame.draw.rect(PANTALLA, "Green", rectangulo_plataforma_nueva, 2)
#     pygame.draw.rect(PANTALLA, "Green", rectangulo_plataforma_nueva_2, 2)
#     pygame.draw.rect(PANTALLA, "Green", rectangulo_plataforma_nueva_3, 2)

#     # aplicar_gravedad(PANTALLA, personaje_salta, rectangulo_personaje, piso)  # Llamada a la función de gravedad

#     pygame.display.update()

