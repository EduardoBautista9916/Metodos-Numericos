import os
import time
import math
import sys
sys.path.append("..")
from NewtonRapshon.impresion import *#imprimir2, imprimir3, cabMet2, cabMet3, cabeceraS1, cabeceraS2, cabeceraS3, cabeceraS4, foter2, foter3
from NewtonRapshon.barras import *
# funcion que valida que entren valores numericos
def val_num():
    try:
        digit= float(input(">"))
    except(ValueError):
        os.system("cls")
        barra(100)
        sl(1)
        barra(42)
        print("VALOR NO VALIDO", end="")
        barra(43)
        sl(1)
        barra(100)
        sl(1)
        digit=val_num()
    return digit

# funcion que da el menu de el metodo de newthon 
def menu_newton():
    menu()
    itera = 0
    option = val_num()
    if(option !=1 and option != 4 and option != 2 and option != 3):
        print("opcion no valida")
        time.sleep(3)
    def sistem_1():
        first_sistem(itera)
    def sistem_2():
        second_sistem(itera)
    def sistem_3():
        third_sistem(itera)
    def sistem_4():
        fourth_sistem(itera)
    dict = {
        1 : sistem_1,
        2 : sistem_2,
        3 : sistem_3,
        4 : sistem_4
    }
    dict.get(option,menu_newton)()

# funcion que resulve el primer siste made ecuaciones    
def first_sistem(itera):
    os.system("cls")
    print("Digita el valor inicial para x ")
    x= val_num()
    print("Digita el valor inicial para y ")
    y = val_num()
    print("Digita el numero de iteraciones deseadas")
    itera_des = val_num()
    print("Digita la tolerancia minima a alcanzar")
    tolerancia = val_num()
    os.system("cls")
    cabMet2()
    cabeceraS1()
    while itera < itera_des:
        fx = [(x*x)+(x*y)-10,y+(3*x*y*y)-50]
        jaco = [[(2*x)+y , x],[3*y*y , (6*x*y)+1]]
        p1_error = [x,y]
        jaco_inv = op_jaco2(jaco)
        if(jaco_inv == 1):
            break
        x = x - ((fx[0]*jaco_inv[0][0]) + (fx[1]*jaco_inv[0][1]))
        y = y - ((fx[0]*jaco_inv[1][0]) + (fx[1]*jaco_inv[1][1]))
        if(itera == 0 ):
            error= 0
        elif(x-p1_error[0]>y-p1_error[1]):
            error = abs(x-p1_error[0])
        else:
            error = abs(y-p1_error[1])
        parar=imprimir2(itera,p1_error,fx,jaco,jaco_inv,error)
        if(error < tolerancia and error != 0):
            foter2()
            sl(1)
            print(" La aproximacion es: ")
            print(" x = ",end="") 
            formatNum(p1_error[0])
            sl(1)
            print(" y = ",end="")
            formatNum(p1_error[1])
            sl(1)
            break
        elif(parar):
            print("No se puede continuar debido a que los números se han desbordado y ya no caben en la Tabla")
            break
        itera += 1
        if(itera == itera_des):
            if(error > 1):
                foter2()
                sl(1)
                print("************aproximacion no encontrada***********")
            else:
                foter2()
                sl(1)
                print(" La aproximacion es: ")
                print(" x = ",end="") 
                formatNum(p1_error[0])
                sl(1)
                print(" y = ",end="")
                formatNum(p1_error[1])
                sl(1)
    time.sleep(5)
    exit()        

