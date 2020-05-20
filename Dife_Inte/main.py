from recursos.barras import *
from recursos.control import *
from recursos.impresion import *
from Dife_Inter import *
from os import system
import time

tabla = []
puntos =[]

def main(punto):
    puntos = punto
    h=0
    intervalo = []
    bienvenida()
    introduccion()
    if len(puntos) == 0:
        print("No hay alguna tabla capturada.")
        print("Ingrese el tamaño de paso h")
        h = val_num()
        puntos = llenarTabla(h)
        imprimirDatos(puntos)
        system("pause")
    while True:
        menuD_I()
        opcion = val_num()
        if opcion != 1 and opcion != 2:
            print("opcion Invalida")
            time.sleep(1)
        else:
            break
    if opcion == 1:
        #Diferenciacion
        interVal = False
        while (not interVal):
            intervalo.clear()
            print("Ingresa el intervalo de valores a los cuales desea sacar la Derivada:")
            print("Desde:")
            intervalo.append(val_num())
            print("Hasta:")
            intervalo.append(val_num())
            interVal=val_inter(intervalo, puntos)
        tabla = diferenciacion(puntos,h,intervalo)
        print(tabla)
        pass
    elif opcion == 2:
        #integracion
        pass

def bienvenida():
    system("cls")
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
    espacios(23)
    print("MÉTODO DE INTERPOLACION POR DIFERENCIAS DIVIDIDAS",end="")
    espacios(24)
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
    system("pause")
    system("cls")

def introduccion():
    system("cls")
    barra(100)
    sl(1)
    barra(2)
    espacios(1)
    print("Este programa esta diseñado para calcular la diferenciacion numerica realizada mediante la", end="")
    espacios(5)
    barra(2)
    sl(1)
    barra(2)
    espacios(1)
    print("formula de diferencias centradas y la interpolacion nuerica mediante la regla de simpson 1/3 o", end="")
    espacios(1)
    barra(2)
    sl(1)
    barra(2)
    espacios(1)
    print("simpson 3/8 segun se nesecite.", end="")
    espacios(65)
    barra(2)
    sl(1)
    barra(100)
    sl(1)
    system("pause")
    system("cls")

def menuD_I():
    system("cls")
    barra(100)
    sl(1)
    barra(48)
    print("MENÚ", end="")
    barra(48)
    sl(1)
    barra(100)
    sl(1)
    barra(2)
    espacios(2)
    print("1.- Diferenciación Numerica", end="")
    espacios(67)
    barra(2)
    sl(1)
    barra(2)
    espacios(2)
    print("2.- Integración Numerica", end="")
    espacios(70)
    barra(2)
    sl(1)
    barra(100)
    sl(1)
    barra(100)
    sl(1)
    print("Elige una de las dos opciones")

main([[1,1], [2,4], [3,9], [4, 16], [5,25], [6,36]])