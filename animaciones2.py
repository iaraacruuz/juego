<<<<<<< HEAD
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


personaje_quieto_2= [pygame.image.load("C:/pygame/Juego - copia (4) - copia/bombon/quieto/6.png") ]
personaje_camina_2=[
                pygame.image.load("C:/Users/PC/Desktop/Juego/bombon/movimiento/0.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/bombon/movimiento/1.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/bombon/movimiento/2.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/bombon/movimiento/3.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/bombon/movimiento/4.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/bombon/movimiento/5.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/bombon/movimiento/6.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/bombon/movimiento/7.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/bombon/movimiento/8.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/bombon/movimiento/11.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/bombon/movimiento/12.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/bombon/movimiento/14.png")]

personaje_salta_2=[pygame.image.load("C:/Users/PC/Desktop/Juego/bombon/salto/19.png"),
                 pygame.image.load("C:/Users/PC/Desktop/Juego/bombon/salto/35.png"),
                 pygame.image.load("C:/Users/PC/Desktop/Juego/bombon/salto/10.png")]

personaje_camina_izquierda_2= girar_imagenes(personaje_camina_2,True,False)
plataforma_imagen= pygame.image.load("C:/Users/PC/Desktop/Juego/plataforma5.png.png")
plataforma_imagen_2= pygame.image.load("C:/pygame/Juego - copia (4) - copia/plataforma6.png")

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

enemigo_camina_derecha_2=[pygame.image.load("C:/Users/PC/Desktop/Juego/him/2.png"),
                        pygame.image.load("C:/Users/PC/Desktop/Juego/him/3.png"),
                        pygame.image.load("C:/Users/PC/Desktop/Juego/him/4.png"),
                        pygame.image.load("C:/Users/PC/Desktop/Juego/him/5.png"),
                        pygame.image.load("C:/Users/PC/Desktop/Juego/him/6.png"),
                        pygame.image.load("C:/Users/PC/Desktop/Juego/him/7.png"),
                        pygame.image.load("C:/Users/PC/Desktop/Juego/him/8.png"),
                        pygame.image.load("C:/Users/PC/Desktop/Juego/him/9.png"),
                        pygame.image.load("C:/Users/PC/Desktop/Juego/him/14.png"),
                        pygame.image.load("C:/Users/PC/Desktop/Juego/him/32.png"),
                        pygame.image.load("C:/Users/PC/Desktop/Juego/him/33.png"),
                        pygame.image.load("C:/Users/PC/Desktop/Juego/him/55.png")] 

enemigo_camina_izquierda_2= girar_imagenes(enemigo_camina_derecha_2,True,False)

personaje_quieto_3= [pygame.image.load("C:/pygame/Juego - copia (4) - copia/burbuja/quieto/7.png") ]
personaje_camina_3=[
                pygame.image.load("C:/Users/PC/Desktop/Juego/burbuja/movimiento/0.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/burbuja/movimiento/1.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/burbuja/movimiento/2.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/burbuja/movimiento/3.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/burbuja/movimiento/4.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/burbuja/movimiento/5.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/burbuja/movimiento/6.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/burbuja/movimiento/8.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/burbuja/movimiento/9.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/burbuja/movimiento/11.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/burbuja/movimiento/13.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/burbuja/movimiento/14.png")]

personaje_salta_3=[pygame.image.load("C:/Users/PC/Desktop/Juego/burbuja/salto/10.png"),
                 pygame.image.load("C:/Users/PC/Desktop/Juego/burbuja/salto/12.png")]

personaje_camina_izquierda_3= girar_imagenes(personaje_camina_3,True,False)


enemigo_camina_derecha_3=[pygame.image.load("C:/pygame/Juego - copia (4) - copia/mojo jojo/camina/7.png"),
                        pygame.image.load("C:/pygame/Juego - copia (4) - copia/mojo jojo/camina/8.png"),
                        pygame.image.load("C:/pygame/Juego - copia (4) - copia/mojo jojo/camina/13.png"),
                        pygame.image.load("C:/pygame/Juego - copia (4) - copia/mojo jojo/camina/18.png"),
                        pygame.image.load("C:/pygame/Juego - copia (4) - copia/mojo jojo/camina/21.png"),
                        pygame.image.load("C:/pygame/Juego - copia (4) - copia/mojo jojo/camina/22.png"),
                        pygame.image.load("C:/pygame/Juego - copia (4) - copia/mojo jojo/camina/23.png")] 

enemigo_camina_izquierda_3= girar_imagenes(enemigo_camina_derecha_3,True,False)

=======
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


