from os import system

def val_num():
    try:
        digit= float(input(">"))
    except(ValueError):
        print("VALOR NO VALIDO")
        digit=val_num()
    return digit

def llenarTabla(h):
    puntos = []
    aux=[]
    print("Ingrese el valor inicial de x")
    valx=val_num()
    aux.append(valx)
    print("Ingrese el valor inicial de f(x)")
    valy=val_num()
    aux.append(valy)
    puntos.append(aux)
    i = 0
    while True:
        system("cls")
        aux=[]
        valx = puntos[i][0] + h
        aux.append(valx)
        print("Ingrese el valor de f(", aux[0],")")
        aux.append(val_num())
        puntos.append(aux)
        i+=1
        print("Si son puntos suficientes ingrese 0")
        opcion=val_num()
        if opcion == 0:
            break
    return puntos

print(llenarTabla(0.5))