# funcion que resuelve el segundo sistema de ecuaciones        
def second_sistem(itera):
    os.system("cls")
    print("Digita el valor inicial para x ")
    x = val_num()
    print("Digita el valor inicial para y ")
    y = val_num()
    print("Digita el numero de iteraciones deseadas")
    itera_des = val_num()
    print("Digita la tolerancia minima a alcanzar")
    tolerancia = val_num()
    os.system("cls")
    cabMet2()
    cabeceraS2()
    while itera < itera_des:
        fx = [(x*x)+(y*y)-9,-((math.e)**x)-(2*y)-3]
        jaco = [[2*x,-((math.e)**x)],[2*y,-2]]
        p1_error = [x,y]
        jaco_inv = op_jaco2(jaco)
        if(jaco_inv == 1):
            break
        x = x - ((fx[0]*jaco_inv[0][0]) + (fx[1]*jaco_inv[0][1]))
        y = y - ((fx[0]*jaco_inv[1][0]) + (fx[1]*jaco_inv[1][1]))
        if(itera == 0 ):
             error= 0
        elif(x-p1_error[0]>y-p1_error[1]):
            error = abs(x-p1_error[0])
        else:
            error = abs(y-p1_error[1])
        imprimir2(itera,p1_error,fx,jaco,jaco_inv,error)
        if(error < tolerancia and error != 0):
            foter2()
            sl(1)
            print(" La aproximacion es: ")
            print(" x = ",end="") 
            formatNum(p1_error[0])
            sl(1)
            print(" y = ",end="")
            formatNum(p1_error[1])
            sl(1)
            break
        itera += 1
        if(itera == itera_des):
            if(error > 1):
                foter2()
                sl(1)
                print("************aproximacion no encontrada***********")
            else:
                foter2()
                sl(1)
                print(" La aproximacion es: ")
                print(" x = ",end="") 
                formatNum(p1_error[0])
                sl(1)
                print(" y = ",end="")
                formatNum(p1_error[1])
                sl(1)
    time.sleep(5)
    exit()

# funcion que resuelve el tercero sistema de ecuaciones
def third_sistem(itera):
    os.system("cls")
    print("Digita el valor inicial para x ")
    x = val_num()
    print("Digita el valor inicial para y ")
    y = val_num()
    print("Digita el valor para z ")
    z = val_num()
    print("Digita el numero de iteraciones deseadas")
    itera_des = val_num()
    print("Digita la tolerancia a alcanzar")
    tolerancia = val_num()
    os.system("cls")
    cabMet3()
    cabeceraS3()
    while itera < itera_des:
        fx = [(2*x*x)-(4*x)+(y*y)+(3*z*z)+(6*z)+2,(x*x)+(y*y)-(2*y)+(2*z*z)-5,(3*x*x)-(12*x)+(y*y)-(3*z*z)+8]
        jaco = [[(4*x)-4,2*y,(6*z)+6],[2*x,(2*y)-2,4*z],[(6*x)-12,2*y,-(6*z)]]
        p1_error = [x,y,z]
        jaco_inv = op_jaco3(jaco)
        if(jaco_inv==1):
            break
        x = x - ((fx[0]*jaco_inv[0][0]) + (fx[1]*jaco_inv[0][1]) + (fx[2]*jaco_inv[0][2]))
        y = y - ((fx[0]*jaco_inv[1][0]) + (fx[1]*jaco_inv[1][1]) + (fx[2]*jaco_inv[1][2]))
        z = z - ((fx[0]*jaco_inv[2][0]) + (fx[1]*jaco_inv[2][1]) + (fx[2]*jaco_inv[2][2]))
        if(itera == 0):
            error = 0
        elif((x-p1_error[0] > y-p1_error[1]) and (x-p1_error[0] > z-p1_error[2])):
            error = abs(x-p1_error[0])
        elif((y-p1_error[1]>x-p1_error[0])and (y-p1_error[1]> z-p1_error[2])):
            error = abs(y-p1_error[1])
        else:
            error = abs(z-p1_error[2])
        imprimir3(itera,p1_error,fx,jaco,jaco_inv,error)
        if(error < tolerancia and error != 0):
            foter3()
            print(" ")
            print(" La aproximacion es: ")
            print(" x = ",end="") 
            formatNum(p1_error[0])
            sl(1)
            print(" y = ",end="")
            formatNum(p1_error[1])
            sl(1)
            print(" z = ",end="")
            formatNum(p1_error[2])
            sl(1)
            break
        itera += 1
        if(itera == itera_des):
            if(error > 1):
                foter3()
                sl(1)
                print("************aproximacion no encontrada***********")
            else:
                foter3()
                sl(1)
                print(" La aproximacion es: ")
                print(" x = ",end="") 
                formatNum(p1_error[0])
                sl(1)
                print(" y = ",end="")
                formatNum(p1_error[1])
                sl(1)
                print(" z = ",end="")
                formatNum(p1_error[2])
                sl(1)
    time.sleep(5)
    exit()

