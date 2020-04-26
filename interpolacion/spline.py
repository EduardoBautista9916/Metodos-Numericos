import os
from numpy import array, linalg
from impresion import imprimirTabla2,imprimirTabla3,imprimirTabla4

def spline_cubico(punto):
    h =[]
    fi = []
    si = [0]
    gi = []
    g = []
    ai=[]
    bi=[]
    ci=[]
    matriz= []
    for i in range(0,len(punto)-1):
        h.append(punto[i+1][0]-punto[i][0])
        fi.append((punto[i+1][1]-punto[i][1])/h[i])
        if i >0:
            gi.append((fi[i]-fi[i-1])*6)
    os.system("cls")
    print("La Tabla de Diferencias de Puntos x y las Derivadas de f(x)")
    imprimirTabla2(punto,h,fi)
    os.system("pause")
    centinela = 1
    aux = centinela
    for i in range(0,len(punto)-2):
        arrayAux=[]
        for j in range(0,len(punto)-2):
            if (centinela==0):
                arrayAux.append(h[i])
            elif(centinela==1):
                arrayAux.append(2*(h[i]+h[i+1]))
            elif(centinela==2):
                arrayAux.append(h[i+1])
            else:
                arrayAux.append(0)
            centinela += 1
        matriz.append(arrayAux)
        aux-=1
        centinela=aux
    os.system("cls")
    matCuad = array(matriz)
    matRes = array(gi)
    matVal = linalg.solve(matCuad,matRes)
    for i in matVal:
        si.append(i)
    si.append(0)
    
    print("La Tabla de Valores con los valores de S")
    imprimirTabla3(punto,h,fi,si)
    os.system("pause")

    for i in range(0,len(punto)-1):
        ai.append((si[i+1]-si[i])/(6*h[i]))
        bi.append(si[i]/2)
        ci.append(((punto[i+1][1]-punto[i][1])/h[i])-(((si[i+1]+(2*si[i]))/6)*h[i]))
    
    os.system("cls")
    print("La Tabla de Valores con los coeficientes a, b, c, y d")
    imprimirTabla4(punto,si,ai,bi,ci)
    os.system("pause")