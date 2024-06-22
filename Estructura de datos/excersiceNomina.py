def leerValHoraEmpl():
    while True:
        try:
            n = int(input("Ingrese el valor de la hora trabajada del empleado: "))
            if n < 8000 or n > 150000:
                print("Valor de la Hora inválida. Debe estar en el rango de [8000, 150000]")
                continue
            return n
        except ValueError:
            print("Error al ingresar el valor de la hora trabajada.")

def leerHoraTrabEmpl():
    while True:
        try:
            n = int(input("Ingrese la horas trabajadas del empleado: "))
            if n < 0 or n > 160:
                print("Horas inválidas. Debe estar en el rango de [0, 160]")
                continue
            return n
        except ValueError:
            print("Error al ingresar las horas.")

def leerNombreEmpl():
    while True:
        try:
            nom = input("Ingrese el nombre del empleado:")
            nom = nom.strip()
            if len(nom) == 0 or not nom.isalnum():
                print("Nombre inválido")
                continue
            return nom
        except Exception as e:
            print("Error al ingresar el nombre.", e)

def leerIDEmpl():
    while True:
        try:
            n = int(input("Ingrese el ID del empleado: "))
            if n < 1:
                print("ID inválido. Debe ser mayor a cero")
                continue
            return n
        except ValueError:
            print("Error al ingresar el ID.")
            
def buscarEmpleado(lstEmpleado, idEmpl):
    for i in range(len(lstEmpleado)):
        if (lstEmpleado[i][0] == idEmpl):
            return i
    return -1


def modificarEmpleado(lstEmpleado):
    print("\n\n2. Modificar Empleado\n")
    
    idEmpl = leerIDEmpl()
    posEmpl = buscarEmpleado(lstEmpleado, idEmpl)
    if posEmpl == -1:
        print("El código del empleado no existe.")
        input()
        return
    
    print("\n")
    while True:
        op = int(input("\n1. Nombre\n2. Cantidad de Horas\n3. Valor de la hora\nOpcion? "))
        if op < 1 or op > 3:
            print("Opción inválida")
            input()
            continue
        break
    
    if op == 1:
        nombre = leerNombreEmpl()
        lstEmpleado[posEmpl][1] = nombre
    elif op == 2:
        cantHoras = leerHoraTrabEmpl()
        lstEmpleado[posEmpl][2] = cantHoras
    elif op == 3:
        valHora = leerValHoraEmpl()
        lstEmpleado[posEmpl][3] = valHora

def agregarEmpleado(lstEmpleado):
    print("\n\n*** 1. Agregar empleado\n")
    lstDatos = []
    id = leerIDEmpl()
    if buscarEmpleado(lstEmpleado, id) != -1:
        print("El id ya existe en la lista")
        input()
        return
    lstDatos.append(id)
    lstDatos.append(leerNombreEmpl())
    lstDatos.append(leerHoraTrabEmpl())
    lstDatos.append(leerValHoraEmpl()) 
    lstEmpleado.append(lstDatos)

def deletEmpleado(lstEmpleado):
    pos = buscarEmpleado(lstEmpleado, leerIDEmpl())
    if pos != -1:
        lstEmpleado.pop(pos)
        print("     DI DE BAJA A UNO :(")
    else:
        print("     EL ID INGRESADO YA SE FUE :DD")

def listarEmpleados(lstEmpleado):
    bandera1 = 0
    while True:
        tamaña = len(lstEmpleado)
        if tamaña <= 5:
            for m in range(tamaña):
                print(lstEmpleado[m])
            input()
            break
        elif tamaña > 5:
            for l in range(5):
                if bandera1 < tamaña:
                    print(lstEmpleado[bandera1])
                    bandera1 += 1
                else:
                    print("NO HAY MAS EMPLEADO.")
                    break
            bandera2 = input("Desea continuar? (S//N)")
            if  bandera2.lower() != "s":
                break
    
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
            print("6. Listar nómina de un empleado")
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

