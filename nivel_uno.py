import pygame,sys
from archivos2 import*
from animaciones2 import *
from class_personaje import *
from modo2 import *
from class_item import *
from class_trampa import * 
from class_plataforma import * 
from nivel import Nivel

class NivelUno(Nivel):
    def __init__(self,pantalla: pygame.Surface,tiempo_inicio, tiempo_total):
        
        W= pantalla.get_width()
        H= pantalla.get_height()
        # Fondo  
        fondo = pygame.image.load("ciudad3.jpg")
        fondo = pygame.transform.scale(fondo, (W,H))


        pygame.init() 

        #CRONOMETRO:
        import time

        tiempo_inicio = time.time()  # Tiempo de inicio del cronómetro
        tiempo_total = 60  # Duración total del cronómetro en segundos

        #PUNTAJE:
        self.puntaje = 0
        #INVULNERABILIDAD:

        invulnerable = False
        tiempo_invulnerable = 1000  # Tiempo en milisegundos (ejemplo: 1000 = 1 segundo)
        tiempo_ultimo_danio = pygame.time.get_ticks()  # Obtén el tiempo actual en milisegundos

        # # ITEMS:

        self.items_group = pygame.sprite.Group()
        item_image = pygame.image.load("15.png")  # Replace with the actual image path
        item_image = pygame.transform.scale(item_image, (50, 50))  # Replace the size with your desired dimensions

        min_x, max_x = 5, W  # Rango de coordenadas X
        min_y, max_y = int(H * 0.4), int(H * 0.6)  # Rango de coordenadas Y ajustado
        num_items = 10  # Número de items que deseas generar

        
        items_list = Item.generar_items(num_items, min_x, max_x, min_y, max_y, item_image)
        ###############################################################
        # #TRAMPA:
        # trampa_group = pygame.sprite.Group()
        # trampa_image = pygame.image.load("posimaa.png") 
        # trampa_image = pygame.transform.scale(trampa_image, (40, 40))  # Replace the size with your desired dimensions

        # min_x, max_x = 5, W  # Rango de coordenadas X
        # min_y, max_y = int(H * 0.4), int(H * 0.6)  # Rango de coordenadas Y ajustado
        # num_trampa = 2  # Numero de items que desea generar

        # trampa_list = Trampa.generar_trampa(num_trampa, min_x, max_x, min_y, max_y, trampa_image)
        # trampa_group.add(trampa_list)

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
        self.enemigos_group = pygame.sprite.Group()
        self.sprites = pygame.sprite.Group()
        posicion_enemigo = (H/2 - 100, 500)  # Cambia la posición según tus necesidades
        tamaño_enemigo = (75, 85)  # Cambia el tamaño según tus necesidades
        diccionario_animaciones_enemigo = {}
        diccionario_animaciones_enemigo["camina_derecha"] = enemigo_camina_derecha
        diccionario_animaciones_enemigo["camina_izquierda"] = enemigo_camina_izquierda

        mi_enemigo = Enemigo(tamaño_enemigo, diccionario_animaciones_enemigo, posicion_enemigo, 7)  # Cambia la velocidad según tus necesidades
        self.enemigos_group.add(mi_enemigo)

        #PISO:
        piso= pygame.Rect(0,0,W,15)
        piso.top= mi_personaje.lados["main"].bottom
        lados_piso= obtener_rectangulos(piso)


        #############################################################################
        tamaño_plataforma = (200, 100)
        tamaño_plataforma2 = (250, 100)

        plataforma_imagen = pygame.image.load("plataforma5.png.png")
        plataforma_imagen = pygame.transform.scale(plataforma_imagen, tamaño_plataforma)

        plataforma = Plataforma(plataforma_imagen, 400, 460, tamaño_plataforma[0], tamaño_plataforma[1])

        plataforma_imagen_2 = pygame.image.load("plataforma5.png.png")
        plataforma_imagen_2 = pygame.transform.scale(plataforma_imagen_2, tamaño_plataforma2)

        plataforma2 = Plataforma(plataforma_imagen_2, 600, 400, tamaño_plataforma2[0], tamaño_plataforma2[1])
        lados_plataforma = plataforma.obtener_lados()
        lados_plataforma2 = plataforma2.obtener_lados()
        lista_plataformas = [lados_piso, lados_plataforma, lados_plataforma2]
        #############################################################################

        #################################################################
        #LIMITES:
        limite_izquierdo = 0
        limite_derecho = W - mi_personaje.lados["main"].width
        velocidad = 5
        #BALAS:
        tanda_balas=0
        self.bullets=[]
        ruta_musica_bala= "rayo.mp3"
        self.sonido_bala= pygame.mixer.Sound(ruta_musica_bala)
        ruta_golpe="golpe.mp3"
        self.sonido_golpe=pygame.mixer.Sound(ruta_golpe)
        #############################

        self.balas=[]

        def redraw():
            for bala in mi_personaje.balas:
                pygame.draw.rect(pantalla, (255, 0, 0), bala.rect)
                bala.update()

            pygame.display.update()

        #MUSICA FONDO:
        # ruta_musica= "musica.mp3"
        # self.musica_fondo= pygame.mixer.music.load(ruta_musica)

        # pygame.mixer.music.play(-1)

        #Musica Golpe PERSONAJE:
        ruta_colision = "reaccion.mp3"
        self.sonido_colision = pygame.mixer.Sound(ruta_colision)

        #####################
        limite_izquierdo = 0
        limite_derecho = W - mi_enemigo.lados["main"].width
        if tanda_balas == 0:
            tanda_balas = 1
        #########################
 
        #######################
        self.tiempo_ultimo_danio = pygame.time.get_ticks()  # Obtén el tiempo actual en milisegundos

        self.danio_enemigo = 10

        self.tiempo_inicio_invulnerable = 0
        self.duracion_invulnerabilidad = 100

        # super().update(lista_eventos)
        #############################################
        super().__init__(pantalla, W, H, mi_personaje, lista_plataformas, fondo, limite_izquierdo, limite_derecho, items_list, mi_enemigo, tiempo_inicio, tiempo_total)

