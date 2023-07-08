
import pygame,sys
from archivos2 import*
from animaciones2 import *
from class_personaje import *
from modo2 import *
from class_item import Item
from class_plataforma import * 

def actualizar_pantalla(pantalla, un_personaje: Personaje, fondo, lista_plataformas, plataforma_imagen,plataforma_imagen_2, items_group):
    pantalla.blit(fondo, (0, 0))
    pantalla.blit(plataforma_imagen, plataforma)
    pantalla.blit(plataforma_imagen_2, plataforma2)
    un_personaje.update(pantalla, lista_plataformas)
      # Check if the item exists before drawing
    
    items_group.draw(pantalla)


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


# ITEMS:
items_group = pygame.sprite.Group()
item_image = pygame.image.load("15.png")  # Replace with the actual image path
item_image = pygame.transform.scale(item_image, (50, 50))  # Replace the size with your desired dimensions

item_position = (500, 400)  # Set the initial position of the item
item = Item(item_image, item_position[0], item_position[1])
items_group.add(item)
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
# #PLATAFORMA:
# tamaño_plataforma=(200,100)
# plataforma_imagen = pygame.image.load("plataforma5.png.png")
# plataforma_imagen = pygame.transform.scale(plataforma_imagen, tamaño_plataforma)

# plataforma = pygame.Rect(400, 460, tamaño_plataforma[0], tamaño_plataforma[1])  # Posición (300, 400) y tamaño personalizado
# lados_plataforma = obtener_rectangulos(plataforma)


# tamaño_plataforma2 = (250, 100)
# plataforma_imagen_2 = pygame.image.load("plataforma5.png.png")
# plataforma_imagen_2 = pygame.transform.scale(plataforma_imagen_2, tamaño_plataforma2)
# plataforma2 = pygame.Rect(600, 400, tamaño_plataforma2[0], tamaño_plataforma2[1])
# lados_plataforma2 = obtener_rectangulos(plataforma2)


# lista_plataformas= [lados_piso,lados_plataforma, lados_plataforma2]

#############################################################################
tamaño_plataforma = (200, 100)
tamaño_plataforma2 = (250, 100)

plataforma_imagen = pygame.image.load("plataforma5.png.png")
plataforma_imagen = pygame.transform.scale(plataforma_imagen, tamaño_plataforma)

plataforma = Plataforma(plataforma_imagen, 400, 460, tamaño_plataforma[0], tamaño_plataforma[1])

plataforma_imagen_2 = pygame.image.load("plataforma5.png.png")
plataforma_imagen_2 = pygame.transform.scale(plataforma_imagen_2, tamaño_plataforma2)

plataforma2 = Plataforma(plataforma_imagen_2, 600, 400, tamaño_plataforma2[0], tamaño_plataforma2[1])
lados_piso = plataforma.obtener_lados()
lados_plataforma = plataforma.obtener_lados()
lados_plataforma2 = plataforma2.obtener_lados()
lista_plataformas = [lados_piso, lados_plataforma, lados_plataforma2]


#LIMITES:
limite_izquierdo = 0
limite_derecho = W - mi_personaje.lados["main"].width
velocidad = 5
#BALAS:
tanda_balas=0
bullets=[]
ruta_musica_bala= "rayo.mp3"
sonido_bala= pygame.mixer.Sound(ruta_musica_bala)
ruta_golpe="golpe.mp3"
sonido_golpe=pygame.mixer.Sound(ruta_golpe)
#############################

balas=[]

def redraw():
    for bala in mi_personaje.balas:
        pygame.draw.rect(PANTALLA, (255, 0, 0), bala.rect)
        bala.update()

    pygame.display.update()
# ruta_musica= "musica.mp3"
# musica_fondo= pygame.mixer.music.load(ruta_musica)

# pygame.mixer.music.play(-1)
#####################
limite_izquierdo = 0
limite_derecho = W - mi_enemigo.lados["main"].width
if tanda_balas == 0:
    tanda_balas = 1
#########################
# player_group = pygame.sprite.Group()
# item_group = pygame.sprite.Group()

