import os
from barras import*
from interpolacion import fun_tabla

def main():
    proceso(0.005)
    bienvenida()
    introduccion()
    fun_tabla()

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
    os.system("pause")
    os.system("cls")

def introduccion():
    os.system("cls")
    barra(100)
    sl(1)
    barra(2)
    espacios(1)
    print("Este programa está diseñado para la interpolacion de una valor dado una tabla de valores de ",end="")
    espacios(3)
    barra(2)
    sl(1)
    barra(2)
    espacios(1)
    print("x & y mediante el método de Diferencias ademas de el ajuste de curvas", end="")
    espacios(26)
    barra(2)
    sl(1)
    barra(100)
    sl(1)
    os.system("pause")
    os.system("cls")

main()