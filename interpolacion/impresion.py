from interpolacion.barras import *
parar = False

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

def formatN(val):
    if(val>0):
        if(val<10):
            espacios(2)
            print("ƒ[",val,"]",end="")
            espacios(2)
        elif(val<100):
            espacios(1)
            print("ƒ[", val, "]",end="")
            espacios(2)
        elif(val<1000):
            espacios(1)
            print("ƒ[", val, "]",end="")
            espacios(1)
        elif(val<10000):
            espacios(1)
            print("ƒ[", val, "]",end="")
            espacios(0)
        elif(val<100000):
            espacios(0)
            print("ƒ[", val, "]",end="")
            espacios(0)
        else:
            espacios(2)
            print("ƒ[###]",end="")
            espacios(2)
            parar = True

def formatIter(val):
    if(val<10):
        espacios(1)
        print(val,end="")
        espacios(1)
    elif(val<100):
        espacios(1)
        print(val,end="")
    elif(val<1000):
        print(val)
    else:
        print("###",end="")

def imprimirTabla2(punto, hi, fi):
    esi(1)
    bh(3)
    for i in range(0,4):
        bsih(1)
        bh(10)
    esd(1)
    sl(1)
    bv(1)
    print(" i ",end="")
    bv(1)
    print("    xi    ",end="")
    bv(1)
    print("  f(xi)   ",end="")
    bv(1)
    print("    hi    ",end="")
    bv(1)
    print("    fi    ",end="")
    bv(1)
    sl(1)
    biiv(1)
    bh(3)
    for i in range(0,4):
        bii(1)
        bh(10)
    bidv(1)
    sl(1)
    for i in range(0,len(punto)):
        bv(1)
        formatIter(i)
        bv(1)
        formatNum(punto[i][0])
        bv(1)
        formatNum(punto[i][1])
        bv(1)
        if (i<len(hi)):
            formatNum(hi[i])
            bv(1)
            formatNum(fi[i])
        else:
            espacios(10)
            bv(1)
            espacios(10)
        bv(1)
        sl(1)
        biiv(1)
        bh(3)
        for j in range(0,4):
            bii(1)
            bh(10)
        bidv(1)
        sl(1)
    
    eii(1)
    bh(3)
    for i in range(0,4):
        biih(1)
        bh(10)
    eid(1)
    sl(1)

def imprimirTabla3(punto, hi, fi, si):
    esi(1)
    bh(3)
    for i in range(0,5):
        bsih(1)
        bh(10)
    esd(1)
    sl(1)
    bv(1)
    print(" i ",end="")
    bv(1)
    print("    xi    ",end="")
    bv(1)
    print("  f(xi)   ",end="")
    bv(1)
    print("    hi    ",end="")
    bv(1)
    print("    fi    ",end="")
    bv(1)
    print("    Si    ",end="")
    bv(1)
    sl(1)
    biiv(1)
    bh(3)
    for i in range(0,5):
        bii(1)
        bh(10)
    bidv(1)
    sl(1)
    for i in range(0,len(punto)):
        bv(1)
        formatIter(i)
        bv(1)
        formatNum(punto[i][0])
        bv(1)
        formatNum(punto[i][1])
        bv(1)
        if (i<len(hi)):
            formatNum(hi[i])
            bv(1)
            formatNum(fi[i])
        else:
            espacios(10)
            bv(1)
            espacios(10)
        bv(1)
        formatNum(si[i])
        bv(1)
        sl(1)
        biiv(1)
        bh(3)
        for j in range(0,5):
            bii(1)
            bh(10)
        bidv(1)
        sl(1)
    
    eii(1)
    bh(3)
    for i in range(0,5):
        biih(1)
        bh(10)
    eid(1)
    sl(1)

def imprimirTabla4(punto, si, ai, bi, ci):
    esi(1)
    bh(3)
    for i in range(0,7):
        bsih(1)
        bh(10)
    esd(1)
    sl(1)
    bv(1)
    print(" i ",end="")
    bv(1)
    print("    xi    ",end="")
    bv(1)
    print("  f(xi)   ",end="")
    bv(1)
    print("    Si    ",end="")
    bv(1)
    print("    ai    ",end="")
    bv(1)
    print("    bi    ",end="")
    bv(1)
    print("    ci    ",end="")
    bv(1)
    print("    di    ",end="")
    bv(1)
    sl(1)
    biiv(1)
    bh(3)
    for i in range(0,7):
        bii(1)
        bh(10)
    bidv(1)
    sl(1)
    for i in range(0,len(punto)):
        bv(1)
        formatIter(i)
        bv(1)
        formatNum(punto[i][0])
        bv(1)
        formatNum(punto[i][1])
        bv(1)
        formatNum(si[i])
        bv(1)
        if (i<len(ai)):
            formatNum(ai[i])
            bv(1)
            formatNum(bi[i])
            bv(1)
            formatNum(ci[i])
            bv(1)
            formatNum(punto[i][1])
        else:
            espacios(10)
            bv(1)
            espacios(10)
            bv(1)
            espacios(10)
            bv(1)
            espacios(10)
        bv(1)
        sl(1)
        biiv(1)
        bh(3)
        for j in range(0,7):
            bii(1)
            bh(10)
        bidv(1)
        sl(1)
    
    eii(1)
    bh(3)
    for i in range(0,7):
        biih(1)
        bh(10)
    eid(1)
    sl(1)