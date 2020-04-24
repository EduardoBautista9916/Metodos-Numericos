def spline_cubico(punto):
    h =[]
    fi = []
    si = [0]
    gi = []
    matriz= []
    for i in range(0,len(punto)-1):
        h.append(punto[i+1][0]-punto[i][0])
        fi.append((punto[i+1][1]-punto[i][1])/h[i])
        if i >0:
            gi.append((fi[i]-fi[i-1])*6)
            
    print (h, fi , gi)