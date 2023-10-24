import pygame
import pygame.locals

from gui.GUI_form import *
from gui.GUI_buttom_image import *

class ContenedorNivel(Form):
    def __init__(self, pantalla: pygame.Surface, nivel):
        super().__init__(pantalla, 0, 0, pantalla.get_width(), pantalla.get_height(), color_background='sakjs')
        nivel._slave = self._slave
        self.nivel = nivel
        self._btn_home = Button_Image(screen=self._slave,
                                        master_x = self._x,
                                        master_y = self._y,
                                        x = self._w - 100,
                                        y = self._h - 100,
                                        w = 50,
                                        h = 50,
                                        color_background= (250,0,0),
                                        color_border= (255,0,255),
                                        onclick= self.btn_home_click,
                                        onclick_param= "",
                                        text= "",
                                        font= "Verdana",
                                        font_size= 15,
                                        font_color= (0,255,0),
                                        path_image= 'gui\home.png' )
        self.lista_widgets.append(self._btn_home)

    def update(self, lista_evento):
        self.nivel.update(lista_evento)
        for widget in self.lista_widgets:
            widget.update(lista_evento)
        self.draw()
    def btn_home_click(self,param):
        self.end_dialog()
        