personaje_quieto_2= [pygame.image.load("C:/pygame/Juego - copia (4) - copia/bombon/quieto/6.png") ]
personaje_camina_2=[
                pygame.image.load("C:/Users/PC/Desktop/Juego/bombon/movimiento/0.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/bombon/movimiento/1.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/bombon/movimiento/2.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/bombon/movimiento/3.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/bombon/movimiento/4.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/bombon/movimiento/5.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/bombon/movimiento/6.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/bombon/movimiento/7.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/bombon/movimiento/8.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/bombon/movimiento/11.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/bombon/movimiento/12.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/bombon/movimiento/14.png")]

personaje_salta_2=[pygame.image.load("C:/Users/PC/Desktop/Juego/bombon/salto/19.png"),
                 pygame.image.load("C:/Users/PC/Desktop/Juego/bombon/salto/35.png"),
                 pygame.image.load("C:/Users/PC/Desktop/Juego/bombon/salto/10.png")]

personaje_camina_izquierda_2= girar_imagenes(personaje_camina_2,True,False)
plataforma_imagen= pygame.image.load("C:/Users/PC/Desktop/Juego/plataforma5.png.png")
plataforma_imagen_2= pygame.image.load("C:/pygame/Juego - copia (4) - copia/plataforma6.png")

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

enemigo_camina_derecha_2=[pygame.image.load("C:/Users/PC/Desktop/Juego/him/2.png"),
                        pygame.image.load("C:/Users/PC/Desktop/Juego/him/3.png"),
                        pygame.image.load("C:/Users/PC/Desktop/Juego/him/4.png"),
                        pygame.image.load("C:/Users/PC/Desktop/Juego/him/5.png"),
                        pygame.image.load("C:/Users/PC/Desktop/Juego/him/6.png"),
                        pygame.image.load("C:/Users/PC/Desktop/Juego/him/7.png"),
                        pygame.image.load("C:/Users/PC/Desktop/Juego/him/8.png"),
                        pygame.image.load("C:/Users/PC/Desktop/Juego/him/9.png"),
                        pygame.image.load("C:/Users/PC/Desktop/Juego/him/14.png"),
                        pygame.image.load("C:/Users/PC/Desktop/Juego/him/32.png"),
                        pygame.image.load("C:/Users/PC/Desktop/Juego/him/33.png"),
                        pygame.image.load("C:/Users/PC/Desktop/Juego/him/55.png")] 

enemigo_camina_izquierda_2= girar_imagenes(enemigo_camina_derecha_2,True,False)

personaje_quieto_3= [pygame.image.load("C:/pygame/Juego - copia (4) - copia/burbuja/quieto/7.png") ]
personaje_camina_3=[
                pygame.image.load("C:/Users/PC/Desktop/Juego/burbuja/movimiento/0.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/burbuja/movimiento/1.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/burbuja/movimiento/2.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/burbuja/movimiento/3.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/burbuja/movimiento/4.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/burbuja/movimiento/5.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/burbuja/movimiento/6.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/burbuja/movimiento/8.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/burbuja/movimiento/9.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/burbuja/movimiento/11.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/burbuja/movimiento/13.png"),
                pygame.image.load("C:/Users/PC/Desktop/Juego/burbuja/movimiento/14.png")]

personaje_salta_3=[pygame.image.load("C:/Users/PC/Desktop/Juego/burbuja/salto/10.png"),
                 pygame.image.load("C:/Users/PC/Desktop/Juego/burbuja/salto/12.png")]

personaje_camina_izquierda_3= girar_imagenes(personaje_camina_3,True,False)


enemigo_camina_derecha_3=[pygame.image.load("C:/pygame/Juego - copia (4) - copia/mojo jojo/camina/7.png"),
                        pygame.image.load("C:/pygame/Juego - copia (4) - copia/mojo jojo/camina/8.png"),
                        pygame.image.load("C:/pygame/Juego - copia (4) - copia/mojo jojo/camina/13.png"),
                        pygame.image.load("C:/pygame/Juego - copia (4) - copia/mojo jojo/camina/18.png"),
                        pygame.image.load("C:/pygame/Juego - copia (4) - copia/mojo jojo/camina/21.png"),
                        pygame.image.load("C:/pygame/Juego - copia (4) - copia/mojo jojo/camina/22.png"),
                        pygame.image.load("C:/pygame/Juego - copia (4) - copia/mojo jojo/camina/23.png")] 

enemigo_camina_izquierda_3= girar_imagenes(enemigo_camina_derecha_3,True,False)

>>>>>>> 52117411583005a06c67a216e64fbb0df54ceb61
posima_trampa= [pygame.image.load("C:/pygame/Juego - copia (4) - copia/posima.png")]