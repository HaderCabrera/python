#EJERCICIO 1
"""
bandera = True
cedula = "1"
type1 = "Puerta a puerta"
type2 = "Telemercadeo"
type3 = "Ejecutivo de ventas"
sumatoriaVentas = 0
sumatoriaComisiones = 0

while bandera == True:
   
        cedula = input("Ingrese el numero de la cedula: ")
        if cedula != "-1":
            name = input("Ingrese el nombre del vendedor: ")
            contVentas = float(input("Cuanto vendio en el mes: "))
            vendedor = int(input(f"Ingrese el tipo de vendedor, donde:\n          [1]->{type1}\n          [2]->{type2}\n          [3]->{type3}\n ¿Que tipo de vendedor es?: "))

            if vendedor == 1:
                comision = contVentas*(0.2)
                print(f"{name} identificado con CC. {cedula} comisiono en el mes: ${comision:,.0f} COP")
            elif vendedor == 2:
                comision = contVentas*(0.15)
                print(f"{name} identificado con CC. {cedula} comisiono en el mes: ${comision:,.0f} COP")
            elif vendedor == 3:
                comision = contVentas*(0.25)
                print(f"{name} identificado con CC. {cedula} comisiono en el mes: ${comision:,.0f} COP")
            sumatoriaVentas += contVentas
            sumatoriaComisiones += comision
        else:
             bandera = False
print("="*10,"INFORMES DEL MES","="*10)     
print(f"En el mes se vendio: ${sumatoriaVentas:,.0f} COP")
print(f"En el mes los empleados comisionaron : ${sumatoriaComisiones:,.0f} COP")

#EJERCICIO 2
bandera = True
gananciaConductores = 0
contNovatos = 0
contExpert = 0
while bandera == True:
    cantidadConductores = int(input("¿Cuantos conductores son? "))
    for i in range(cantidadConductores):
        cedula = input("\nIngrese la cedula del conductor:  ")
        name = input("Ingrese el nombre del conductor:  ")
        claseConductor = int(input("Ingrese la clase del conducor siendo:\n          [1]->Experto\n          [2]->Novato\nLa clase es: "))
        ingresosPasajes = float(input("Cuantas ganancias genero por pasajes? "))
        ingresoEncomiendad = float(input("¿Cuantas ganancias genero por encomiendad? "))

        if claseConductor == 1:
            ganancias = ingresosPasajes*0.3 + ingresoEncomiendad*0.2
            contExpert += 1
            print(f"El conductor {name} obtuvo una ganancia de : ${ganancias:,.0f}")
        elif claseConductor == 2:
            ganancias = ingresosPasajes*0.2 + ingresoEncomiendad*0.15
            contNovatos += 1
            print(f"El conductor {name} obtuvo una ganancia de : ${ganancias:,.0f}")
    bandera = False
    gananciaConductores += ganancias
print("="*18,"INFORME GENERAL","="*18)
print(f"El valor total a pagar a los conductores es: ${gananciaConductores:,.0f} COP")
print(f"La cantidad de conductores NOVATOS es :{contNovatos} y la cantidad de conductores EXPERTOS es:{contExpert}")
""" 

#EJERCICIO 3
bandera = True
pagarGeneral = 0
contA = 0
contB = 0
contC = 0
while bandera == True:
    cantDocentes = int(input("¿Cuantos docentes son? "))
    for i in range(cantDocentes):
        documento = input("Ingrese el documento del docente: ")
        name = input("Ingrese el nombre del docente: ")
        contHoras = int(input("Ingrese la cantidad de horas laboradas: "))
        categoria = input("Ingrese la categoria del docente: A, B o C \nLa categoria del docente e :")

        if categoria == "A" or categoria =="a":
            salario = contHoras*25000
            contA += 1
            print(f"el salario de {name} es: ${salario:,.0f}")
        elif categoria == "B" or categoria == "b":
            salario = contHoras*35000
            print(f"el salario de {name} es: ${salario:,.0f}")
            contB += 1
        elif categoria == "C" or categoria == "c":
            salario = contHoras*50000
            print(f"el salario de {name} es: ${salario:,.0f}")
            contC += 1
        pagarGeneral += salario

    bandera = False
print("="*18,"INFORME GENERAL","="*18)
print(f"Las ganacias de todos los docentes es: ${pagarGeneral:,.0f}")
print(f"Hay {contA} docentes categoria A,{contB} categoria B y {contC} categoria C")
