import pygame
from pygame.locals import *
from gui.GUI_widget import *

FPS = 18
    
class Button_Image(Widget):
    def __init__(self, screen,master_x,master_y, x,y,w,h, path_image,
                onclick=None, onclick_param=None, text="", font="Arial", font_size=12, font_color="Black",
                color_background = None, color_border = "Black", border_size = -1):
        super().__init__(screen, x,y,w,h,color_background,color_border, border_size)
        
        pygame.font.init()
        
        self._onclick = onclick
        self._onclick_param = onclick_param
        self._text = text
        self._font = pygame.font.SysFont(font,font_size)
        self._font_color = font_color
        self._master_x = master_x
        self._master_y = master_y
        
        aux_image = pygame.image.load(path_image)
        aux_image = pygame.transform.scale(aux_image,(w,h))
        self._slave = aux_image
        
        self.isclicked = False
        self.contador_click = 0
        
        self.render()
        
     