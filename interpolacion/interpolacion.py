import time
import os
from interpolacion.impresion import imprimirDatos, imprimirTabla, formatNum
from interpolacion.barras import *
from interpolacion.spline import *

puntos = []

def menu_interpolacion(punto):
    puntos = punto
    os.system("cls")
    while True:
        menu()
        option = val_num()
        if  option != 1 and option != 2:
            print("opcion no valida")
        def capturar():
            fun_tabla()
        def interpolacion():
            os.system("cls")
            punto = ordenamiento(puntos)
            imprimirDatos(punto)
            fun_interpolacion(punto)
            os.system("cls")
        def ajuste_curvas():
            if len(puntos) < 3:
                print("puntos insuficientes")
            else:
                punto = ordenamiento(puntos)
                spline_cubico(punto)
        dict = {
            1 : capturar,
            2 : interpolacion,
            3 : ajuste_curvas
        }
        dict.get(option,menu_interpolacion)()
        os.system("cls")
        print("¿Desea Realizar Algo más?(Si es así escriba yes)")
        op= input(">")
        if(op.lower()!='yes'):
            os.system("cls")
            print("*"*100)
            print("*"*42 + "HASTA LA PROXIMA"+ "*"*42)
            print("*"*47 + "GRACIAS"+ "*"*46)
            print("*"*100)
            break
        else:
            while True:
                menu_rep()
                rep_tabla = int(val_num())
                if rep_tabla != 1 and rep_tabla != 2:
                    os.system("cls")
                    print("opcion no valida")
                else:
                    break
            if(rep_tabla == 2):
                puntos.clear()
                os.system("cls")
                fun_tabla()
                break
    return punto

# funcion que valida que sea un numero la entrada
def val_num():
    try:
        digit= float(input(">"))
    except(ValueError):
        print("VALOR NO VALIDO")
        digit=val_num()
    return digit

# funcion que obtiene los datos de la tabla  
def fun_tabla():
    barra(100)
    sl(1)
    barra(2)
    espacios(2)
    print("Para comenzar debes de ingresar los valores de la Tabla. Recuerda que los valores para x no ", end="")
    espacios(2)
    barra(2)
    sl(1)
    barra(2)
    espacios(2)
    print("se deben de repetir.",end="")
    espacios(74)
    barra(2)
    sl(1)
    barra(100)
    sl(1)
    os.system("pause")
    i=1
    while True :
        os.system("cls")
        x=0
        rep=True
        while rep:
            print("Da el valor para x", i)
            x = val_num()
            rep=False
            for j in range(0,len(puntos)):
                if x == puntos[j][0]:
                    os.system("cls")
                    print("Recurerda que no puede haber dos x iguales, debes de ingresar otro valor")
                    rep = True
                    break
                else:
                    rep = False
        print("Da el valor para y", i)
        y = val_num()
        cordenadas= [x,y]
        puntos.append(cordenadas)
        i+=1
        print("Digita '0' si desea continuar con los puntos ya ingresados si no digite cualquier otro numero ")
        aux = val_num()
        if aux == 0:
            break
    os.system("cls")
    imprimirDatos(puntos)
    print("digita '1'si hay que corregir algún punto, si no, digita cualquier otro numero")
    correcto = val_num()
    if correcto == 1:
        correccion()

# corrige algun punto mal capturado    
def correccion():
    os.system("cls")
    while True:
        imprimirDatos(puntos)
        print("El número de columna a corregir")
        col_corregir = int(val_num())
        if col_corregir <= len(puntos):
            break
        else:
            os.system("cls")
            print("La Tabla solo Tiene", len(puntos), "columnas.")

    x=0
    rep=True
    while rep:
        print(f"Da el valor para x en la columna ",col_corregir )
        x = val_num()
        rep=False
        for j in range(0,len(puntos)):
            if x == puntos[j][0]:
                os.system("cls")
                print("Recurerda que no puede haber dos x iguales, este valor ya está en la tabla, debes de ingresar otro valor")
                rep = True
                break
            else:
                rep = False
    puntos[col_corregir - 1][0] = x
    print(f"Da el valor para y en la columna ", col_corregir)
    puntos[col_corregir - 1][1] = val_num()
    os.system("cls")
    print("La nueva tabla de puntos es: ")
    imprimirDatos(puntos)
    print("si desea corregir otro dato digite '1', si no, digite culaquier otro número")
    repetir = val_num()
    if repetir == 1:
        correccion()