# funcion que resuelve el cuarto sistema de secuaciones
def fourth_sistem(itera):
    os.system("cls")
    print("Digita el valor para x ")
    x = val_num()
    print("Digita el valor inicial para y ")
    y = val_num()
    print("Digita el valor para z ")
    z = val_num()
    print("Digita el numero de iteraciones deseadas")
    itera_des = val_num()
    print("Digita la tolerancia minima a alcanzar")
    tolerancia = val_num()
    os.system("cls")
    cabMet3()
    cabeceraS4()
    while itera < itera_des:
        jaco = [[(2*x)-4,2*y,0],[(2*x)-1,-12,0],[(6*x)-12,2*y,-(6*z)]]
        fx = [(x*x)-(4*x)+(y*y),(x*x)-(x)-(12*y)+1,(3*x*x)-(12*x)+(y*y)-(3*z*z)+8]
        p1_error = [x,y,z]
        jaco_inv = op_jaco3(jaco)
        if(jaco_inv== 1):
            break
        x = x - ((fx[0]*jaco_inv[0][0]) + (fx[1]*jaco_inv[0][1]) + (fx[2]*jaco_inv[0][2]))
        y = y - ((fx[0]*jaco_inv[1][0]) + (fx[1]*jaco_inv[1][1]) + (fx[2]*jaco_inv[1][2]))
        z = z - ((fx[0]*jaco_inv[2][0]) + (fx[1]*jaco_inv[2][1]) + (fx[2]*jaco_inv[2][2]))
        if(itera == 0):
            error = 0
        elif((x-p1_error[0] > y-p1_error[1]) and (x-p1_error[0] > z-p1_error[2])):
            error = abs(x-p1_error[0])
        elif((y-p1_error[1]>x-p1_error[0])and (y-p1_error[1]> z-p1_error[2])):
            error = abs(y-p1_error[1])
        else:
            error = abs(z-p1_error[2])
        imprimir3(itera,p1_error,fx,jaco,jaco_inv,error)
        if(error < tolerancia and error != 0):
            foter3()
            print(" ")
            print(" La aproximacion es: ")
            print(" x = ",end="") 
            formatNum(p1_error[0])
            sl(1)
            print(" y = ",end="")
            formatNum(p1_error[1])
            sl(1)
            print(" z = ",end="")
            formatNum(p1_error[2])
            sl(1)
            break
        itera += 1
        if(itera == itera_des):
            if(error > 1):
                foter3()
                sl(1)
                print("************aproximacion no encontrada***********")
            else:
                foter3()
                sl(1)
                print(" La aproximacion es: ")
                print(" x = ",end="") 
                formatNum(p1_error[0])
                sl(1)
                print(" y = ",end="")
                formatNum(p1_error[1])
                sl(1)
                print(" z = ",end="")
                formatNum(p1_error[2])
                sl(1)
    time.sleep(5)
    exit()
        
# funcion que genera la matriz inverza de 2 x 2      
def op_jaco2(jaco):
    det = ((jaco[0][0])*(jaco[1][1]))-((jaco[0][1]*jaco[1][0]))
    adj = [[jaco[1][1],-1*jaco[1][0]],[-1*jaco[0][1],jaco[0][0]]]
    try:
        jaco_inv = [[adj[0][0]/det,adj[1][0]/det],[adj[0][1]/det,adj[1][1]/det]]
    except ZeroDivisionError:
        print(" Divicion entre cero")
        jaco_inv = 1
    return (jaco_inv)

# funcion que da la inversa de 3 x 3
def op_jaco3(jaco):
    det = ((jaco[0][0]*jaco[1][1]*jaco[2][2])+(jaco[0][2]*jaco[1][0]*jaco[2][1])+(jaco[0][1]*jaco[1][2]*jaco[2][0])-(jaco[0][2]*jaco[1][1]*jaco[2][0])-(jaco[0][0]*jaco[1][2]*jaco[2][1])-(jaco[0][1]*jaco[1][0]*jaco[2][2]))
    adj = [[(jaco[1][1]*jaco[2][2])-(jaco[1][2]*jaco[2][1]),-(jaco[1][0]*jaco[2][2])+(jaco[1][2]*jaco[2][0]),(jaco[1][0]*jaco[2][1])-(jaco[1][1]*jaco[2][0])],[-(jaco[0][1]*jaco[2][2])+(jaco[0][2]*jaco[2][1]),(jaco[0][0]*jaco[2][2])-(jaco[0][2]*jaco[2][0]),-(jaco[0][0]*jaco[2][1])+(jaco[0][1]*jaco[2][0])],[(jaco[0][1]*jaco[1][2])-(jaco[0][2]*jaco[1][1]),-(jaco[0][0]*jaco[1][2])+(jaco[0][2]*jaco[1][0]),(jaco[0][0]*jaco[1][1])-(jaco[0][1]*jaco[1][0])]]
    try:
        jaco_inv = [[adj[0][0]/det,adj[1][0]/det,adj[2][0]/det],[adj[0][1]/det,adj[1][1]/det,adj[2][1]/det],[adj[0][2]/det,adj[1][2]/det,adj[2][2]/det]]
    except ZeroDivisionError:
        print("divicion entre cero")
        jaco_inv=1
    return jaco_inv

