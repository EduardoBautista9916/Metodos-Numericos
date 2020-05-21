import os
import time
def barra(c):# * 
    for i in range(c):
        print(chr(42), end="")

def espacios(c):# _ 
    for i in range(c):
        print(chr(32), end="")

def esi(c):# Esquina Superior Izquierda ╔ 
    v=ord("╔")
    for i in range(c):
        print(chr(v), end="")

def bv(c):# Barra Vertical ║
    v=ord("║")
    for i in range(c):
        print(chr(v), end="")

def biiv(c):# Barra Intermedia Izquierda Vertical ╠
    v=ord("╠")
    for i in range(c):
        print(chr(v), end="")

def eii(c):# Esquina Inferior Izquierda ╚
    v=ord("╚")
    for i in range(c):
        print(chr(v), end="")

def bh(c):# Barra Horizontal ═
    v=ord("═")
    for i in range(c):
        print(chr(v), end="")

def bsih(c):# Barra Superior Intermedia Horizontal ╦
    v=ord("╦")
    for i in range(c):
        print(chr(v), end="")

def bii(c):# Barra Intermedia Intermedia ╬
    v=ord("╬")
    for i in range(c):
        print(chr(v), end="")

def biih(c):# Barra Inferior Intermedia Horizontal ╩ 
    v=ord("╩")
    for i in range(c):
        print(chr(v), end="")

def esd(c):# Esquina Superior Derecha ╗ 
    v=ord("╗")
    for i in range(c):
        print(chr(v), end="")

def bidv(c):# Barra Intermedia Derecha Vertical ╣
    v=ord("╣")
    for i in range(c):
        print(chr(v), end="")

def eid(c):# Esquina Inferior Derecha ╝
    v=ord("╝")
    for i in range(c):
        print(chr(v), end="")

def desborde(c):
    for i in range(c):
        print("#", end="")

def sl(c):
    for i in range(c):
        print()

def bcsup(c): #Barra de Carga Superior ▄
    for i in range(c):
        print("▄", end="")

def bcint(c):#Barra de Carga Itermedia █
    for i in range(c):
        print("█", end="")

def bcinf(c):#Barra de Carga Inferior ▀
    for i in range(c):
        print("▀", end="")

def proceso(t):
    for i in range(99):
        c = 98 - i
        barra(100)
        sl(1)
        barra(2)
        espacios(2)
        print("Espere un Momento, el Programa está cargando los Atributos y Herramientas necesarios para", end="")
        espacios(5)
        barra(2)
        sl(1)
        barra(2)
        espacios(2)
        print("el Proceso", end="")
        espacios(84)
        barra(2)
        sl(1)
        barra(100)
        sl(2)
        espacios(45)
        print("CARGANDO...", end="")
        espacios(44)
        print()
        esi(1)
        bcsup(i)
        bh(c)
        esd(1)
        sl(1)
        bv(1)
        bcint(i)
        espacios(c)
        bv(1)
        sl(1)
        eii(1)
        bcinf(i)
        bh(c)
        eid(1)
        sl(1)
        time.sleep(t)
        os.system("cls")