# player_group.add(mi_personaje)
# item_group.add(my_item)
#######################

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

    direccion=0
    if keys[pygame.K_RIGHT] and mi_personaje.lados["main"].right + velocidad <= limite_derecho  :
        mi_personaje.que_hace = "derecha"
        mi_personaje.direccion = "derecha"  # Establecer dirección como "derecha"
        if mi_personaje.direccion == "derecha":
             direccion= 1
    elif keys[pygame.K_LEFT] and  mi_personaje.lados["main"].left - velocidad >= limite_izquierdo :
            mi_personaje.que_hace = "izquierda"
            mi_personaje.direccion = "izquierda"  # Establecer dirección como "derecha"
            if mi_personaje.direccion == "izquierda":
             direccion= -1
    elif keys[pygame.K_UP]:
        mi_personaje.que_hace = "salta"
    
    else:
        mi_personaje.que_hace = "quieto" # Si no se realiza ninguna acción, está quieto
        direccion=0
    



    if tanda_balas >0:
        tanda_balas +=1
    if tanda_balas>3:
        tanda_balas=0
    #Contacto del rpoyectil con el villano:

    if tanda_balas == 1:
        for bala in mi_personaje.balas:
            if len(mi_personaje.balas) < 5:
                x_bala = mi_personaje.lados["main"].x + mi_personaje.lados["main"].width // 2
                mi_personaje.balas.append(proyectiles(x_bala, mi_personaje.lados["main"].y + mi_personaje.alto // 2, 10 , "Black", direccion))
                sonido_bala.play()
            tanda_balas = 2


   
    for bala in mi_personaje.balas:
        if bala.rect.colliderect(mi_enemigo.rect):
            sonido_golpe.play()
            mi_enemigo.salud -= 5
            mi_personaje.balas.remove(bala)
  
        else:
            bala.update()  # Actualiza la posición de la bala
    for bala in mi_personaje.balas: 
        if bala.x < W and bala.x > 0:
                # Mueve la bala si está dentro de la ventana
                    bala.x += bala.velocidad
        else:
                # Elimina la bala si está fuera de la ventana
                    mi_personaje.balas.remove(bala)

    if mi_enemigo.salud < 0:
                enemigos_group.remove(mi_enemigo)
                
                mi_enemigo.morir()

    if mi_personaje.rect.colliderect(mi_enemigo.rect):
        mi_personaje.salud -= 1

    mi_enemigo.detectar_colisiones_bala(mi_enemigo.balas,1)
    
    


    items_group.update(lista_plataformas)
 
    if mi_personaje.rect.colliderect(item.rect):
        item.check_collision(mi_personaje)

    if mi_enemigo.rect.left <= limite_izquierdo or mi_enemigo.rect.right >= limite_derecho:
        mi_enemigo.cambiar_direccion()
    

    print(mi_personaje.rect)
    items_group.draw(PANTALLA)
    mi_personaje.update(PANTALLA, lista_plataformas) 
    mi_personaje.aplicar_gravedad(PANTALLA, lista_plataformas)
    actualizar_pantalla(PANTALLA, mi_personaje, fondo, lista_plataformas, plataforma_imagen, plataforma_imagen_2,item)
     # Dibujar y actualizar enemigo
    enemigos_group.update(PANTALLA, lista_plataformas, mi_enemigo.balas,1)
    mi_enemigo.detectar_colisiones(lista_plataformas)

    # mi_personaje.update(PANTALLA, lista_plataformas)  # Update character position and animation
    # actualizar_pantalla(PANTALLA, mi_personaje, fondo, plataformas_group, item)
    # PANTALLA.blit(my_item.image, my_item.rect)
    mi_personaje.dibujar(PANTALLA)
    mi_enemigo.dibujar(PANTALLA)
    # plataforma.dibujar(PANTALLA)
    # plataforma2.dibujar(PANTALLA)

    # items_group.draw(PANTALLA)

    for lado in lados_piso:
        pygame.draw.rect(PANTALLA,"Orange",lados_piso[lado],3)
    for lado in mi_personaje.lados:
            pygame.draw.rect(PANTALLA,"Blue",mi_personaje.lados[lado],3)
    
    # plataformas_group.draw(PANTALLA)
    for lado in lados_plataforma2:
        pygame.draw.rect(PANTALLA, "Green", lados_plataforma2[lado], 3)
    
    
    pygame.draw.rect(PANTALLA, "Red", plataforma,3)
    pygame.draw.rect(PANTALLA,"Green", plataforma2, 3)
    pygame.draw.rect(PANTALLA,"Blue", item.rect, 3)
   
    for bala in mi_personaje.balas:
        bala.update()
    redraw()
   
 

    pygame.display.update()

