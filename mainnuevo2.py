
import pygame,sys
from archivos2 import*
from animaciones2 import *
from class_personaje import *
from modo2 import *
from class_item import *
from class_plataforma import * 

def actualizar_pantalla(pantalla, un_personaje: Personaje, fondo, lista_plataformas, plataforma_imagen, plataforma_imagen_2, items_list):
    pantalla.blit(fondo, (0, 0))
    pantalla.blit(plataforma_imagen, plataforma)
    pantalla.blit(plataforma_imagen_2, plataforma2)
    pantalla.blit(plataforma_imagen_3, plataforma3)
    un_personaje.update(pantalla, lista_plataformas)
    
    for item in items_list:
        item.draw(pantalla)

#PANTALLA:
W, H = 1200, 600
TAMAÑO= (W,H)
FPS = 10
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode(TAMAÑO)
# Fondo  
fondo = pygame.image.load("ciudad2.jpg")
fondo = pygame.transform.scale(fondo, TAMAÑO)

pygame.init() 

#CRONOMETRO:
import time

tiempo_inicio = time.time()  # Tiempo de inicio del cronómetro
tiempo_total = 60  # Duración total del cronómetro en segundos

#PUNTAJE:
puntaje = 0 #inicializa puntaje
#INVULNERABILIDAD:

invulnerable = False
tiempo_invulnerable = 1000  # Tiempo en milisegundos (ejemplo: 1000 = 1 segundo)
tiempo_ultimo_danio = pygame.time.get_ticks()  # Obtén el tiempo actual en milisegundos

# # ITEMS:

items_group = pygame.sprite.Group()
item_image = pygame.image.load("15.png")  # Replace with the actual image path
item_image = pygame.transform.scale(item_image, (50, 50))  # Replace the size with your desired dimensions

min_x, max_x = 5, W  # Rango de coordenadas X
min_y, max_y = int(H * 0.4), int(H * 0.6)  # Rango de coordenadas Y ajustado
num_items = 10  # Número de items que deseas generar

items_list = Item.generar_items(num_items, min_x, max_x, min_y, max_y, item_image)
###############################################################
#PERSONAJE:

posicion_inicial= (H/2 - 300,500)
tamaño=(75,85)
diccionario_animaciones={}
diccionario_animaciones["quieto"]= personaje_quieto_2
diccionario_animaciones["salta"]= personaje_salta_2
diccionario_animaciones["camina_derecha"]= personaje_camina_2
diccionario_animaciones["camina_izquierda"]= personaje_camina_izquierda_2

mi_personaje = Personaje(tamaño, diccionario_animaciones, posicion_inicial, 10)


#PISO:
piso= pygame.Rect(0,0,W,15)
piso.top= mi_personaje.lados["main"].bottom
lados_piso= obtener_rectangulos(piso)


#############################################################################
tamaño_plataforma = (200, 100)
tamaño_plataforma2 = (250, 100)
tamaño_plataforma3 = (300, 100)
plataforma_imagen = pygame.image.load("plataforma6.png")
plataforma_imagen = pygame.transform.scale(plataforma_imagen, tamaño_plataforma)

plataforma = Plataforma(plataforma_imagen, 400, 460, tamaño_plataforma[0], tamaño_plataforma[1])

plataforma_imagen_2 = pygame.image.load("plataforma6.png")
plataforma_imagen_2 = pygame.transform.scale(plataforma_imagen_2, tamaño_plataforma2)

plataforma2 = Plataforma(plataforma_imagen_2, 600, 400, tamaño_plataforma2[0], tamaño_plataforma2[1])
lados_plataforma = plataforma.obtener_lados()
lados_plataforma2 = plataforma2.obtener_lados()

plataforma_imagen_3 = pygame.image.load("plataforma6.png")
plataforma_imagen_3 = pygame.transform.scale(plataforma_imagen_2, tamaño_plataforma3)
plataforma3 = Plataforma(plataforma_imagen_3, 800, 500, tamaño_plataforma3[0], tamaño_plataforma3[1])

