import json


#CAMBIAR RUTA DE FICHERO CVS
##CAMBIAR RUTA DE FICHERO CVS
###CAMBIAR RUTA DE FICHERO CVS
def tomarDatosPais(rutaJeison):

    ruta = "talleres/datosPais.txt"
    fd = open(ruta, "r")
    lstObservatorios = []
    dicObservatorio = {}
    fd.readline()
    for linea in fd:
        linea.strip("\n")
        dicObservatorio["codigo"] = int(linea.split(";")[0])
        dicObservatorio["nombre"] = linea.split(";")[1]
        dicObservatorio["fecha"] = linea.split(";")[2]
        dicObservatorio["tempmax"] = float(linea.split(";")[3])
        dicObservatorio["tempmin"] = float(linea.split(";")[4])
        lstObservatorios.append(dicObservatorio)
        dicObservatorio = {}    
    fd.close
    if cargarDatosJson(lstObservatorios,rutaJeison) == True:
        print("Informacion cargada a JSON con EXITO.")
    
    return lstObservatorios

def cargarDatosJson(lstObservatorios,rutaJeison):

    
    ruta = rutaJeison
    try:
      fj = open(ruta,"w")
    except Exception as e:
        print("Error al abrir el archivo para guardar al empleado.\n", e)
        input("Presione cualquier tecla para continuar\n")
        return False
    
    try:
        json.dump(lstObservatorios, fj)
    except Exception as e:
        print("Error al guardar la información del observatorio.\n", e)
        input("Presione cualquier tecla para continuar\n")
        return False
    
    try:
        if not fj.closed:
            fj.close()
    except Exception as e:
        print("Error al cerrar el archivo.")
        input("Presione cualquier tecla para continuar\n")
        return False
    
    return True    

def tomarDatosJson(rutaJeison):

    ruta = rutaJeison
    try:
        fd = open(ruta, "r")
    except Exception as e:
        try:
            fd = open(ruta, "w")
        except Exception as d:
            print("Error al intentar abrir el archivo\n", d)
            #input("Presione cualquier tecla para continuar\n")
        return False
    try:
        linea = fd.readline()
        if linea.strip() != "":
            fd.seek(0)
            lstObservatorios = json.load(fd)
        else:
            return False
    except Exception as e:
        print("Error al cargar la información\n", e)
        input("Presione cualquier tecla para continuar\n")
        return False
    return lstObservatorios

def metodoBurbuja(lstObservatorio, caso):

    if caso == 1:
        N = len(lstObservatorio)
        for i in range(0, N - 1):
            for j in range( i + 1, N):
                if lstObservatorio[i]["codigo"] > lstObservatorio[j]["codigo"]:
                    t = lstObservatorio[i]
                    lstObservatorio[i] = lstObservatorio[j]
                    lstObservatorio[j] = t
        return lstObservatorio
    
    elif caso == 2:
        N = len(lstObservatorio)
        for i in range(0, N - 1):
            for j in range( i + 1, N):
                if lstObservatorio[i]["nombre"] > lstObservatorio[j]["nombre"]:
                    t = lstObservatorio[i]
                    lstObservatorio[i] = lstObservatorio[j]
                    lstObservatorio[j] = t
        return lstObservatorio

    elif caso == 3:
        fecha = str(lstObservatorio[0]["fecha"]).split("/")[0]
        N = len(lstObservatorio)
        for i in range(0, N - 1):
            for j in range( i + 1, N):
                if str(lstObservatorio[i]["fecha"]).split("/")[2] > str(lstObservatorio[j]["fecha"]).split("/")[2]:
                    t = lstObservatorio[i]
                    lstObservatorio[i] = lstObservatorio[j]
                    lstObservatorio[j] = t
                elif str(lstObservatorio[i]["fecha"]).split("/")[2] == str(lstObservatorio[j]["fecha"]).split("/")[2]:
                    if str(lstObservatorio[i]["fecha"]).split("/")[1] > str(lstObservatorio[j]["fecha"]).split("/")[1]:
                        t = lstObservatorio[i]
                        lstObservatorio[i] = lstObservatorio[j]
                        lstObservatorio[j] = t 
                    elif str(lstObservatorio[i]["fecha"]).split("/")[1] == str(lstObservatorio[j]["fecha"]).split("/")[1]:
                        if str(lstObservatorio[i]["fecha"]).split("/")[0] > str(lstObservatorio[j]["fecha"]).split("/")[0]:
                            t = lstObservatorio[i]
                            lstObservatorio[i] = lstObservatorio[j]
                            lstObservatorio[j] = t 

        return lstObservatorio
