#import sys
#sys.path.append("..")
#from Newton_Rapshon.main import val_num
puntos = []
def val_num():
    try:
        digit= float(input(">"))
    except(ValueError):
        print("VALOR NO VALIDO", end="")
        digit=val_num()
    return digit
def menu_interpolacion():
    print("digita 1 para usar interpolacion")
    print("digita 2 para usar ajuste de curvas")
    option = val_num()
    if  option != 1 and option != 2:
        print("opcion no valida")
    def interpolacion():
        punto = ordenamiento(puntos)
        print(punto)
        fun_interpolacion(punto)
    def ajuste_curvas():
        print("opcion fuera de servio")
    dict = {
        1 : interpolacion,
        2 : ajuste_curvas
    }
    dict.get(option,menu_interpolacion)()
    
def fun_tabla():
    while True :
        print("da el valorpara x")
        x = val_num()
        print("da el para y")
        y = val_num()
        cordenadas= [x,y]
        puntos.append(cordenadas)
        print("digita '0' si desea continuar con los puntos ya ingresados si no digite cualquier otro numrto")
        aux = val_num()
        if aux == 0:
            break
    print(puntos)
    print("digita '1'si hay que corregir algun punto, si no, digita cualquier otro numero")
    correcto = val_num()
    if correcto == 1:
        correccion()
    print(len(puntos))
    menu_interpolacion()
    
def correccion():
    print("el numero de columna acorregir")
    col_corregir = int(val_num())
    print(f"da el valor para x en lacolumna ",col_corregir )
    puntos[col_corregir - 1][0] = val_num()
    print(f"de la columna col_corregir para y")
    puntos[col_corregir - 1][1] = val_num()
    print("la nueva lista es ",puntos)
    print("si desea corregir otro dato digite '1', si no, digite culaquier otro numero")
    repetir = val_num()
    if repetir == 1:
        correccion()

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
            print("se requieren "+ grado + "+1 puntos.\n Ingrese otro Grado\>")
        else:
            break
    tabla_dif=[]
    con=1
    for i in range(len(punto),1,-1):
        aux=[]
        for j in range(0,i):
            val=(punto[j+con][1]-punto[j][1])/(punto[j+con][0]-punto[j][0])
            print(val)
            aux.append(val)
        tabla_dif.append(aux)
        aux=[]
        con+=1
    print(tabla_dif)


def agregar_puntos(repeticiones):
    for i in range(1,repeticiones):
        print("da el valor para x")
        x = val_num()
        print("da el valor para y")
        y = val_num()
        puntos.append([x,y])

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
fun_tabla()