#funcio que  continua el programa o lo saca
def exit():
    print("                ¿Deseas resolver al guna otra ecuacion?")
    print(" Digita '1' para resolver otra ecuacion.     o     Digita '0' para salir.")
    ex= int(val_num())
    if (ex != 1  and ex != 0):
        print("opncion no valida")
        exit()
    def rep():
        menu_newton()
    def exi():
        os.system("cls")
        print("      __^__                                      __^__")
        print("     ( ___ )************************************( ___ )")
        print("      |   |                                      |   |")
        print("      |   |           HASTA LA PROXIMA           |   |")
        print("      |   |                                      |   |")
        print("     ( ___ )************************************( ___ )")
        time.sleep(2)
    dict1 = {
        0 : exi,
        1 : rep
    }
    dict1.get(ex,exit)()

#Funcion que imprime el menu del metodo
def menu():
    os.system("cls")
    barra(100)
    sl(1)
    barra(48)
    print("MENÚ", end="")
    barra(48)
    print()
    barra(100)
    sl(1)
    barra(2)
    espacios(2)
    print("Escoja uno de los cuatro sistemas de ecuaciones integrado en este programa", end="")
    espacios(20)
    barra(2)
    sl(1)
    barra(2)
    espacios(10)
    print("1.-", end="")
    espacios(83)
    barra(2)
    sl(1)
    barra(2)
    espacios(13)
    print("ƒ1(x, y)=x²+xy-10=0", end="")
    espacios(64)
    barra(2)
    sl(1)
    barra(2)
    espacios(13)
    print("ƒ2(x, y)=y+3xy²-50=0", end="")
    espacios(63)
    barra(2)
    sl(1)
    barra(2)
    espacios(10)
    print("2.-", end="")
    espacios(83)
    barra(2)
    sl(1)
    barra(2)
    espacios(13)
    print("ƒ1(x, y)=x²+y²-9=0", end="")
    espacios(65)
    barra(2)
    sl(1)
    barra(2)
    espacios(13)
    print("ƒ2(x, y)=-ex-2y-3=0", end="")
    espacios(64)
    barra(2)
    sl(1)
    barra(2)
    espacios(10)
    print("3.-", end="")
    espacios(83)
    barra(2)
    sl(1)
    barra(2)
    espacios(13)
    print("ƒ1(x, y, z)=2x²-4x+y²+3z²+6z+2=0", end="")
    espacios(51)
    barra(2)
    sl(1)
    barra(2)
    espacios(13)
    print("ƒ2(x, y, z)=x²+y²-2y+2z²-5=0", end="")
    espacios(55)
    barra(2)
    sl(1)
    barra(2)
    espacios(13)
    print("ƒ3(x, y, z)=3x²-10x+y²-3z²+8=0", end="")
    espacios(53)
    barra(2)
    sl(1)
    barra(2)
    espacios(10)
    print("4.-", end="")
    espacios(83)
    barra(2)
    sl(1)
    barra(2)
    espacios(13)
    print("ƒ1(x, y, z)=x²-4x+y²=0", end="")
    espacios(61)
    barra(2)
    sl(1)
    barra(2)
    espacios(13)
    print("ƒ2(x, y, z)=x²-x-12y+1=0", end="")
    espacios(59)
    barra(2)
    sl(1)
    barra(2)
    espacios(13)
    print("ƒ3(x, y, z)=3x²-10x+y²-3z²+8=0", end="");
    espacios(53)
    barra(2)
    sl(1)
    barra(100)
    sl(1)
