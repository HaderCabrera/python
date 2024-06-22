#CALCULAR FACTORIAL DE UN NUMERO

num = int(input("Ingrese el numero: "))
fact = 1
for i in range(1,num+1):
    fact *= i
print(f"El factorial de {num} ingresado es : {fact}")

# HACER UN PROGRAMA EN PYTHON QUE GENERE EL SIGUIENTE NUMERO DE 
# LA SECUENCIA: 1,1,2,-1,1,-2,?
n1 = 1
n2 = 1
sig = -1
print(n1,n2,end=",")
for i in range(5):
    numSiguiente = n1 + (sig**i)*n2
    n1 = n2
    n2 = numSiguiente
    print(numSiguiente, end=",")
     