# comienza el metodo de interpolacion por diferencias divididas 
def fun_interpolacion(punto):
    while True:
        print("digita el numero a interpolar")
        num_inter = val_num()
        if num_inter < punto[0][0] or num_inter > punto[len(puntos)-1][0]:
            print("valor a interpolar fuera de rrango")
        else:
            break
    print("digita el grado de el polinomio que se requiere")
    while True:
        grado = val_num()
        if len(puntos) -1 < grado :
            print("se requieren ",grado+1 , " puntos.\n Ingrese otro Grado")
            print("NOTA: grado maximo posibles es:" , len(puntos)-1 )
        else:
            break
    os.system("cls")
    tabla=diferencias(punto)
    imprimirTabla(punto,tabla)
    resultado = punto [0][1]
    
    for i in range(0,int(grado)):
        aux = tabla[i][0]
        for j in range(0,i+1):
            aux *= (num_inter - punto[j][0])
        resultado += aux
    print("P",end="")
    print(int(grado),end="")
    print("(",end="")
    print(num_inter,end="")
    print(")=",end="")
    formatNum(resultado)
    sl(1)
    os.system("pause")

#Genera la tabla de diferencias divididas
def diferencias(punto):
    con=1
    tabla=[]
    auxiliar=[]
    for i in range(0,len(punto)-1):
        try:
            val=(punto[i+1][1]-punto[i][1])/(punto[i+1][0]-punto[i][0])
        except(ZeroDivisionError):
            print("error divicion entre cero")
            time.sleep(2)
            val = 0 
        auxiliar.append(val)
    tabla.append(auxiliar)
    auxiliar=[]
    con+=1
    for i in range(len(punto)-1,1,-1):
        for j in range(0,(i-1)):
            try:
                val=(tabla[con-2][j+1]-tabla[con-2][j])/(punto[j+con][0]-punto[j][0])
            except:
                print("error divicion entre cero")
                time.sleep(2)
            auxiliar.append(val)
        tabla.append(auxiliar)
        auxiliar=[]
        con+=1
    return tabla

#Agrega los puntos necesarios
def agregar_puntos(repeticiones):
    for i in range(1,repeticiones):
        print("da el valor para x")
        x = val_num()
        print("da el valor para y")
        y = val_num()
        puntos.append([x,y])

#Ordena la tabla ingresada
def ordenamiento(punto):
    izquierda =[]
    derecha = []
    centro = []
    if len(punto) > 1:
        pivote = punto[0][0]
        for i in punto:
            if i[0] < pivote:
                izquierda.append(i)
            elif i[0] == pivote:
                centro.append(i)
            elif i[0] > pivote:
                derecha.append(i)
        return ordenamiento(izquierda) + centro + ordenamiento(derecha)
    else:
        return punto

def menu():
    os.system("cls")
    barra(100)
    sl(1)
    barra(48)
    print("MENÚ", end="")
    barra(48)
    sl(1)
    barra(2)
    espacios(2)
    print("1.- Capturar Tabla", end="")
    espacios(77)
    barra(2)
    sl(1)
    barra(2)
    espacios(2)
    print("2.- Interpolacion", end="")
    espacios(77)
    barra(2)
    sl(1)
    barra(2)
    espacios(2)
    print("3.- Ajuste de Curvas", end="")
    espacios(74)
    barra(2)
    sl(1)
    barra(100)
    sl(1)
    barra(100)
    sl(1)
    print("Elige una de las tres opciones")

def menu_rep():
    barra(100)
    sl(1)
    barra(2)
    espacios(2)
    print("Digita 1.- Para continuar con la misma tabla",end="")
    espacios(50)
    barra(2)
    sl(1)
    barra(2)
    espacios(2)
    print("Digita 2.- Para cambiar la tabla",end="")
    espacios(65)
    barra(2)
    sl(1)
    barra(100)
    sl(1)