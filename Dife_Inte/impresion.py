import sys
from barras import *

def imprimirDatos(punto):
    esi(1)
    bh(3)
    for i in range(0,len(punto)):
        bsih(1)
        bh(10)
    esd(1)
    sl(1)
    bv(1)
    espacios(1)
    print("x", end="")
    espacios(1)
    bv(1)
    for i in range(0,len(punto)):
        formatNum(punto[i][0])
        bv(1)
    sl(1)
    biiv(1)
    bh(3)
    for i in range(0,len(punto)):
        bii(1)
        bh(10)
    bidv(1)
    sl(1)
    bv(1)
    espacios(1)
    print("y", end="")
    espacios(1)
    bv(1)
    for i in range(0,len(punto)):
        formatNum(punto[i][1])
        bv(1)
    sl(1)
    eii(1)
    bh(3)
    for i in range(0,len(punto)):
        biih(1)
        bh(10)
    eid(1)
    sl(1)

def formatNum(val):
    if(val>0):
        if(val<10):
            print("{0:.8f}".format(val), end="")
        elif(val<100):
            print("{0:.7f}".format(val), end="")
        elif(val<1000):
            print("{0:.6f}".format(val), end="")
        elif(val<10000):
            print("{0:.5f}".format(val), end="")
        elif(val<100000):
            print("{0:.4f}".format(val), end="")
        elif(val<1000000):
            print("{0:.3f}".format(val), end="")
        elif(val<10000000):
            print("{0:.2f}".format(val), end="")
        elif(val<100000000):
            print("{0:.1f}".format(val), end="")
        else:
            desborde(10)
            parar = True
    elif(val<0):
        if(val>-10):
            print("{0:.7f}".format(val), end="")
        elif(val>-100):
            print("{0:.6f}".format(val), end="")
        elif(val>-1000):
            print("{0:.5f}".format(val), end="")
        elif(val>-10000):
            print("{0:.4f}".format(val), end="")
        elif(val>-100000):
            print("{0:.3f}".format(val), end="")
        elif(val>-1000000):
            print("{0:.2f}".format(val), end="")
        elif(val>-10000000):
            print("{0:.1f}".format(val), end="")
        else:
            desborde(10)
            parar = True
    else:
        cadena = str("{0:.8f}".format(val))
        cont = 0
        for i in cadena:
            print(i, end="")
            cont+=1
            if(cont==10):
                break

def imprimirDer(punto, tabla, intervalo, h):
    inicio = int(((intervalo[0])/h)-2)
    fin = int(((intervalo[1])/h)+1)

    esi(1)
    bh(43)
    esd(1)
    sl(1)
    bv(1)
    espacios(12)
    print("TABLA DE DERIVADAS", end="")
    espacios(13)
    bv(1)
    sl(1)
    biiv(1)
    bh(10)
    for i in range(0,3):
        bsih(1)
        bh(10)
    bidv(1)
    sl(1)
    bv(1)
    espacios(5)
    print("x", end="")
    espacios(4)
    bv(1)
    espacios(3)
    print("f(x)", end="")
    espacios(3)
    bv(1)
    espacios(2)
    print("f'(x)", end="")
    espacios(3)
    bv(1)
    espacios(2)
    print("f''(x)", end="")
    espacios(2)
    bv(1)
    sl(1)
    biiv(1)
    bh(10)
    for i in range(0,3):
        bii(1)
        bh(10)
    bidv(1)
    sl(1)
    j=0
    k=0
    for i in range(inicio,fin):
        bv(1)
        formatNum(punto[i][0])
        bv(1)
        formatNum(punto[i][1])
        bv(1)
        if(i>inicio and i<fin-1):
            formatNum(tabla[0][j])
            j+=1
        else:
            espacios(10)
        bv(1)
        if(i>inicio+1 and i<fin-2):
            formatNum(tabla[1][k])
            k+=1
        else:
            espacios(10)
        bv(1)
        sl(1)
        biiv(1)
        bh(10)
        for i in range(0,3):
            bii(1)
            bh(10)
        bidv(1)
        sl(1)
    eii(1)
    bh(10)
    for i in range(0,3):
        biih(1)
        bh(10)
    eid(1)
    sl(1)