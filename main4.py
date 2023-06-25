import pygame
from archivos import *
from animaciones import *
from modo import *
import sys


def aplicar_gravedad(pantalla, personaje_animacion, rectangulo_personaje: pygame.Rect, piso: pygame.Rect):
    global desplazamiento_y, esta_saltando

    if esta_saltando:
        animar_personaje(pantalla, rectangulo_personaje, personaje_animacion)

    rectangulo_personaje.y += desplazamiento_y

    if desplazamiento_y + gravedad < limite_velocidad_caida:
        desplazamiento_y += gravedad

    if rectangulo_personaje.colliderect(piso):
        esta_saltando = False
        desplazamiento_y = 0
        rectangulo_personaje.bottom = piso.top



def animar_personaje(pantalla, rectangulo_personaje,accion_personaje):
    global contador_pasos

    largo= len(accion_personaje)
    if contador_pasos >= largo:
        contador_pasos=0
    #el contador va animando y moviendo el personaje, nos dice que secuencia es
    PANTALLA.blit(accion_personaje[contador_pasos],rectangulo_personaje)
    contador_pasos +=1 #va pasando de la imagen en movimiento 0 a la 1 a la 2 y asi sucesivamente
    
def mover_personaje(rectangulo_personaje: pygame.Rect , velocidad):
    rectangulo_personaje.x += velocidad





W, H = 1200, 600
FPS = 10

pygame.init()

RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode((W, H))

# Fondo
fondo = pygame.image.load("ciudad.jpg")
fondo = pygame.transform.scale(fondo, (W, H))


#Personaje:
x_inicial= W/10 
y_inicial= H-100
contador_pasos=0
velocidad= 5
rectangulo_personaje= personaje_camina[0].get_rect()
rectangulo_personaje.x= x_inicial
rectangulo_personaje.y= y_inicial

lista_animaciones=[personaje_quieto,personaje_camina,personaje_camina_izquierda,personaje_salta]
reescalar_imagenes(lista_animaciones,75,85)

posicion_actual_x=0




#SALTO:
gravedad= 1
potencia_salto= -15 #mientras mas chico sea valor mas alto va a saltar
limite_velocidad_caida= 15
esta_saltando= False
desplazamiento_y= 0


#SUPERFICIE:
piso= pygame.Rect(0,0,W,20)
piso.top= rectangulo_personaje.bottom





que_hace= "Quieto"



def actualizar_pantalla(pantalla, que_hace,rectangulo_personaje, velocidad,piso): 
    global desplazamiento_y, esta_saltando
    match que_hace: #si lo que esta haciendo...
        case "Derecha": #esta a la derecha
            #animar:
            animar_personaje(pantalla,rectangulo_personaje,personaje_camina)
            #mover
            mover_personaje(rectangulo_personaje, velocidad)
        case "Izquierda":
            #animar:
            animar_personaje(pantalla,rectangulo_personaje,personaje_camina_izquierda)
            #mover
            mover_personaje(rectangulo_personaje, velocidad*-1)
        case "Salta":
            if not esta_saltando:
                esta_saltando=True
                desplazamiento_y=potencia_salto
        case "Quieto":
            #analizarlo
            animar_personaje(pantalla,rectangulo_personaje, personaje_quieto)

aplicar_gravedad(PANTALLA, personaje_quieto, rectangulo_personaje, piso)  # Llamada inicial a la función de gravedad

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
    if keys[pygame.K_RIGHT]: # Va hacia la derecha
        que_hace = "Derecha"
    elif keys[pygame.K_LEFT]:
        que_hace = "Izquierda"
    elif keys[pygame.K_UP]:
        que_hace = "Salta"
    else:
        que_hace = "Quieto" # Si no se realiza ninguna acción, está quieto

    PANTALLA.blit(fondo, (0, 0))
    if get_mode():
        pygame.draw.rect(PANTALLA, "Red", rectangulo_personaje, 2)
        pygame.draw.rect(PANTALLA, "Green", piso, 2)

    actualizar_pantalla(PANTALLA, que_hace, rectangulo_personaje, velocidad, piso)
    aplicar_gravedad(PANTALLA, personaje_salta, rectangulo_personaje, piso)  # Llamada a la función de gravedad

    pygame.display.update()

