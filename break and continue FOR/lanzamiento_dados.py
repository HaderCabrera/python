#lanzar un dado 100 veces, imṕrimir cuantas veces cae el numero 5
import random

contador = 0
for i in range(101):
    dado = random.randrange(7)
    #print(dado)
    if dado == 5:
        contador += 1
print(f"El numero 5 cayó {contador} veces")
