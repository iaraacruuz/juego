from pygame.locals import *
from nivel_uno import NivelUno
from nivel_dos import NivelDos
# from NivelTres import NivelTres
# from NivelCuatro import NivelCuatro

class ManejadorNiveles:
    def __init__(self,pantalla):
        self._slave = pantalla
        self.niveles = {"nivel_uno": NivelUno ,"nivel_dos": NivelDos}
           
        
    def get_nivel(self, nombre_nivel):
        return self.niveles[nombre_nivel](self._slave)
