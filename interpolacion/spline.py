from numpy import array, linalg

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
    
    matCuad = array(matriz)
    matRes = array(gi)
    matVal = linalg.solve(matCuad,matRes)
    for i in matVal:
        si.append(i)
    si.append(0)
    
    for i in range(0,len(punto)-1):
        ai.append((si[i+1]-si[i])/(6*h[i]))
        bi.append(si[i]/2)
        ci.append(((punto[i+1][1]-punto[i][1])/h[i])-(((si[i+1]+(2*si[i]))/6)*h[i]))

puntos = [[0.95,-1.1],[1.73,0.27],[2.23,-0.29],[2.77,0.56],[2.99,1.0]]
spline_cubico(puntos)