import json
#CARGAR ARCHIVO JSON
#SI NO LOGRA ABRIRSE POR W RETORNA FALSO
#SI NO LOGRA HACER EL DUMP RETORNA FALSO
#SI SALE BIEN RETORNA TRUE
def cargarGanador(ganadores):
    
    ruta = "hader_cabrera\\talleres\\ganadores_json.json"
    try:
      fp = open(ruta,"w")
    except Exception as e:
        print("Error al abrir el archivo para guardar al empleado.\n", e)
        input("Presione cualquier tecla para continuar\n")
        return False
    
    try:
        json.dump(ganadores, fp)
    except Exception as e:
        print("Error al guardar la información del empleado.\n", e)
        input("Presione cualquier tecla para continuar\n")
        return False
    
    try:
        if not fp.closed:
            fp.close()
    except Exception as e:
        print("Error al cerrar el archivo.")
        input("Presione cualquier tecla para continuar\n")
        return False
    
    return True

#INTENTA ABRIR EL ARCHIVO EN R, SINO LO LOGRA LO INTENTA EN W
#SI ABRE EN W RETORNA FALSE
#SI ABRIO EN R INTENTA LEER CON READLINE. 
#SI NO ESTA VACIO HACE (LOAD) Y RETORNA
#SI ESTA VACIO RETORNA FALSE
def getGanadores():
    ruta = "hader_cabrera\\talleres\\ganadores_json.json"
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
            discGanadores = json.load(fd)
        else:
            return False
    except Exception as e:
        print("Error al cargar la información\n", e)
        input("Presione cualquier tecla para continuar\n")
        return False
    return discGanadores