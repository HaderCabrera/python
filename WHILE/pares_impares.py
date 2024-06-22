# determinar el numero de pares e impar
num = input(input("INtgrese un número"))
contPares = 0
contImpares = 0
while num != -1:
    if num % 2 == 0:
        print("el numero es par")
        contPares += 1
    else:
        print("el numero es impar")
        contImpares += 1

    num = int(input("Ingrese un número: "))

print("\n","="*30)
print(f"Cantidad de numeros pares es: {contPares}")
print(f"Cantidad de numeros impares es: {contImpares}")
