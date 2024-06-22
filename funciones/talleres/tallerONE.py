def calcFactorial(num):
    factorial = 1
    for i in range(1,num+1):
        multiplo = i
        factorial = factorial* multiplo
    return factorial

def readNum(smjNum):
    while True:
        try:
            numero = int(input(smjNum))
            return numero
        except ValueError:
            print("Error. Digite un numero")
    
######################################################################
def calcSalario(horasTrabajadas,valorHora):
    if horasTrabajadas > 40:
        salario = (40 * valorHora) + ((horasTrabajadas - 40) * valorHora)
        return salario
    elif horasTrabajadas <= 40:
        salario = horasTrabajadas * valorHora
        return salario
    
def cantHoras(msjHoras):
    while True:
        try:
            horas = int(input(msjHoras))
            return horas
        except ValueError:
            print("Numero invalido. D")

def valHora(smjValor):
    while True:
        try:
            valHora = float(input(smjValor))
            return valHora
        except ValueError:
            print("Error.Formato incorrecto. (use el simbolo .)")
######################################################################

def contPalabras(smjText):
            
            parrafo = input(smjText)
            parrafo = parrafo.strip()
            parrafo = parrafo.split(" ")
            cantidadPalabras = len(parrafo)
            return(cantidadPalabras)
    
######################################################################

#DEFINIR MENÚ
def menu():
    while True:
        try:
            print("\n")
            print("****** MENÚ ******")
            print("1. Factorial de un número")
            print("2. Calcular salario de un empleado")
            print("3. Calcular palabras de un párrafo")
            print("4. Salir")
            op = int(input(">>> Opción (1-5)? "))
            if op < 1 or op > 4:
                print("Rango incorrecto. DIgite un numero entre el 1 y el 4")
                input("Presiones cualquier tecla para intentar de nuevo...")
                continue
            return op
        except ValueError:
            print("Opcion no valida. Digite del 1 al 4")
            input("Presiones cualquier tecla para intentar de nuevo...")


while True:
    op = menu()
    if op == 2:
        print("\n2. Calcular salario de un empleo")
        horas = cantHoras("Ingrese la cantidad de horas laboradas: ")
        valor = valHora("Ingrese el valor de la hora: ")
        print(f"EL salario del empleado es: {calcSalario(horas, valor):,.2f}")
    elif op == 1:
        print("\n1. Factorial de un numero")
        numero = readNum("Ingrese numero para sacar el Factorial: ")
        b = calcFactorial(numero)
        print(f"El factorial del numero {numero} es {b}")
    elif op == 3:
        print("\n3. Calcular palabras de un párrafo")
        parrafo = contPalabras("Ingrese el parrafo: ")
        print(f"La cantidad de palabras en el parrafo es: {parrafo}")
    elif op == 4:
        print("Gracias por usar mi programa <3.")
        input("Presione cualquier tecla para salir...")
        break




