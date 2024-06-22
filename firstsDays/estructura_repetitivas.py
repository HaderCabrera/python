#FUNCION RANGE([ini], fin, [inc]), ME GENERA UN LISTADO DE NUMEROS
print(list(range(5)))

print(list(range(2,10)))
print(list(range(2,10,3)))
print(list(range(15,-3,-1)))

#CICLO FOR
for i in range(10):
    print(i, end =",")
print("")
for i in range(6):
    print("*",end="")

print("")
for i in range(3):
    print("*    *")

for i in range(6):
    print("*",end="")


cantLineas = int(input("Ingrese el numero de filas: "))

for i in range(cantLineas):
    print("*"*(i+1))
    

