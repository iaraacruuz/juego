import pygame
from archivos import *

personaje_quieto=[]


cargar_imagenes_archivo(personaje_quieto, "bellota/quieto")



personaje_camina= []

cargar_imagenes_archivo(personaje_camina, "bellota/movimiento")

personaje_salta=[]
cargar_imagenes_archivo(personaje_salta,"bellota/salto")
personaje_camina_izquierda= girar_imagenes(personaje_camina,True,False)

enemigo_camina= []
cargar_imagenes_archivo(enemigo_camina,"snake\movimiento")