#HALLA TEMP MAXIMO, TEMP MINIMO Y PROMEDIO DE UNA LISTA DE OBSERVATORIO 
    elif caso == 4:
        acumuladorTempMin = 0
        acumuladorTempMax = 0
        N = len(lstObservatorio)
        for i in range(0, N - 1):
            for j in range( i + 1, N):
                if lstObservatorio[i]["tempmax"] < lstObservatorio[j]["tempmax"]:
                    t = lstObservatorio[i]
                    lstObservatorio[i] = lstObservatorio[j]
                    lstObservatorio[j] = t
        tempMax = lstObservatorio[0]["tempmax"]
        for i in range(0, N - 1):
            for j in range( i + 1, N):
                if lstObservatorio[i]["tempmin"] < lstObservatorio[j]["tempmin"]:
                    t = lstObservatorio[i]
                    lstObservatorio[i] = lstObservatorio[j]
                    lstObservatorio[j] = t
        tempMin = lstObservatorio[0]["tempmin"]


        for i in range(len(lstObservatorio)):
            acumuladorTempMax += lstObservatorio[i]["tempmax"]
            acumuladorTempMin += lstObservatorio[i]["tempmin"]
        promedio = ((acumuladorTempMax / len(lstObservatorio))+ (acumuladorTempMin / len(lstObservatorio))) / 2

        return tempMax,tempMin, promedio
#LISTAR POR TEMPERATURA
    elif caso == 6:

        N = len(lstObservatorio)
        for i in range(0, N - 1):
            for j in range( i + 1, N):
                if ((lstObservatorio[i]["tempmax"] + lstObservatorio[i]["tempmin"]) / 2) > ((lstObservatorio[j]["tempmax"] + lstObservatorio[j]["tempmin"]) / 2):
                    t = lstObservatorio[i]
                    lstObservatorio[i] = lstObservatorio[j]
                    lstObservatorio[j] = t
        return lstObservatorio
    
def imprimirPaginacion(lstObservatorio):
    contador = 0
    for i in range(len(lstObservatorio)):
        print(f'{lstObservatorio[i]["fecha"]} TempMax = {lstObservatorio[i]["tempmax"]} TempMin = {lstObservatorio[i]["tempmin"]}'.center(40))
        contador += 1
        if contador%10 == 0 and contador != 0:
            input(">>>Presiones una tecla para continuar: ")
            contador = 0
        
def buscarID(lstObservatorios, id):
    for i in range(len(lstObservatorios)):
        if id == lstObservatorios[i]["codigo"]:
            return True
    return False

def menu():
    print("_"*30)
    print("OBSERVATORIOS".center(25))
    print("-"*30)
    print("1. Listado por codigos.")
    print("2. Listado por nombres.")
    print("3. Listado por codigo.")
    print("4. Listado de cantidades.")
    print("5. Listado nacional (paginacion).")
    print("6. Listado nacional (temperaturas).")
    print("7. Exit.")
    print("-"*30)
    while True:
        try:
            opcion = int(input(">>> Que desea realizar? "))
            if 1 < opcion > 7 :
                print("Wrong number.[1 - 7]>>> ")
                continue
            return opcion
        except  ValueError:
            print("Error. Digite un numero correcto.")

#PROGRAMA PRINCIPAL
rutaJeison = "talleres/observatoriosJson.json"

