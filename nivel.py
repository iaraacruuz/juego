import pygame,sys
from archivos2 import*
from animaciones2 import *
from class_personaje import *
from modo2 import *
from class_item import *
from class_plataforma import * 
import time
# from mainnuevo import *
# from nivel_uno import NivelUno

class Nivel():
    def __init__(self,pantalla,W,H,personaje_principal: Personaje ,lista_plataformas,imagen_fondo, limite_izquierdo, limite_derecho,items_list, enemigo_principal: Enemigo, tiempo_inicio, tiempo_total):
        self._slave = pantalla
        self.ancho = W
        self.alto = H
        self.jugador = personaje_principal
        self.enemigo = enemigo_principal
        self.plataformas = lista_plataformas
        self.img_fondo = imagen_fondo
        self.velocidad = 5
        self.direccion = 0
        self.limite_izquierdo = limite_izquierdo
        self.limite_derecho = limite_derecho
        self.items = items_list
        self.tanda_balas = 0
        self.puntaje = 0
        self.tiempo_inicio = tiempo_inicio
        self.tiempo_total = tiempo_total
        self.danio_enemigo = 10
        self.invulnerable = False
        self.tiempo_ultimo_danio = pygame.time.get_ticks()
        self.duracion_invulnerabilidad = 2000
        self.tiempo_actual = 0
        self.sonido_colision = pygame.mixer.Sound("reaccion.mp3")
        self.sonido_golpe = pygame.mixer.Sound("golpe.mp3")
        self.sonido_bala = pygame.mixer.Sound("rayo.mp3")
        self.fuente = pygame.font.Font(None, 36)
        self.tamaño_plataforma = (200, 100)
        self.tamaño_plataforma2 = (250, 100)
        self.plataforma_imagen = pygame.image.load("plataforma5.png.png")
        self.plataforma_imagen = pygame.transform.scale(self.plataforma_imagen, self.tamaño_plataforma)
        self.plataforma_imagen_2 = pygame.image.load("plataforma5.png.png")
        self.plataforma= Plataforma(self.plataforma_imagen, 400, 460, self.tamaño_plataforma[0], self.tamaño_plataforma[1])
        self.plataforma2=Plataforma(self.plataforma_imagen_2, 600, 400, self.tamaño_plataforma2[0], self.tamaño_plataforma2[1])
        self.items_group= pygame.sprite.Group()
        self.enemigos_group = pygame.sprite.Group()
        self.piso= pygame.Rect(0,0,W,15)
        # self.plataformas = [self.plataforma, self.plataforma2]
        self.lados_plataforma = self.plataforma.obtener_lados()
        self.lados_plataforma2 = self.plataforma2.obtener_lados()
        self.piso.top= self.jugador.lados["main"].bottom
        self.lados_piso= obtener_rectangulos(self.piso)
        # self.lados= self.obtener_lados()



    def update(self,lista_eventos):
        tiempo_actual = pygame.time.get_ticks()
        tiempo_transcurrido = tiempo_actual - self.tiempo_inicio
        tiempo_restante = self.tiempo_total - int(tiempo_transcurrido)

        if tiempo_restante <= 0:
            font_game_over = pygame.font.Font(None, 100)
            texto_game_over = font_game_over.render("GAME OVER", True, (255, 0, 0))
            posicion_texto = texto_game_over.get_rect(center=(self.ancho // 2, self.alto // 2))
            self._slave.blit(texto_game_over, posicion_texto)
            pygame.display.update()
            pygame.time.wait(3000)
            pygame.quit()
            sys.exit(0)
        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_TAB:
                    cambiar_modo()        
                elif evento.key == pygame.K_SPACE:
                        self.jugador.lanzar_proyectil()
        
        self.leer_inputs()
        self.actualizar_pantalla(tiempo_restante)
        self.actualizar_tanda_balas()
        self.contacto_proyectil_villano()
        self.actualizar_enemigo()
        self.actualizar_items()
        self.actualizar_tiempo()
        self.detectar_colisiones()
        self.dibujar_rectangulos()
        self.dibujar_texto_puntaje()
        self.dibujar_texto_cronometro()
        # self.dibujar_personaje()
        # self.dibujar_enemigo()
        self.dibujar_items()
        self.dibujar_piso()
        self.comprobar_paso_nivel()
        self.detectar_colisiones_plataforma()
        self.detectar_colisiones_jugador()
        self.detectar_colisiones_enemigo()
        self.detectar_colisiones_bala_enemigo()
        self.detectar_colisiones_item()
        self.detectar_colisiones_enemigo_plataforma()
        self.detectar_colisiones_jugador_plataforma()
        self.detectar_colisiones_bala_jugador()
        self.detectar_colisiones_bala_enemigo()
        self.detectar_colisiones_bala_jugador_plataforma()
        self.detectar_colisiones_jugador_enemigo()
        self.detectar_colisiones_jugador_item()
        self.dibujar_personaje()
        self.dibujar_enemigo()

    
    
    def leer_inputs(self):
        keys = pygame.key.get_pressed() # Teclas presionadas
        self.direccion = 0
        if keys[pygame.K_RIGHT] and self.jugador.lados["main"].right + self.velocidad <= self.limite_derecho:
            self.jugador.que_hace = "derecha"
            self.jugador.direccion = "derecha"  # Establecer dirección como "derecha"
            if self.jugador.direccion == "derecha":
                self.direccion = 1
        elif keys[pygame.K_LEFT] and self.jugador.lados["main"].left - self.velocidad >= self.limite_izquierdo:
            self.jugador.que_hace = "izquierda"
            self.jugador.direccion = "izquierda"  # Establecer dirección como "izquierda"
            if self.jugador.direccion == "izquierda":
                self.direccion = -1
        elif keys[pygame.K_UP]:
            self.jugador.que_hace = "salta"
        else:
            self.jugador.que_hace = "quieto" # Si no se realiza ninguna acción, está quieto
            self.direccion = 0

    # def obtener_lados(self):
    #     lados = {}
    #     lados["top"] = pygame.Rect(self.rect.left, self.rect.top, self.rect.width, 1)
    #     lados["bottom"] = pygame.Rect(self.rect.left, self.rect.bottom, self.rect.width, 1)
    #     lados["left"] = pygame.Rect(self.rect.left, self.rect.top, 1, self.rect.height)
    #     lados["right"] = pygame.Rect(self.rect.right, self.rect.top, 1, self.rect.height)
    #     return lados


    def dibujar_rectangulos(self):

        for lado in self.jugador.lados:
            pygame.draw.rect(self._slave,"Blue",self.jugador.lados[lado],3)
    
        # # plataformas_group.draw(PANTALLA)
        # for self.plataforma in self.plataformas:
        #     for self.lado in self.plataforma.lados:
        #         pygame.draw.rect(self._slave, "Green", self.plataforma.lados[lado], 3)
        
        #         pygame.draw.rect(self._slave, "Red", self.plataforma,3)
        #         pygame.draw.rect(self._slave,"Green", self.plataforma2, 3)
        for item in self.items:
                pygame.draw.rect(self._slave,"Blue", item.rect, 3)



    
    def actualizar_pantalla( self, tiempo_restante):
        self._slave.blit(self.img_fondo, (0, 0))
        for plataforma in self.plataformas:
            self._slave.blit(plataforma_imagen, self.plataforma)
            self.img_fondo.blit(self.plataforma_imagen, self.plataforma2)
        self.jugador.update(self._slave, self.plataformas)
        font = pygame.font.Font(None, 36)  # Crea una fuente con el tamaño de 36
        self.puntaje_surface = font.render(str(self.puntaje), True, (255, 255, 255))  # Convierte el puntaje en una superficie de texto renderizada
        self._slave.blit(self.puntaje_surface, (200,10))
        font = pygame.font.Font(None, 36)  # Crea una fuente con el tamaño de 36
        tiempo_restante_surface = font.render(str(tiempo_restante), True, (255, 255, 255))  # Convierte el tiempo restante en una superficie de texto renderizada
        self._slave.blit(tiempo_restante_surface, (10, 10))  # Dibuja el tiempo restante en la posición (10, 10)
        # self.dibujar_piso()
        # self._slave.blit(str(tiempo_restante),(10,10))


        for item in self.items:
            item.draw(self._slave)
        



    def actualizar_tanda_balas(self):
        if self.tanda_balas > 0:
            self.tanda_balas += 1
        if self.tanda_balas > 3:
            self.tanda_balas = 0

        if self.tanda_balas == 1:
            for bala in self.jugador.balas:
                if len(self.jugador.balas) < 5:
                    x_bala = self.jugador.lados["main"].x + self.jugador.lados["main"].width // 2
                    self.jugador.balas.append(proyectiles(x_bala, self.jugador.lados["main"].y + self.jugador.alto // 2, 10, "Black", self.direccion))
                    self.sonido_bala.play()
                self.tanda_balas = 2

        for bala in self.jugador.balas:
            if bala.rect.colliderect(self.enemigo.rect):
                self.sonido_golpe.play()
                self.enemigo.salud -= 5
                self.jugador.balas.remove(bala)
            else:
                bala.update()

        for bala in self.jugador.balas:
            if bala.x < self.ancho and bala.x > 0:
                bala.x += bala.velocidad
            else:
                self.jugador.balas.remove(bala)

        if self.enemigo.salud < 0:
            self.enemigos_group.remove(self.enemigo)
            self.enemigo.morir()

    def contacto_proyectil_villano(self):
        self.enemigo.detectar_colisiones_bala(self.enemigo.balas, 1)

 
    def actualizar_enemigo(self):
        # for plataforma in self.plataformas:
            if self.enemigo.lados["main"].colliderect(self.plataforma.rect):
                self.enemigo.cambiar_direccion()

    def actualizar_items(self):
        self.items_group.update(self.plataformas)




    def detectar_colisiones(self):
        if self.enemigo.rect.colliderect(self.jugador.rect):
            self.sonido_colision.play()
            self.jugador.salud -= self.danio_enemigo
            self.tiempo_ultimo_danio = self.tiempo_actual
            self.invulnerable = True
            self.tiempo_inicio_invulnerable = self.tiempo_actual

        if not self.invulnerable or self.tiempo_actual - self.tiempo_inicio_invulnerable > self.duracion_invulnerabilidad:
            self.invulnerable = False

        if self.jugador.salud < 0:
           self.jugador.salud = 0

    def dibujar_texto_puntaje(self):
        fuente = pygame.font.Font(None, 36)
        texto_puntaje = fuente.render("Puntaje: " + str(self.puntaje), True, (255, 255, 255))
        self._slave.blit(texto_puntaje, (self.ancho - 200, 20))

    def dibujar_texto_cronometro(self):
        fuente = pygame.font.Font(None, 36)
        self.tiempo_transcurrido = time.time() - self.tiempo_inicio
        tiempo_restante = self.tiempo_total - int(self.tiempo_transcurrido)
        texto_cronometro = fuente.render("Tiempo: " + str(tiempo_restante) + " s", True, (255, 255, 255))
        self._slave.blit(texto_cronometro, (self.ancho - 200, 60))



    def dibujar_personaje(self):
        self.jugador.dibujar(self._slave)

    def dibujar_enemigo(self):
        self.enemigos_group.update(self._slave, self.plataformas, self.enemigo.balas, 1)
        self.enemigo.dibujar(self._slave)

    def dibujar_items(self):
        self.items_group.draw(self._slave)

    def dibujar_piso(self):
        pygame.draw.rect(self._slave, "Orange", self.piso, 3)

    def comprobar_paso_nivel(self):
        if self.enemigo.salud <= 0 and self.puntaje > 70:
            mensaje = self.fuente.render("PASASTE DE NIVEL", True, (255, 255, 255))
            posicion_mensaje = mensaje.get_rect(center=(self.ancho // 2, self.alto // 2))
            self._slave.blit(mensaje, posicion_mensaje)
            pygame.display.update()
            pygame.time.wait(3000)
            pygame.quit()
            sys.exit(0)

    def detectar_colisiones_plataforma(self):
        for plataforma in self.plataformas:
            if self.jugador.desplazamiento_X > 0 and self.jugador.lados["right"].colliderect(plataforma.rect) and \
                    self.jugador.lados["bottom"].right > plataforma.rect.left and \
                    self.jugador.lados["top"].bottom > plataforma.rect.top and \
                    self.jugador.lados["bottom"].top < plataforma.rect.bottom:
                self.jugador.lados["main"].right = plataforma.rect.left
            elif self.jugador.desplazamiento_X < 0 and self.jugador.lados["left"].colliderect(plataforma.rect) and \
                    self.jugador.lados["bottom"].left < plataforma.rect.right and \
                    self.jugador.lados["top"].bottom > plataforma.rect.top and \
                    self.jugador.lados["bottom"].top < plataforma.rect.bottom:
                self.jugador.lados["main"].left = plataforma.rect.right

    def detectar_colisiones_jugador(self):
        self.jugador.detectar_colisiones(self.plataformas)

    def detectar_colisiones_enemigo(self):
        self.enemigo.detectar_colisiones(self.plataformas)

    def detectar_colisiones_bala_enemigo(self):
        for bala in self.jugador.balas:
            if bala.rect.colliderect(self.enemigo.rect):
                self.sonido_golpe.play()
                self.enemigo.salud -= 5
                self.jugador.balas.remove(bala)

    def detectar_colisiones_item(self):
        for item in self.items:
            self.puntaje = item.check_collision(self.jugador, self.puntaje)
            item.update()
            item.draw(self._slave)
            if item.recogido:
                self.items.remove(item)

    def detectar_colisiones_enemigo_plataforma(self):
        if self.enemigo.rect.left <= self.limite_izquierdo or self.enemigo.rect.right >= self.limite_derecho:
            self.enemigo.cambiar_direccion()

    def detectar_colisiones_jugador_plataforma(self):
        # for plataforma in self.plataformas:
            if self.jugador.lados["main"].colliderect(self.plataforma.rect):
                self.jugador.detectar_colisiones()

    def detectar_colisiones_bala_jugador(self):
        for bala in self.jugador.balas:
            if bala.x < self.ancho and bala.x > 0:
                bala.x += bala.velocidad
            else:
                self.jugador.balas.remove(bala)

    def detectar_colisiones_bala_enemigo(self):
        for bala in self.jugador.balas:
            if bala.rect.colliderect(self.enemigo.rect):
                self.sonido_golpe.play()
                self.enemigo.salud -= 5
                self.jugador.balas.remove(bala)

    def detectar_colisiones_bala_jugador_plataforma(self):
        for bala in self.jugador.balas:
            if bala.rect.colliderect(self.plataforma.rect):
                self.jugador.balas.remove(bala)

    def detectar_colisiones_jugador_enemigo(self):
        if self.jugador.rect.colliderect(self.enemigo.rect):
            self.sonido_colision.play()
            self.jugador.salud -= self.danio_enemigo
            self.tiempo_ultimo_danio = self.tiempo_actual
            self.invulnerable = True
            self.tiempo_inicio_invulnerable = self.tiempo_actual

    def detectar_colisiones_jugador_item(self):
        for item in self.items:
            if self.jugador.rect.colliderect(item.rect):
                self.puntaje = item.check_collision(self.jugador, self.puntaje)
                item.update()
                item.draw(self._slave)
                if item.recogido:
                    self.items.remove(item)

    # def dibujar_rectangulos(self):
    #     for lado in self.jugador.lados:
    #         pygame.draw.rect(self._slave, "Blue", self.jugador.lados[lado], 3)

    #     for plataforma in self.plataformas:
    #         for lado in plataforma.lados:
    #             pygame.draw.rect(self._slave, "Green", plataforma.lados[lado], 3)

    #     pygame.draw.rect(self._slave, "Red", plataforma, 3)

    def actualizar_tiempo(self):
        fuente = pygame.font.Font(None, 36)
        tiempo_transcurrido = time.time() - self.tiempo_inicio
        tiempo_restante = self.tiempo_total - int(tiempo_transcurrido)
        texto_cronometro = fuente.render("Tiempo: " + str(tiempo_restante) + " s", True, (255, 255, 255))
        self._slave.blit(texto_cronometro, (self.ancho - 200, 60))