import sys
sys.path.append("..")
from recursos.barras import *

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

def imprimirTabla(punto, tabla):
    esi(1)
    bh(10)
    for i in range(0,len(punto)):
        bsih(1)
        bh(10)
    esd(1)
    sl(1)
    bv(1)
    espacios(4)
    print("xi", end="")
    espacios(4)
    bv(1)
    espacios(4)
    print("ƒi", end="")
    espacios(4)
    for i in range(0,len(punto)-1):
        bv(1)
        formatN(i+1)
    bv(1)
    sl(1)
    biiv(1)
    bh(10)
    for i in range(0,len(punto)):
        bii(1)
        bh(10)
    bidv(1)
    sl(1)
    con=0
    for i in range(len(punto),0,-1):
        bv(1)
        formatNum(punto[con][0])
        bv(1)
        formatNum(punto[con][1])
        for j in range(0,i-1):
            bv(1)
            formatNum(tabla[j][con])
        for i in range(0,con):
            bv(1)
            espacios(10)
        bv(1)
        sl(1)
        biiv(1)
        bh(10)
        for i in range(0,len(punto)):
            bii(1)
            bh(10)
        bidv(1)
        sl(1)
        con+=1
    eii(1)
    bh(10)
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