lados_plataforma3 = plataforma3.obtener_lados()
lista_plataformas = [lados_piso, lados_plataforma, lados_plataforma2, lados_plataforma3]
#############################################################################
#ENEMIGO: 
enemigos_group = pygame.sprite.Group()
sprites = pygame.sprite.Group()
posicion_enemigo = (H/2 - 100, 500)  # Cambia la posición según tus necesidades
tamaño_enemigo = (75, 85)  # Cambia el tamaño según tus necesidades
diccionario_animaciones_enemigo = {}
diccionario_animaciones_enemigo["camina_derecha"] = enemigo_camina_derecha_2
diccionario_animaciones_enemigo["camina_izquierda"] = enemigo_camina_izquierda_2

mi_enemigo = Enemigo(tamaño_enemigo, diccionario_animaciones_enemigo, posicion_enemigo, 7)  # Cambia la velocidad según tus necesidades
enemigos_group.add(mi_enemigo)

diccionario_animaciones_enemigo_2 = {}
diccionario_animaciones_enemigo_2["camina_derecha"] = enemigo_camina_derecha
diccionario_animaciones_enemigo_2["camina_izquierda"] = enemigo_camina_izquierda
tamaño_enemigo_2 = (75, 85)  # Cambia el tamaño según tus necesidades
posicion_enemigo_2 = (plataforma2.rect.centerx, plataforma2.rect.top - tamaño_enemigo_2[1])


mi_enemigo_2 = Enemigo(tamaño_enemigo_2, diccionario_animaciones_enemigo_2, posicion_enemigo_2, 7)  # Cambia la velocidad según tus necesidades
enemigos_group.add(mi_enemigo_2)

#################################################################
#LIMITES:
limite_izquierdo = 0
limite_derecho = W - mi_personaje.lados["main"].width
velocidad = 5
#BALAS:
tanda_balas=0
balas=[]
#SONIDOS ESPECIALES:
ruta_musica_bala= "rayo.mp3"
sonido_bala= pygame.mixer.Sound(ruta_musica_bala)
ruta_golpe="golpe.mp3"
sonido_golpe=pygame.mixer.Sound(ruta_golpe)
#############################

#DIBUJAR BALAS:
def redraw():
    for bala in mi_personaje.balas:
        pygame.draw.rect(PANTALLA, (255, 0, 0), bala.rect)
        bala.update()

    pygame.display.update()

#MUSICA FONDO:
ruta_musica= "musica.mp3"
musica_fondo= pygame.mixer.music.load(ruta_musica)

pygame.mixer.music.play(-1)

#Musica Golpe PERSONAJE:
ruta_colision = "reaccion.mp3"
sonido_colision = pygame.mixer.Sound(ruta_colision)

#####################
#limites:
limite_izquierdo = 0
limite_derecho = W - mi_enemigo.lados["main"].width
##########################
#control de la tanda de balas:
if tanda_balas == 0:
    tanda_balas = 1
#########################
#limites del segundo enemigo:
limite_izquierdo_plataforma2 = plataforma2.rect.left
limite_derecho_plataforma2 = plataforma2.rect.right - mi_enemigo_2.lados["main"].width
#######################
tiempo_ultimo_danio = pygame.time.get_ticks()  # Obtén el tiempo actual en milisegundos

danio_enemigo = 5

tiempo_inicio_invulnerable = 0
duracion_invulnerabilidad = 100
danio_reduccion_salud= 5
#############################################

