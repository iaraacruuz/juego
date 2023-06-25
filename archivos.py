import pygame
import os


def reescalar_imagenes(lista_animaciones,W,H):
    for lista in lista_animaciones:
        for i in range(len(lista)):
            imagen= lista[i]
            lista[i]=pygame.transform.scale(imagen,(W,H))

def cargar_imagenes_archivo(lista,directorio):
    for archivo in os.listdir(directorio):
        lista.append(pygame.image.load(os.path.join(directorio, archivo)))


def girar_imagenes(lista_original,flip_x,flip_y):
    lista_girada=[]
    for imagen in lista_original:
        lista_girada.append(pygame.transform.flip(imagen,flip_x,flip_y))
    return lista_girada


def obtener_rectangulos(principal: pygame.Rect) ->dict:
    diccionario= {}
    #main - bottom- left - top- right(top parte de arriba del rect, bottom parte de abajo, right derecha left izq)
    diccionario["main"]= principal
    diccionario["bottom"]= pygame.Rect(principal.left,  principal.bottom - 10, principal.width,10)
    
    diccionario["right"]= pygame.Rect(principal.right -2, principal.top,2, principal.height)

    diccionario["left"]=  pygame.Rect(principal.left,principal.top,2,principal.height)
    diccionario["top"]= pygame.Rect(principal.left,principal.top, principal.width, 6)
    return diccionario