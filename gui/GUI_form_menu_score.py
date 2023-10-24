import pygame
from pygame.locals import *

from gui.GUI_form import *
from gui.GUI_button import *
from gui.GUI_buttom_image import *
from gui.GUI_textbox import *
from gui.GUI_label import *
from gui.GUI_widget import *
from gui.GUI_slider import *

class FormMenuScore(Form):
    def __init__(self, screen, x, y, w, h, color_background, color_border, active, path_image, score, margen_y, margen_x, espacio):
        super().__init__(screen,x,y,w,h,color_background,color_border,active)

        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image, (w,h))

        self._slave = aux_image
        self._score = score

        self._margen_y = margen_y

        # Crear etiquetas de encabezado para cada columna
        column_width = (w - margen_x * 4) / 3  # Ancho de cada columna
        lbl_jugador = Label(self._slave, x=margen_x + 10, y=20, w=column_width, h=50,
                            text='Tiempo', font='Verdana', font_size=30, font_color='White',
                            path_image='gui/bar.png')
        lbl_enemigo = Label(self._slave, x=margen_x * 2 + column_width, y=20, w=column_width, h=50,
                            text='Personaje', font='Verdana', font_size=30, font_color='White',
                            path_image='gui/bar.png')
        lbl_tiempo = Label(self._slave, x=margen_x * 3 + column_width * 2, y=20, w=column_width, h=50,
                           text='Enemigo', font='Verdana', font_size=30, font_color='White',
                           path_image='gui/bar.png')

        self.lista_widgets.append(lbl_jugador)
        self.lista_widgets.append(lbl_enemigo)
        self.lista_widgets.append(lbl_tiempo)

        pos_inicial_y = margen_y

        for j in self._score:
            pos_inicial_x = margen_x
            for n, s in j.items():
                cadena = ''
                cadena = f'{s}'
                # Crear etiquetas de jugador en la columna correspondiente
                jugador = Label(self._slave, pos_inicial_x, pos_inicial_y, column_width, 100, cadena, 'Verdana',
                                30, 'White', 'gui\Table.png')
                self.lista_widgets.append(jugador)
                pos_inicial_x += column_width + margen_x
            pos_inicial_y += 100 + espacio

        self._btn_home = Button_Image(screen=self._slave,
                                      x=w - 70,
                                      y=h - 70,
                                      master_x=x,
                                      master_y=y,
                                      w=50,
                                      h=50,
                                      color_background=(250, 0, 0),
                                      color_border=(255, 0, 255),
                                      onclick=self._btn_home_click,
                                      onclick_param="",
                                      text="",
                                      font="Verdana",
                                      font_size=15,
                                      font_color=(0, 255, 0),
                                      path_image='gui\home.png')

        self.lista_widgets.append(self._btn_home)

    def _btn_home_click(self, param):
        self.end_dialog()

    def update(self, lista_eventos):
        if self.active:
            for wid in self.lista_widgets:
                wid.update(lista_eventos)
            self.draw()