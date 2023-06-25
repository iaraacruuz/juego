import pygame,sys
from archivos2 import*
from animaciones2 import *
from class_personaje import *
from modo2 import *

def actualizar_pantalla(pantalla, un_personaje: Personaje, fondo, lista_plataformas, plataforma_imagen,plataforma_imagen_2):
    pantalla.blit(fondo, (0, 0))
    pantalla.blit(plataforma_imagen, plataforma)
    pantalla.blit(plataforma_imagen_2, plataforma2)
    un_personaje.update(pantalla, lista_plataformas)

#PANTALLA:
W, H = 1200, 600
TAMAÑO= (W,H)
FPS = 10
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode(TAMAÑO)
# Fondo
fondo = pygame.image.load("ciudad.jpg")
fondo = pygame.transform.scale(fondo, TAMAÑO)


pygame.init()



#PERSONAJE:
posicion_inicial= (H/2 - 300,500)
tamaño=(75,85)
diccionario_animaciones={}
diccionario_animaciones["quieto"]= personaje_quieto
diccionario_animaciones["salta"]= personaje_salta
diccionario_animaciones["camina_derecha"]= personaje_camina
diccionario_animaciones["camina_izquierda"]= personaje_camina_izquierda

mi_personaje = Personaje(tamaño, diccionario_animaciones, posicion_inicial, 10)
#ENEMIGO: 
enemigos_group = pygame.sprite.Group()
sprites = pygame.sprite.Group()
posicion_enemigo = (H/2 - 100, 500)  # Cambia la posición según tus necesidades
tamaño_enemigo = (75, 85)  # Cambia el tamaño según tus necesidades
diccionario_animaciones_enemigo = {}
diccionario_animaciones_enemigo["camina_derecha"] = enemigo_camina_derecha
diccionario_animaciones_enemigo["camina_izquierda"] = enemigo_camina_izquierda

mi_enemigo = Enemigo(tamaño_enemigo, diccionario_animaciones_enemigo, posicion_enemigo, 7)  # Cambia la velocidad según tus necesidades
enemigos_group.add(mi_enemigo)

#PISO:
piso= pygame.Rect(0,0,W,15)
piso.top= mi_personaje.lados["main"].bottom

lados_piso= obtener_rectangulos(piso)
#PLATAFORMA:
tamaño_plataforma=(200,100)
# PLATAFORMA:
plataforma_imagen = pygame.image.load("plataforma5.png.png")
plataforma_imagen = pygame.transform.scale(plataforma_imagen, tamaño_plataforma)

plataforma = pygame.Rect(400, 460, tamaño_plataforma[0], tamaño_plataforma[1])  # Posición (300, 400) y tamaño personalizado
lados_plataforma = obtener_rectangulos(plataforma)


tamaño_plataforma2 = (250, 100)
plataforma_imagen_2 = pygame.image.load("plataforma5.png.png")
plataforma_imagen_2 = pygame.transform.scale(plataforma_imagen_2, tamaño_plataforma2)
plataforma2 = pygame.Rect(600, 400, tamaño_plataforma2[0], tamaño_plataforma2[1])
lados_plataforma2 = obtener_rectangulos(plataforma2)


lista_plataformas= [lados_piso,lados_plataforma, lados_plataforma2]


#LIMITES:
limite_izquierdo = 0
limite_derecho = W - mi_personaje.lados["main"].width
velocidad = 5


        
def redraw():

    # Dibuja los proyectiles

    for bala in mi_personaje.balas:
        bala.draw(PANTALLA)
    pygame.display.update()         


bullets=[]

ruta_musica= "musica.mp3"
musica_fondo= pygame.mixer.music.load(ruta_musica)

pygame.mixer.music.play(-1)
    
while True:
    RELOJ.tick(FPS)

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_TAB:
                cambiar_modo()        
            elif evento.key == pygame.K_SPACE:
                    mi_personaje.lanzar_proyectil()
        
          
    

    

    keys = pygame.key.get_pressed() # Teclas presionadas

    
    if keys[pygame.K_RIGHT] and mi_personaje.lados["main"].right + velocidad <= limite_derecho  :
        mi_personaje.que_hace = "derecha"
    elif keys[pygame.K_LEFT] and  mi_personaje.lados["main"].left - velocidad >= limite_izquierdo :
            mi_personaje.que_hace = "izquierda"
    elif keys[pygame.K_UP]:
        mi_personaje.que_hace = "salta"
    
    else:
        mi_personaje.que_hace = "quieto" # Si no se realiza ninguna acción, está quieto
    

 

    for bala in mi_personaje.balas:
            if bala.x < 500 and bala.x > 0:
                bala.x += bala.velocidad
            else:
                mi_personaje.balas.remove(bala)
            bala.draw(PANTALLA)
    

    actualizar_pantalla(PANTALLA, mi_personaje, fondo, lista_plataformas, plataforma_imagen, plataforma_imagen_2)
    for lado in lados_piso:
    
        pygame.draw.rect(PANTALLA,"Orange",lados_piso[lado],3)
    for lado in mi_personaje.lados:
            pygame.draw.rect(PANTALLA,"Blue",mi_personaje.lados[lado],3)
    
    for lado in lados_plataforma2:
        pygame.draw.rect(PANTALLA, "Green", lados_plataforma2[lado], 3)
    # Dibujar y actualizar enemigo
    enemigos_group.update(PANTALLA, piso)

    

    sprites.update()
    sprites.draw(PANTALLA)
    # sprites = pygame.sprite.Group()
    # sprites = pygame.sprite.Group()

    pygame.draw.rect(PANTALLA, "Red", plataforma,3)
    pygame.draw.rect(PANTALLA,"Green", plataforma2, 3)

    redraw()

    pygame.display.update()


