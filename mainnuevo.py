
import pygame,sys
from archivos2 import*
from animaciones2 import *
from class_personaje import *
from modo2 import *
import turtle
from class_item import * 


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

#TEXTO:
# texto= turtle.Turtle()
# texto.speed(0)
# texto.color("Black")
# texto.penup()
# texto.hideturtle()
# texto.goto(0,260)
# texto.write("Puntaje:0          high score: 0", align= "center", font= ("Courier",24, "normal"))



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
#BALAS:
tanda_balas=0
bullets=[]
ruta_musica_bala= "rayo.mp3"
sonido_bala= pygame.mixer.Sound(ruta_musica_bala)
ruta_golpe="golpe.mp3"
sonido_golpe=pygame.mixer.Sound(ruta_golpe)
#############################

balas=[]

# def redraw():
#     for bala in mi_personaje.balas:
#         pygame.draw.rect(PANTALLA, (255, 0, 0), bala.rect)
#         bala.update()
#     items_group.update()
#     items_group.draw(PANTALLA)

#     pygame.display.update()
def redraw():
    for bala in mi_personaje.balas:
        pygame.draw.rect(PANTALLA, (255, 0, 0), bala.rect)
        bala.update()
    items_group.update(mi_personaje, items_group)  
    items_group.draw(PANTALLA)

    pygame.display.update()

# ruta_musica= "musica.mp3"
# musica_fondo= pygame.mixer.music.load(ruta_musica)

# pygame.mixer.music.play(-1)
#####################
limite_izquierdo = 0
limite_derecho = W - mi_enemigo.lados["main"].width
if tanda_balas == 0:
    tanda_balas = 1

##########################
items_group = pygame.sprite.Group()

# Antes de entrar al bucle principal del juego
# for _ in range(5):
#     item = Item((300, 500), (40, 40), "14.png", 10)
#     # item.update_posicion((300, 500))  # Agregar esta línea para actualizar el rectángulo del item
#     items_group.add(item)
for _ in range(5):
    item = Item((random.randint(100, 1000), random.randint(100, 500)), (40, 40), "14.png", 10)
    items_group.add(item)

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
        
          
    

    # Item.detectar_colision_items(mi_personaje, Item.lista_items)

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
    
  
    PANTALLA.blit(fondo, (0, 0))
    

    pygame.display.flip()
    if mi_enemigo.rect.left <= limite_izquierdo or mi_enemigo.rect.right >= limite_derecho:
        mi_enemigo.cambiar_direccion()
    

   
    for item in items_group:
        if mi_personaje.rect.colliderect(item.rect):
            # Item collision: Add points, remove the item
            # item.update(mi_personaje, items_group)
            # mi_personaje.puntaje += item.valor_puntaje
            item.colision_con_personaje(mi_personaje)
            items_group.remove(item)
            

    # Item.dibujar_y_actualizar_items(PANTALLA, Item.lista_items)
    actualizar_pantalla(PANTALLA, mi_personaje, fondo, lista_plataformas, plataforma_imagen, plataforma_imagen_2)
     # Dibujar y actualizar enemigo
    enemigos_group.update(PANTALLA, lista_plataformas, mi_enemigo.balas,1)
    Item.dibujar_y_actualizar_items(PANTALLA, Item.lista_items)
    
    mi_personaje.dibujar(PANTALLA)
    mi_enemigo.dibujar(PANTALLA)
 
    for lado in lados_piso:
    
        pygame.draw.rect(PANTALLA,"Orange",lados_piso[lado],3)
    for lado in mi_personaje.lados:
            pygame.draw.rect(PANTALLA,"Blue",mi_personaje.lados[lado],3)
    
    for lado in lados_plataforma2:
        pygame.draw.rect(PANTALLA, "Green", lados_plataforma2[lado], 3)
    
    
    pygame.draw.rect(PANTALLA, "Red", plataforma,3)
    pygame.draw.rect(PANTALLA,"Green", plataforma2, 3)
    pygame.draw.rect(PANTALLA, "Red", mi_enemigo.rect, 3)

   
    for bala in mi_personaje.balas:
        bala.update()

    redraw()
   
 

    pygame.display.update()