while True:

    tomarDatosPais(rutaJeison)
    opcion = menu()
    lstObservatorio = []

    if opcion == 1:
        lstObservatorios = tomarDatosJson(rutaJeison)
        ordenado = metodoBurbuja(lstObservatorios,1)
        print("="*62)
        for i in range(len(ordenado)):
            print(f'ID = {ordenado[i]["codigo"]}    NOMBRE = {ordenado[i]["nombre"]}    TEMPERATURE = {ordenado[i]["tempmax"]} - {ordenado[i]["tempmin"]}')
        print("="*62)
        input()

    elif opcion == 2:
        lstObservatorios = tomarDatosJson(rutaJeison)
        ordenado = metodoBurbuja(lstObservatorios,2)
        print("="*62)
        for i in range(len(ordenado)):
            print(f'NOMBRE = {ordenado[i]["nombre"]}    ID = {ordenado[i]["codigo"]}      TEMPERATURE = {ordenado[i]["tempmax"]} - {ordenado[i]["tempmin"]}')
        print("="*62)
        input()

    elif opcion == 3:
        codigo = int(input("Indique el codigo del observatorio que quiere consultar: "))
        lstObservatorios = tomarDatosJson(rutaJeison)
        if buscarID(lstObservatorios, codigo) == True:
            for i in range(len(lstObservatorios)):
                if codigo == lstObservatorios[i]["codigo"]:
                    lstObservatorio.append(lstObservatorios[i])
            imprimir = metodoBurbuja(lstObservatorio,3)

            print("="*44)
            print(f'{codigo} [{imprimir[0]["nombre"]}]'.center(40))
            for i in range(len(imprimir)):
                print(f'FECHA = {imprimir[i]["fecha"]} TEMPERATURE = {imprimir[i]["tempmax"]} - {imprimir[i]["tempmin"]}')
            print("="*44)
            input()
        else:
            print("")
            input("El ID no existe, digite una tecla para continuar...")
    
    elif opcion == 4:
        
        codigo = int(input("Indique el codigo del observatorio que quiere consultar: "))
        lstObservatorios = tomarDatosJson(rutaJeison)
        if buscarID(lstObservatorios, codigo) == True:
            for i in range(len(lstObservatorios)):
                if codigo == lstObservatorios[i]["codigo"]:
                    lstObservatorio.append(lstObservatorios[i])

            cantidad = len(lstObservatorio)
            tempMax,tempMin,promedio = metodoBurbuja(lstObservatorio,4)

            print("="*38)
            print(f'{codigo} [{lstObservatorio[0]["nombre"]}] || {cantidad} OBSERVACIONES'.center(40))
            print("_"*38)
            print(f"Tmax = {tempMax}")
            print(f"Tmin = {tempMin}")
            print(f"Temperatura promedio = {promedio:.2f}")
            print("="*38)
            input()
        else:
            input("El ID no existe, digite cualquier tecla para continuar...")

    elif opcion == 5:
        lstObservatorios = tomarDatosJson(rutaJeison)
        ordenado = metodoBurbuja(lstObservatorios,1)
        lstObservatorio = []
        for i in range(len(ordenado)):
            if i == len(ordenado) - 1:
                lstObservatorio.append(ordenado[i])
                tmax,tmin,prom = metodoBurbuja(lstObservatorio,4)
                cantidad = len(lstObservatorio)
                print("="*38)
                print(f'{lstObservatorio[0]["codigo"]} [{lstObservatorio[0]["nombre"]}] || {cantidad} OBSERVACIONES '.center(40))
                print(f"Temperatura promedio = {prom:3f}".center(40))
                print("_"*38)
                imprimirPaginacion(lstObservatorio)
                print("="*38)
                input()
                break
            if ordenado[i]["codigo"] == ordenado[i+1]["codigo"]:
                lstObservatorio.append(ordenado[i])
            else:
                lstObservatorio.append(ordenado[i])
                tmax,tmin,prom = metodoBurbuja(lstObservatorio,4)
                cantidad = len(lstObservatorio)
                print("="*38)
                print(f'{lstObservatorio[0]["codigo"]} [{lstObservatorio[0]["nombre"]}] || {cantidad} OBSERVACIONES '.center(40))
                print(f"Temperatura promedio = {prom:3f}".center(40))
                print("_"*38)
                imprimirPaginacion(lstObservatorio)
                print("="*38)
                lstObservatorio = []
   
    elif opcion == 6:

        lstObservatorios = tomarDatosJson(rutaJeison)
        ordenado = metodoBurbuja(lstObservatorios,1)
        lstObservatorio = []
        for i in range(len(ordenado)):
                if i == len(ordenado) - 1:
                    lstObservatorio.append(ordenado[i])
                    imprimir = metodoBurbuja(lstObservatorio,6)
                    cantidad = len(lstObservatorio)
                    print("="*38)
                    print(f'{lstObservatorio[0]["codigo"]} [{lstObservatorio[0]["nombre"]}] || {cantidad} OBSERVACIONES '.center(40))
                    print("_"*38)
                    for m in range(len(imprimir)):
                        print(f' {imprimir[m]["fecha"]} || {imprimir[m]["tempmax"]} || {imprimir[m]["tempmin"]}')
                        print()
                    print("="*38)
                    input()
                    break
                if ordenado[i]["codigo"] == ordenado[i+1]["codigo"]:
                    lstObservatorio.append(ordenado[i])
                else:
                    lstObservatorio.append(ordenado[i])
                    imprimir = metodoBurbuja(lstObservatorio,6)
                    cantidad = len(lstObservatorio)
                    print("="*38)
                    print(f'{lstObservatorio[0]["codigo"]} [{lstObservatorio[0]["nombre"]}] || {cantidad} OBSERVACIONES '.center(40))
                    print("_"*38)
                    for m in range(len(imprimir)):
                        print(f' {imprimir[m]["fecha"]} || {imprimir[m]["tempmax"]} || {imprimir[m]["tempmin"]}')
                        print()
                    print("="*38)
                    input()
                    lstObservatorio = []

    elif opcion == 7:
        break
