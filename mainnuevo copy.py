
import pygame,sys
from archivos2 import*
from animaciones2 import *
from class_personaje import *
from modo2 import *
from class_item import *
from class_plataforma import * 
from nivel_uno import NivelUno
from nivel_dos import NivelDos
from gui.GUI_form_principal import *
from gui.GUI_forn_prueba import *
import time
#PANTALLA:
W, H = 1200, 600
TAMAÑO= (W,H)
FPS = 10
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode(TAMAÑO)
tiempo_inicio = 0
tiempo_total = 60
# nivel_actual = NivelDos(PANTALLA,tiempo_inicio, tiempo_total)
form_prinicpal= FormPrueba(PANTALLA,200,150,900,350,"Gold","Magenta",5)
while True:
    RELOJ.tick(FPS)
    eventos=pygame.event.get()
    for evento in eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    
    # nivel_actual.update(eventos)
    form_prinicpal.update(eventos)



    pygame.display.update()
 