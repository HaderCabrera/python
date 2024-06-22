""" # CALCULAR SI UN NUMERO ES PRIMO, DIVISIBLE POR SI MISMO Y POR 1

num = int(input("ingrese un numero?"))

if num < 2:
    print("no es primo")
elif num == 2:
    print("es primo")
else:
    esprimo = True
    for i in range(2,num):
        if num % i == 0:
            esprimo = False
            break

if esprimo == True:
    print("es primo")
else:
    print("no es primo, lo divide",i)

#salta un iteracion de un ciclo
#IMPRIMA LOS NUMEROS 1 AL 100 EXCEPTO LOS MULTIPLOS DE 7
 """
for i in range(1,101):
    if i % 7 == 0:
        continue
    print(i, end =",")