from os import system

def val_num():
    try:
        digit= float(input(">"))
    except(ValueError):
        print("VALOR NO VALIDO")
        digit=val_num()
    return digit

def llenarTabla(h, cant):
    puntos = []
    aux=[]
    print("Ingrese el valor inicial de x")
    valx=val_num()
    aux.append(valx)
    print("Ingrese el valor inicial de f(x)")
    valy=val_num()
    aux.append(valy)
    puntos.append(aux)
    for i in range(0,cant-1):
        system("cls")
        aux=[]
        valx = puntos[i][0] + h
        aux.append(valx)
        print("Ingrese el valor de f(", aux[0],")")
        aux.append(val_num())
        puntos.append(aux)
    return puntos

def val_inter(intervalo, punto):
    if (intervalo[0]>intervalo[1]):
        print("El intervalo no es valido, El primer valor no puede ser mas grande que el segundo")
        return False
    elif(intervalo[0]==punto[0][0] or intervalo[1] == punto[len(punto)-1][0]):
        print("Intervalo invalido, El intervalo no puede tomar valores de los extremos")
        return False
    elif(intervalo[0]<punto[1][0] or intervalo[1] > punto[len(punto)-2][0]):
        print("Intervalo Invalido, El intervalo no puede estar fuera de la tabla")
        return False
    else:
        centinela1 = False
        centinela2= False
        for i in range(0, len(punto)-1):
            if(intervalo[0]==punto[i][0]):
                centinela1 = True
            if(intervalo[1]==punto[i][0]):
                centinela2=True
        if(not(centinela1 and centinela2)):
            print("Intervalo Invalido, algun valor del intervalo no pertence a la tabla")
        return (centinela1 and centinela2)