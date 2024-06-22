dicEmpresa = {}
def menu():
    while True:
        try:
            print("*** NOMINA ACME ***".center(40))
            print("MENU".center(40))
            print("1. Agregar empleado")
            print("2. Modificar empleado")
            print("3. Buscar emplado")
            print("4. Eliminar empleado")
            print("5. Listar empleados")
            print("6. Nómina de un empleado")
            print("7. Listar nómina de todos los empleados")
            print("8. Salir")
            op = int(input(">>> Opción (1-8)? "))
            if op < 1 or op > 8:
                print("Opción no válida. Escoja de 1 a 8.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 8.")
            input("Presione cualquier tecla para continuar...")
def agregarEmpleado():
    dicEmpleado = {}
    id = int(input("Digite el ID del empelado (cedula): "))
    dicEmpleado["Nombre"] = input("Ingrese el nombre del empleado: ")
    dicEmpleado["horasTrabajadas"] = int(input("Ingrese cuantas horas trabajo [1h -> 160h]: "))
    dicEmpleado["valorHora"] = float(input("Digite el valor de la hora [8k -> 150k]: "))
    dicEmpresa[id] = dicEmpleado
def modificarEmpleado():
    empleado = int(input("Digite el ID [CC] del empleado que desea modificar: "))
    print("====QUE DESEA MODIFICAR?==== ")
    print("     1. Nombre")
    print("     2. horasTrabajadas")
    print("     3. valorHora")
    op = int(input("Digite la opcion que desea modificar: "))
    if op == 1:
        dicEmpresa[empleado]["Nombre"] = input("    Ingrese el nuevo nombre >>> ")
    if op == 2:
        dicEmpresa[empleado]["horasTrabajadas"] = input("   Ingrese la nueva cantidad de horas >>> ")
    if op == 3:
        dicEmpresa[empleado]["valorHora"] = float(input("   Ingrese el nuevo valor de la hora >>> "))
def buscarEmpleado():
    empleado = int(input("Ingrese el ID(CC) del usuario que quiere buscar >>> "))
 #   for a,b in dicEmpresa.items():
    return empleado, dicEmpresa.get(empleado)
def eliminarEmpleado():
    while True:
        try:
            empleado = int(input("Ingrese el ID del empleado que quiere dar de baja? "))
            del dicEmpresa[empleado]
            print(f"Elimine al usuario {empleado} de la base de datos.")
            input()
            break
        except KeyError:
            print("El empleado ya no esta aca...")
def listarEmpleados():
    bandera = 0
    while True:
        if len(dicEmpresa) <= 5:
            for empleado, listEmpresa in dicEmpresa.items():
                print(f"========__*{empleado}*__========")
                print(f'Nombre = {listEmpresa["Nombre"]}')
                print(f'Horas trabajadas = {listEmpresa["horasTrabajadas"]}')
                print(f'Valor hora = {listEmpresa["valorHora"]:,.0f} COP')
                print("="*40) 
            input()   
            break
        elif len(dicEmpresa) > 5:
            for empleado, listEmpresa in dicEmpresa.items():
                if bandera < len(dicEmpresa):
                    print(f"========__*{empleado}*__========")
                    print(f'Nombre = {listEmpresa["Nombre"]}')
                    print(f'Horas trabajadas = {listEmpresa["horasTrabajadas"]}')
                    print(f'Valor hora = {listEmpresa["valorHora"]:,.0f} COP')
                    print("="*40) 
                    bandera += 1
                    if bandera == 5:
                        input("Digite cualquier tecla para continuar >>> ")
                        bandera = 0
                        continue
                else:
                    break
            input()
            break
def nominaEmpleado():
    empleado = int(input("Ingrese el ID(CC) del empleado: "))
    MINIMO = 1160000
    AUXTRANS = 140000
    salarioBruto = dicEmpresa[empleado]["horasTrabajadas"] * dicEmpresa[empleado]["valorHora"]
    descuentos = salarioBruto * 0.08
    if salarioBruto <= 1160000:
        salarioNeto = salarioBruto + AUXTRANS - descuentos
        print("\n======================NOMINA===========================")
        print(f'        ID = {empleado}     Empleado = {dicEmpresa[empleado]["Nombre"]}')
        print("=========================================================")
        print(f"Saldo Bruto:                ${salarioBruto:,.0f}COP")
        print(f"Descuento S-P:              ${descuentos:,.0f}COP")
        print(f"Auxilio de transporte:      ${AUXTRANS:,.0f} COP")
        print(f"Saldo neto:                 ${salarioNeto:,.0f}COP")
        input()
    else:
        salarioNeto = salarioBruto - descuentos
        print("\n======================NOMINA===========================")
        print(f'        ID = {empleado}     Empleado = {dicEmpresa[empleado]["Nombre"]}')
        print("=========================================================")
        print(f"Saldo Bruto:            ${salarioBruto:,.0f}COP")
        print(f"Descuento S-P:          ${descuentos:,.0f}COP")
        print(f"Saldo neto:             ${salarioNeto:,.0f}COP")
        input()
def calcularNomina():
    pass
def listarNomina():
    pass

while True:
    opcion = menu()
    if opcion == 1:
        agregarEmpleado()
        print(dicEmpresa)
    elif opcion == 2:
        modificarEmpleado()
        print(dicEmpresa)
    elif opcion == 3:
        id,datos = buscarEmpleado()
        print(f"\n=====*__{id}__*=====")
        print(f'Nombre = {datos["Nombre"]}')
        print(f'Horas trabajadas = {datos["horasTrabajadas"]}')
        print(f'Valor hora = {datos["valorHora"]:,.0f} COP')
        input()
    elif opcion == 4:
        eliminarEmpleado()
    elif opcion == 5:
        listarEmpleados()
    elif opcion == 6:
        nominaEmpleado()
    elif opcion == 7:
        pass
    elif opcion == 8:
        break



