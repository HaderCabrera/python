 # PRACTICANDO WHILE
# EJERCICIO 1
"""
numero = int(input("ingrese numero entero"))
suma = 0
divisor = 1

while suma < numero:
        if numero % divisor == 0:
            suma += divisor
            divisor += 1
        else:
             divisor += 1
            #print(suma)
if suma == numero:
    print(f"El numero {numero} es perfecto")
else:
    print(f"El numero {numero} no es perfecto")

# EJERCICIO 2
importe = int (10000)
bandera = 0
añosTranscurridos = 0
while importe < 20000:
      importe = importe + importe*0.07
      bandera += 1
      #for i in range(bandera):
      añosTranscurridos = int(bandera)
print(f"En {añosTranscurridos} años el valor superara los 20,000")
"""
import random
import math
#EJERCICIO 3
numeroPoints = 0
pointHits = 0
pointNohits = 0

while numeroPoints < 1000000:   
     point = [random.random(), random.random()]
    #print(point)
     area = math.sqrt((point[0])**2 + (point[1])**2)
     numeroPoints += 1
     if area <1:
        pointHits += 1
     else:
        pointNohits += 1
     pi = 4*pointHits*(1/1000000)
print(f"el numero de puntos con probabilidad es {pi:,}")




     