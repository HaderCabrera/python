# TALLER 3
"""
    #EJERCICIO 1
PRECIO = 0.65
diasEstancia = int(input("¿Cuantos dias planea hospedarse? "))
distanciaRecorrida = float(input("Distancia recorrida [Km] = "))

if diasEstancia > 7 and distanciaRecorrida > 800:
    valorBillete = PRECIO * distanciaRecorrida * (1-0.3)
    print(f"el valor del billete es: ${valorBillete:0.2f} USD")
else:
    valorBillete = PRECIO * distanciaRecorrida
    print(f"el valor del billete es: ${valorBillete:0.2f} USD")

    # EJERCICIO 2
añoIngresado = int(input("Ingrese un año [AAAA] : "))
conditionOne = añoIngresado % 4
conditionTwo = añoIngresado % 100
conditionThree = añoIngresado % 400


if conditionOne == 0 :
    print("el año es bisiesto")
    if conditionTwo == 0 and conditionThree != 0 :
        print("EL año es bisiesto")
else:
    print("el año no es bisiesto")

 # EJERCICIO 3

weight = float(input("Enter your weight [Pounds]: "))
height = float(input("Enter your height [Inch]: "))

weightKilograms = weight * 0.45359237
heightMeters = height * 0.0254

bmi = weightKilograms / (heightMeters**2)
print(f"BMI is {bmi:.2f}")

if bmi < 18.5:
    interpretation = "Underweight"
    print(interpretation)
if bmi >18.5 and bmi < 24.9:
    interpretation = "Normal"
    print(interpretation)
if bmi >25.0 and bmi < 29.9:
    interpretation = "Overweight"
    print(interpretation)
if bmi >30:
    interpretation = "Obese"
    print(interpretation)
"""
#EJERCICIO 4

diaActual = int(input("Ingrese el dia actual [1(Lunes) - 7(Domingo)] : "))
cantidadDias = int(input("Ingrese la cantidad de dias transcurridos: "))
variable1 = cantidadDias%7
diaFuturo = diaActual + variable1
print(diaFuturo)
if diaFuturo > 7:
    variables2 = diaFuturo - 7
    if variables2 == 1:
        print("el dia futuro es Lunes")
    if variables2 == 2:
        print("el dia futuro es Martes")
    if variables2 == 3:
        print("el dia futuro es Miercoles")
    if variables2 == 4:
        print("el dia futuro es Jueves")
    if variables2 == 5:
        print("El dia futuro es Viernes")
    if variables2 == 6:
        print("el dia futuro es Sabado")
    if variables2 == 7:
        print("El dia futuro es Domingo")

if diaFuturo == 1:
    diaFuturo = "Lunes"
    print(f"EL dia actual es Lunes y el dia futuro es {diaFuturo}")
if diaFuturo == 2:
    diaFuturo = "Martes"
    print(f"EL dia actual es Martes y el dia futuro es {diaFuturo}")
    
if diaFuturo == 3:
    diaFuturo = "Miercoles"
    print(f"EL dia actual es MIercoles y el dia futuro es {diaFuturo}")
    
if diaFuturo == 4:
    diaFuturo = "Jueves"
    print(f"EL dia actual es JUeves y el dia futuro es {diaFuturo}")
    
if diaFuturo == 5:
    diaFuturo = "Viernes"
    print(f"EL dia actual es Viernes y el dia futuro es {diaFuturo}")
    
if diaFuturo == 6:
    diaFuturo = "Sabado"
    print(f"EL dia actual es Sabado y el dia futuro es {diaFuturo}")
    
if diaFuturo == 7:
    diaFuturo = "Domingo"
    print(f"EL dia actual es Domingo y el dia futuro es {diaFuturo}")


"""
#EJERCICO 5


numero = int(input("Ingrese un numero entero: "))
if numero >=1 and numero <= 9:
    print("1")
if numero >=10 and numero <= 99:
    print("2")
if numero >= 100 and numero <=999:
    print("3")
if numero >= 1000 and numero <=9999:
    print("4")
if numero >= 10000 and numero <=99999:
    print("5")
if numero >= 100000 and numero <=999999:
    print("6")
"""