from recursos.barras import *
import os

def diferenciacion(punto, h, intervalo):
    tabla = []
    aux=[]
    inicio = int(((intervalo[0]-punto[0][0])/h)-1)
    inter = int(((intervalo[1]-intervalo[0])/h)+1)
    for i in range(inicio,inter):
        aux.append((1/2*h)*(punto[i+2][1]-punto[i][1]))
        print(aux)
    tabla.append(aux)
    print(tabla)
    aux=[]
    print()
    for i in range(0,len(tabla[0])-2):
        print(i)
        aux.append((1/2*h)*(tabla[0][i+2]-tabla[0][i]))
        print(aux)
    tabla.append(aux)
    return tabla

def integracion(punto, h):
    integral = 0
    integral2 = 0
    if((len(punto) % 2)==0):
        integral=punto[0][1]+punto[len(punto)-1][1]
        for i in range(1, len(punto)-2, 2):
            integral += (2*punto[i][1]) + (4*punto[i+1][1])
        integral = (integral*h)/3
        print(integral)
    else:
        integral=punto[0][1]+punto[len(punto)-4][1]
        for i in range(1, len(punto)-5, 2):
            integral += (2*punto[i][1]) + (4*punto[i+1][1])
        integral = (integral*h)/3
        integral2=punto[len(punto)-4][1]+punto[len(punto)-1][1]
        for i in range(len(punto)-3, len(punto)-1):
            integral2 += (3*punto[i][1])
        integral2 = (3*h*integral2)/8

        print(integral)
        print(integral2)
        integral+=integral2
        print(integral)
    return integral

def diferencias(punto):
    con=1
    val = 0
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