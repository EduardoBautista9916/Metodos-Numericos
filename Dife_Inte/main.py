from Dife_Inte.barras import *
from Dife_Inte.control import *
from Dife_Inte.impresion import *
from Dife_Inte.Dife_Inter import *
from os import system
import time

tabla = []
puntos =[]

def mainDif(punto):
    global puntos
    puntos = punto
    h=0
    intervalo = []
    integral = 0
    cant = 0
    repetir=True
    introduccion()
    while(repetir):
        while True:
            menuD_I()
            opcion = val_num()
            if opcion != 1 and opcion != 2 and opcion !=3:
                print("opcion Invalida")
                time.sleep(1)
            else:
                break
        if opcion==1:
            print("Ingrese el tamaño de paso h")
            h = val_num()
            print("Ingrese cuantos datos quiere")
            cant = int(val_num())
            puntos = llenarTabla(h, cant)
            imprimirDatos(puntos)
            system("pause")

        elif opcion == 2:
            #Diferenciacion
            interVal = False
            if len(puntos) == 0:
                print("No hay alguna tabla capturada.")
                print("Ingrese el tamaño de paso h")
                h = val_num()
                print("Ingrese cuantos datos quiere")
                cant = int(val_num())
                puntos = llenarTabla(h, cant)
                imprimirDatos(puntos)
                system("pause")
            else:
                h=(puntos[len(puntos)-1][0]-puntos[0][0])/(len(puntos)-1)
            while (not interVal):
                intervalo.clear()
                system("cls")
                print("Ingresa el intervalo de valores a los cuales desea sacar la Derivada:")
                print("Desde:")
                intervalo.append(val_num())
                print("Hasta:")
                intervalo.append(val_num())
                interVal=val_inter(intervalo, puntos)
            print(puntos)
            print(h)
            print(intervalo)
            tabla = diferenciacion(puntos,h,intervalo)
            system("cls")
            imprimirDer(puntos, tabla, intervalo,h)
            system("pause")
        elif opcion == 3:
            if len(puntos) == 0:
                print("No hay alguna tabla capturada.")
                print("Ingrese el tamaño de paso h")
                h = val_num()
                print("Ingrese cuantos datos quiere")
                cant = int(val_num())
                puntos = llenarTabla(h, cant)
                imprimirDatos(puntos)
                system("pause")
            else:
                h=(puntos[len(puntos)-1][0]-puntos[0][0])/(len(puntos)-1)
            system("cls")
            integral = integracion(puntos,h)
            print("El valor de la intgral numerica es de:", integral)
            system("pause")
            #integracion
        if opcion != 1:
            system("cls")
            print("Desea Realizar otra cosa?\n1.-si\n2.-no")
            opcion=val_num()
            if(opcion==1):
                system("cls")
                print("Desea cambiar con la misma tabla?\n 1.-si\n2.-no")
                opcion = val_num()
                if(opcion==1):
                    puntos=[]
                    repetir=True
            elif(opcion==2):
                repetir=False
            else:
                print("No entendi tu opcion, pero mejor terminamos hasta aqui...")
                time.sleep(1)
                repetir=False
    os.system("cls")
    print("      __^__                                      __^__")
    print("     ( ___ )************************************( ___ )")
    print("      |   |                                      |   |")
    print("      |   |           HASTA LA PROXIMA           |   |")
    print("      |   |                                      |   |")
    print("     ( ___ )************************************( ___ )")
    time.sleep(4)
    return puntos

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
    print("1.- Capturar Tabla", end="")
    espacios(76)
    barra(2)
    sl(1)
    barra(2)
    espacios(2)
    print("2.- Diferenciación Numerica", end="")
    espacios(67)
    barra(2)
    sl(1)
    barra(2)
    espacios(2)
    print("3.- Integración Numerica", end="")
    espacios(70)
    barra(2)
    sl(1)
    barra(100)
    sl(1)
    barra(100)
    sl(1)
    print("Elige una de las dos opciones")

#main([])