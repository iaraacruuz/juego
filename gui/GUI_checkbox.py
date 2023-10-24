import pygame
from pygame.locals import *
from gui.GUI_widget import *

FPS = 18
    

class CheckBox(Widget):
    """
    Clase que representa un checkbox en una interfaz gráfica.
    Hereda de la clase Widget.
    """
    def __init__(self, screen,master_x,master_y, x,y,w,h, path_image_on, path_image_off):
        super().__init__(screen, x,y,w,h)
        """
        Inicializa una instancia de CheckBox.

        Argumentos:
        - screen: La superficie de la pantalla donde se dibujará el checkbox.
        - master_x: Coordenada x del punto de referencia de la superficie contenedora respecto a la pantalla.
        - master_y: Coordenada y del punto de referencia de la superficie contenedora respecto a la pantalla.
        - x: Coordenada x del punto de referencia del widget en la superficie dada.
        - y: Coordenada y del punto de referencia del widget en la superficie dada.
        - w: Ancho del checkbox.
        - h: Altura del checkbox.
        - path_image_on: Ruta de la imagen para el estado activado del checkbox.
        - path_image_off: Ruta de la imagen para el estado desactivado del checkbox.
        """
        
        self.esta_prendido = False
        self._master_x = master_x
        self._master_y = master_y
        
        aux_image_on = pygame.image.load(path_image_on)
        aux_image_on = pygame.transform.scale(aux_image_on,(w,h))
        self.image_on = aux_image_on

        aux_image_off = pygame.image.load(path_image_off)
        aux_image_off = pygame.transform.scale(aux_image_off,(w,h))
        self.image_off = aux_image_off

        self._slave = self.image_off
        
        self.isclicked = False
        self.contador_click = 0
        
        self.render()
        
     
 
    def render(self):
        self.slave_rect = self._slave.get_rect()

        self.slave_rect.x = self._x
        self.slave_rect.y = self._y
        
        self.slave_rect_collide = pygame.Rect(self.slave_rect)
        self.slave_rect_collide.x += self._master_x
        self.slave_rect_collide.y += self._master_y
    
    def update(self, lista_eventos):
        
        self.isclicked = False
        if self.contador_click > FPS/2:
            
            for evento in lista_eventos:
                if evento.type == pygame.MOUSEBUTTONDOWN:
                    if self.slave_rect_collide.collidepoint(evento.pos):
                        self.esta_prendido = not self.esta_prendido
                        self.contador_click = 0
        else:
            self.contador_click += 1
        
        if self.esta_prendido:
            self._slave = self.image_on
        else:
            self._slave = self.image_off

        self.draw()

    def get_esta_prendido(self):
        return self.esta_prendido