#BUCLE PRINCIPAL:
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
 

    #tanda de balas:
    if tanda_balas >0:
        tanda_balas +=1
    if tanda_balas>3:
        tanda_balas=0
        
    #Contacto del proyectil con el villano:
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
    for bala in mi_personaje.balas:
        if bala.rect.colliderect(mi_enemigo_2.rect):
            sonido_golpe.play()
            mi_enemigo_2.salud -= 5
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


        
    #############################################################
 
    if mi_enemigo.lados["main"].colliderect(plataforma.rect):
        mi_enemigo.cambiar_direccion()

    items_group.update(lista_plataformas)

    if mi_enemigo_2.rect.left <= limite_izquierdo_plataforma2 or mi_enemigo_2.rect.right >= limite_derecho_plataforma2:
        if mi_enemigo_2.movimiento != 0:
            mi_enemigo_2.cambiar_direccion()

    ######################################################
    for item in items_list:
        puntaje = item.check_collision(mi_personaje, puntaje)
        item.update()  # Actualiza el estado del item
        item.draw(PANTALLA)  # Dibuja el item en la pantalla
        if item.recogido:
            items_list.remove(item)
    ######################################################################
    if mi_enemigo.rect.left <= limite_izquierdo or mi_enemigo.rect.right >= limite_derecho:
        mi_enemigo.cambiar_direccion()
    
    tiempo_actual = pygame.time.get_ticks()




    print(mi_personaje.rect)
    items_group.draw(PANTALLA)
    mi_personaje.update(PANTALLA, lista_plataformas) 

    mi_personaje.aplicar_gravedad(PANTALLA, lista_plataformas)
   

            

    if mi_personaje.desplazamiento_X > 0 and mi_personaje.lados["right"].colliderect(plataforma.rect) and \
            mi_personaje.lados["bottom"].right > plataforma.rect.left and \
            mi_personaje.lados["top"].bottom > plataforma.rect.top and \
            mi_personaje.lados["bottom"].top < plataforma.rect.bottom:
        mi_personaje.lados["main"].right = plataforma.rect.left
    elif mi_personaje.desplazamiento_X < 0 and mi_personaje.lados["left"].colliderect(plataforma.rect) and \
            mi_personaje.lados["bottom"].left < plataforma.rect.right and \
            mi_personaje.lados["top"].bottom > plataforma.rect.top and \
            mi_personaje.lados["bottom"].top < plataforma.rect.bottom:
        mi_personaje.lados["main"].left = plataforma.rect.right




    mi_personaje.detectar_colisiones(lista_plataformas)
    #cronometro: 
    tiempo_transcurrido = time.time() - tiempo_inicio
    tiempo_restante = tiempo_total - int(tiempo_transcurrido)

    fuente = pygame.font.Font(None, 36)
    texto_cronometro = fuente.render("Tiempo: " + str(tiempo_restante) + " s", True, (255, 255, 255))


    if tiempo_restante <= 0:
        
            font_game_over = pygame.font.Font(None, 100)
            texto_game_over = font_game_over.render("GAME OVER", True, (255, 0, 0))
            posicion_texto = texto_game_over.get_rect(center=(W // 2, H // 2))
            PANTALLA.blit(texto_game_over, posicion_texto)
            pygame.display.update()
            pygame.time.wait(3000)  # Esperar 3 segundos antes de salir del juego
            pygame.quit()
            sys.exit(0)

    


    if mi_personaje.rect.colliderect(mi_enemigo.rect):
        if not invulnerable and tiempo_actual - tiempo_ultimo_danio > tiempo_invulnerable:
            sonido_colision.play()
            mi_personaje.salud -= danio_enemigo
            tiempo_ultimo_danio = tiempo_actual
            invulnerable = True
            tiempo_inicio_invulnerable = tiempo_actual
            if mi_personaje.salud < 0:
                mi_personaje.salud = 0  # Establecer la salud mínima en 0
            else:
                # Reducir la salud en un valor específico en lugar de establecerla en 0
                mi_personaje.salud -= danio_reduccion_salud


    if not invulnerable or tiempo_actual - tiempo_inicio_invulnerable > duracion_invulnerabilidad:
        invulnerable = False

  
    if len(enemigos_group) > 0:
        mi_enemigo.detectar_colisiones_bala(mi_enemigo.balas, 1)
        enemigos_group.update(PANTALLA, lista_plataformas, mi_enemigo.balas, 1)
        mi_enemigo.dibujar(PANTALLA)

    if mi_enemigo.salud < 0:
            enemigos_group.remove(mi_enemigo)
            sprites.remove(mi_enemigo)
            mi_enemigo.morir()

    if mi_enemigo_2.salud < 0:
        enemigos_group.remove(mi_enemigo_2)
        sprites.remove(mi_enemigo_2)
        mi_enemigo_2.morir()


    if mi_personaje.rect.colliderect(mi_enemigo.rect):
        if not invulnerable and tiempo_actual - tiempo_ultimo_danio > tiempo_invulnerable:
            sonido_colision.play()
            mi_personaje.salud -= danio_enemigo
            tiempo_ultimo_danio = tiempo_actual
            invulnerable = True
            tiempo_inicio_invulnerable = tiempo_actual
            if mi_personaje.salud < 0:
                mi_personaje.salud = 0  # Establecer la salud mínima en 0
            else:
                # Reducir la salud en un valor específico en lugar de establecerla en 0
                mi_personaje.salud -= danio_reduccion_salud


    if not invulnerable or tiempo_actual - tiempo_inicio_invulnerable > duracion_invulnerabilidad:
        invulnerable = False
    if mi_personaje.salud < 0 : 
        mi_personaje.salud = 0 
        font_game_over = pygame.font.Font(None, 100)
        texto_game_over = font_game_over.render("GAME OVER", True, (255, 0, 0))
        posicion_texto = texto_game_over.get_rect(center=(W // 2, H // 2))
        PANTALLA.blit(texto_game_over, posicion_texto)
        pygame.display.update()
        pygame.time.wait(3000)  # Esperar 3 segundos antes de salir del juego
        pygame.quit()
        sys.exit(0)
    
    for bala in mi_enemigo.balas[:]:
        if bala.x < 0 or bala.x > W:
            mi_enemigo.balas.remove(bala)
    mi_enemigo.detectar_colisiones_bala(mi_enemigo.balas,1)

    lista_plataformas.append(plataforma2.obtener_lados())

    actualizar_pantalla(PANTALLA, mi_personaje, fondo, lista_plataformas, plataforma_imagen, plataforma_imagen_2,items_list)
    
    # Dibujar y actualizar enemigo
    mi_personaje.detectar_colisiones(lista_plataformas)
    enemigos_group.update(PANTALLA, lista_plataformas, mi_enemigo.balas,1)

    #deteccion de colisiones:
    mi_personaje.detectar_colisiones(lista_plataformas)
    mi_enemigo.detectar_colisiones(lista_plataformas)
 
    mi_personaje.dibujar(PANTALLA)
    mi_enemigo.dibujar(PANTALLA)
    mi_enemigo_2.dibujar(PANTALLA)
   
    fuente = pygame.font.Font(None, 36)  # Crea una fuente para el texto
    texto_puntaje = fuente.render("Puntaje: " + str(puntaje), True, (255, 255, 255))  # Renderiza el texto del puntaje
    PANTALLA.blit(texto_puntaje, (W - 200, 20))  # Dibuja el texto en la posición deseada (en este caso, en la esquina superior derecha)

    
    #CONDICION PARA PASAR DE NIVEL:
    if mi_enemigo.salud <= 0 and puntaje > 70:
        mensaje = fuente.render("PASASTE DE NIVEL", True, (255, 255, 255))
        posicion_mensaje = mensaje.get_rect(center=(W // 2, H // 2))
        PANTALLA.blit(mensaje, posicion_mensaje)
        pygame.display.update()
        pygame.time.wait(3000)
        pygame.quit()
        sys.exit(0)


    #dibujar rectangulos:
    
    for lado in lados_plataforma2:
        pygame.draw.rect(PANTALLA, "Green", lados_plataforma2[lado], 3)
    for lado in lados_plataforma3:
        pygame.draw.rect(PANTALLA, "Green", lados_plataforma3[lado], 3)
    
    pygame.draw.rect(PANTALLA, "Orange", piso, 3)
    pygame.draw.rect(PANTALLA, "Red", plataforma,3)
    pygame.draw.rect(PANTALLA,"Green", plataforma2, 3)
    pygame.draw.rect(PANTALLA,"Blue", item.rect, 3)
    
    for lado in mi_personaje.lados:
        pygame.draw.rect(PANTALLA,"Blue",mi_personaje.lados[lado],3)
    for bala in mi_personaje.balas:
        bala.update()
    redraw()
    PANTALLA.blit(texto_cronometro, (W - 200, 60))
 

    pygame.display.update()
 