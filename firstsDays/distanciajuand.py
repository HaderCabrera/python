import math
def distancia (xt,yt,xs,ys):
    d = math.sqrt((xt-xs)**2 + (yt-ys)**2)
    return d
x1 = 1
x2=3
y1=2
y2=4

#EJERCICIO 2
import math
def distancia (xt,yt,xs,ys):
    d = math.sqrt((xt-xs)**2 + (yt-ys)**2)
    return d
    

def perimetroTriangulo(xp,yp,xq,yq,xr,yr):
    perimetro = distancia(xp,yp, xr, yr) + distancia(xr,yr,xq,yq) + distancia(xq,yq,xp,yp)
    return perimetro
    

x1=1 
y1=4
x2=3
y2=0
x3=5
y3=3
print(f"El perimetro del triangulo es: {perimetroTriangulo(x1,y1,x2,y2,x3,y3):.3f}")

#EJERCICIO 3
def descuento(valor):

    if valor >150000:
        d=valor*0.05
    else:
        d= 0
    return d
valor=int(input("Ingrese el valor del articulo"))
d= descuento(valor)
print(f"El descuento es de {d:,}")

#EJERCICIO 4
def resultEstudiante(n1,n2,n3,n4,n5):
    promedio =(n1+n2+n3+n4+n5)/5

    if promedio >3.5:
        return True
        
    else:
        return False
        

nota1 = float(input("Ingrese la nota 1: "))
nota2 = float(input("Ingrese la nota 2: "))
nota3 = float(input("Ingrese la nota 3: "))
nota4 = float(input("Ingrese la nota 4: "))
nota5 = float(input("Ingrese la nota 5: "))

if resultEstudiante(nota1,nota2,nota3,nota4,nota5):
    print("GANO EL AÑO")
else:
    print("PERDIO EL AÑO")