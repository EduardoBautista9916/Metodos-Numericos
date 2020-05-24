import os
import time
from NewtonRapshon.fun_newton import val_num
from NewtonRapshon.main import mainNew
from interpolacion.main import mainInter
from Dife_Inte.main import mainDif
from NewtonRapshon.barras import *

puntos=[]

def menuPrincipal(puntos):
    opcion=0
    repetir = True
    proceso(0.001)
    bienvenida()
    introduccion()
    while repetir:
        os.system("cls")
        menuInicio()
        opcion=val_num()
        if opcion ==1:
            #Ecuaciones no lineales
            mainNew()
            repetir = False
            pass
        elif opcion == 2:
            puntos=mainInter(puntos)
            #Interpolacion y Ajuste de Curvas
            repetir = False
            pass
        elif opcion == 3:
            #Diferenciacion e Interpolacion
            puntos=mainDif(puntos)
            repetir = False
            pass
        elif opcion == 4:
            #Salir
            repetir = False
            pass
        else:
            #Valor no Encontrado
            print("Esa opcion no esta disponible")
            time.sleep(1)
            repetir=True
            pass
    pass

def menuInicio():
    barra(100)
    sl(1)
    barra(43)
    print("MENU PRINCIPAL", end="")
    barra(43)
    sl(1)
    barra(100)
    sl(1)
    barra(2)
    espacios(96)
    barra(2)
    sl(1)
    barra(2)
    espacios(1)
    print("1.- Sistemas de Ecuaciones no Lineales",end="")
    espacios(57)
    barra(2)
    sl(1)
    barra(2)
    espacios(1)
    print("2.- Interpolacion y Ajuste de Curvas",end="")
    espacios(59)
    barra(2)
    sl(1)
    barra(2)
    espacios(1)
    print("3.- Diferenciacion e Integracion",end="")
    espacios(63)
    barra(2)
    sl(1)
    barra(2)
    espacios(1)
    print("4.- Salir",end="")
    espacios(86)
    barra(2)
    sl(1)
    barra(100)
    sl(1)
    barra(100)
    sl(1)
    print("Elije una de las tres opciones")

def introduccion():
    os.system("cls")
    barra(100)
    sl(1)
    barra(2)
    espacios(2)
    print("El siguiente programa es el conjunto de todos los programas que se realizaron a lo largo del", end="")
    espacios(2)
    barra(2)
    sl(1)
    barra(2)
    espacios(2)
    print("curso de Metodos Numericos II", end="")
    espacios(65)
    barra(2)
    sl(1)
    barra(100)
    sl(1)
    os.system("pause")

def bienvenida():
    os.system("cls")
    barra(100)
    sl(1)
    barra(45)
    print("BIENVENIDO", end="")
    barra(45)
    sl(1)
    barra(100)
    sl(1)
    barra(2)
    espacios(29)
    print("UNIVERSIDAD NACIONAL AUTÓNOMA DE MÉXICO",end="")
    espacios(28)
    barra(2)
    sl(1)
    barra(2)
    espacios(29)
    print("FACULTAD DE ESTUDIOS SUPERIORES ACATLÁN", end="")
    espacios(28) 
    barra(2) 
    sl(1)
    barra(2)
    espacios(38)
    print("MÉTODOS NUMÉRICOS II",end="")
    espacios(38)
    barra(2)
    sl(1)
    barra(2)
    espacios(96)
    barra(2)
    sl(1)
    barra(2)
    espacios(5)
    print("Miembros del equipo:", end="")
    espacios(71)
    barra(2)
    sl(1)
    barra(2)
    espacios(10)
    print("-Álvarez Cortes Kevin Alejandro", end="")
    espacios(55)
    barra(2)
    sl(1)
    barra(2)
    espacios(10)
    print("-Bautista Gaona Luis Eduardo",end="")
    espacios(58)
    barra(2)
    sl(1)
    barra(2)
    espacios(10)
    print("-De la Peña Estrada Valerie Samantha", end="")
    espacios(50)
    barra(2)
    sl(1)
    barra(2)
    espacios(10)
    print("-Ortiz Flores Diana Michelle", end="")
    espacios(58)
    barra(2)
    sl(1)
    barra(100)
    sl(1)
    os.system("pause")
    os.system("cls")



menuPrincipal(puntos)