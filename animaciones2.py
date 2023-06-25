import pygame 
from archivos2 import *


personaje_quieto= [pygame.image.load("C:/Users/PC/Desktop/Juego/bellota/quieto/6.png") ]
personaje_camina=[
                pygame.image.load("C:/Users/PC/Desktop/Juego/bellota/movimiento/0.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/bellota/movimiento/1.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/bellota/movimiento/2.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/bellota/movimiento/3.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/bellota/movimiento/4.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/bellota/movimiento/5.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/bellota/movimiento/6.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/bellota/movimiento/7.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/bellota/movimiento/8.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/bellota/movimiento/9.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/bellota/movimiento/10.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/bellota/movimiento/11.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/bellota/movimiento/12.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/bellota/movimiento/14.png")]

personaje_salta=[pygame.image.load("C:/Users/PC/Desktop/Juego/bellota/salto/18.png"),
                 pygame.image.load("C:/Users/PC/Desktop/Juego/bellota/salto/19.png"),
                 pygame.image.load("C:/Users/PC/Desktop/Juego/bellota/salto/37.png")]

personaje_camina_izquierda= girar_imagenes(personaje_camina,True,False)

plataforma_imagen= pygame.image.load("C:/Users/PC/Desktop/Juego/plataforma5.png.png")

enemigo_camina_derecha=[pygame.image.load("C:/Users/PC/Desktop/Juego/snake/movimiento/4.png"),
                        pygame.image.load("C:/Users/PC/Desktop/Juego/snake/movimiento/5.png"),
                        pygame.image.load("C:/Users/PC/Desktop/Juego/snake/movimiento/6.png"),
                        pygame.image.load("C:/Users/PC/Desktop/Juego/snake/movimiento/7.png"),
                        pygame.image.load("C:/Users/PC/Desktop/Juego/snake/movimiento/8.png"),
                        pygame.image.load("C:/Users/PC/Desktop/Juego/snake/movimiento/10.png"),
                        pygame.image.load("C:/Users/PC/Desktop/Juego/snake/movimiento/11.png"),
                        pygame.image.load("C:/Users/PC/Desktop/Juego/snake/movimiento/12.png"),
                        pygame.image.load("C:/Users/PC/Desktop/Juego/snake/movimiento/31.png"),
                        pygame.image.load("C:/Users/PC/Desktop/Juego/snake/movimiento/32.png"),
                        pygame.image.load("C:/Users/PC/Desktop/Juego/snake/movimiento/33.png"),
                        pygame.image.load("C:/Users/PC/Desktop/Juego/snake/movimiento/34.png"),
                        pygame.image.load("C:/Users/PC/Desktop/Juego/snake/movimiento/35.png"),
                        pygame.image.load("C:/Users/PC/Desktop/Juego/snake/movimiento/36.png")] 

enemigo_camina_izquierda= girar_imagenes(enemigo_camina_derecha,True,False)