def nominaEmpleado(lstEmpleado,Id):
    empleado = buscarEmpleado(lstEmpleado,Id)
    saldoBruto = lstEmpleado[empleado][2] * lstEmpleado[empleado][3]
    destEpsPension = saldoBruto * 0.08
    if saldoBruto <= 1160000:
        nomina = saldoBruto + 140000 - destEpsPension
        
        print("\n======================NOMINA===========================")
        print(f"ID = {lstEmpleado[empleado][0]}     Empleado = {lstEmpleado[empleado][1]} ")
        print("=========================================================")
        print(f"Saldo Bruto:            ${saldoBruto:,.0f}COP")
        print(f"Descuento S-P:              ${destEpsPension:,.0f}COP")
        print(f"Auxilio de transporte:          $140,000COP")
        print(f"Saldo neto:             ${nomina:,.0f}COP")
        #print(f"El sueldo del empleado es :{nomina:,.0f} ")
        input()
    else:
        nomina = saldoBruto - destEpsPension
        print("\n======================NOMINA===========================")
        print(f"ID = {lstEmpleado[empleado][0]}     Empleado = {lstEmpleado[empleado][1]} ")
        print("=========================================================")
        print(f"Saldo Bruto:            ${saldoBruto:,.0f}COP")
        print(f"Descuento S-P:              ${destEpsPension:,.0f}COP")
        print(f"Saldo neto:             ${nomina:,.0f}COP")
        #print(f"El sueldo del empleado es :{nomina:,.0f} ")
        input()
#calcular nomina de empleado sin preguntar ID
def calNomina():
    AUXTRANS = 140000
    for m in range(len(lstEmpleado)):
        saldoBruto = lstEmpleado[m][3] * lstEmpleado[m][2]
        descuento = saldoBruto * 0.08
        if saldoBruto <= 1160000:
            saldoNeto = saldoBruto - descuento + AUXTRANS
            print("\n======================NOMINA===========================")
            print(f"ID = {lstEmpleado[m][0]}     Empleado = {lstEmpleado[m][1]} ")
            print("=========================================================")
            print(f"Saldo Bruto:            ${saldoBruto:,.0f}COP")
            print(f"Descuento S-P:          ${descuento:,.0f}COP")
            print(f"Auxilio de transporte:  ${AUXTRANS:,.0f}COP")
            print(f"Saldo neto:             ${saldoNeto:,.0f}COP")
            input()
        else:
            saldoNeto = saldoBruto - descuento
            print("\n======================NOMINA===========================")
            print(f"ID = {lstEmpleado[m][0]}     Empleado = {lstEmpleado[m][1]} ")
            print("=========================================================")
            print(f"Saldo Bruto:            ${saldoBruto:,.0f}COP")
            print(f"Descuento S-P:          ${descuento:,.0f}COP")
            print(f"Saldo neto:             ${saldoNeto:,.0f}COP")
            input()

def listarNomina(lstEmpelado):
    pass
    
## PROGRAMA PRINCIPAL
lstEmpleado = []
while True:
    op = menu()
    if op == 1:
        agregarEmpleado(lstEmpleado)
        print(lstEmpleado)
        input()
    elif op == 2:
        modificarEmpleado(lstEmpleado)
    elif op == 3:
        
        empleado = buscarEmpleado(lstEmpleado,leerIDEmpl())
        print("\nLos datos del empleado son : ")
        print("ID ==", lstEmpleado[empleado][0])
        print("NOMBRE ==", lstEmpleado[empleado][1])
        print("HORAS ==", lstEmpleado[empleado][2])
        print("VALORHORAS ==", lstEmpleado[empleado][3])
        input()
        
    elif op == 4:
        deletEmpleado(lstEmpleado)
    elif op == 5:
        listarEmpleados(lstEmpleado)
    elif op == 6:
        nominaEmpleado(lstEmpleado,leerIDEmpl())
    elif op == 7:
        calNomina()
    elif op == 8:
        print("\n\nGracias por usar el software. Adios")
        break
