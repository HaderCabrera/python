#NO ESTA COMPLETO.

import json

def guardarEmpleado(lstPersonal, ruta):
    # Función que guarda los datos de la lista de personal
    # en un arcivo JSON
    # Devuelve True: si los datos fueron guardados correctamente
    # Devuelve False: si los datos no se pudieron guardar
    
    try:
        fd = open(ruta, "w")
    except Exception as e:
        print("Error al abrir el archivo para guardar al empleado.\n", e)
        input("Presione cualquier tecla para continuar\n")
        return False
    
    try:
        json.dump(lstPersonal, fd)
    except Exception as e:
        print("Error al guardar la información del empleado.\n", e)
        input("Presione cualquier tecla para continuar\n")
        return False
    
    try:
        if not fd.closed:
            fd.close()
    except Exception as e:
        print("Error al cerrar el archivo.")
        input("Presione cualquier tecla para continuar\n")
        return False
    
    return True

def existeId(cod, lstLibreria):
    #funcion que encuentra la posición de un id en la lista
    # Devuelve un número enterior >= 0 si el id existe
    # Devuelve un -1 si el id NO existe
    for i, datos in enumerate(lstLibreria):
        # El método enumerate () agrega un contador a un iterable y 
        # lo devuelve en forma de objeto de enumeración. 
        # Este objeto enumerado puede usarse directamente para bucles 
        # o convertirse en una lista de tuplas usando la función list().
        k = int(list(datos.keys())[0])
        if k == cod:
            return i
    return -1

def borrarPersonal(lstPersonal, rutaFile):
    print("\n\n3. Borrar Personal")
    
    id = int(input("Ingrese el ID: "))
    if existeId(id, lstPersonal) == -1:
        # si existeId es -1 entonces no existe ese id en lstPersonal
        print("No existe un empleado con ese ID")
        input("Presione cualquier tecla para continuar\n")
        return None
    
    for i in range(len(lstPersonal)):
        datos = lstPersonal[i]
        k = int(list(datos.keys())[0])
        if k == id:
            del lstPersonal[i]
            break
    
    if guardarEmpleado(lstPersonal, rutaFile) == True:
        print("El empleado ha sido borrado con exito")
        input("Presione cualquier tecla para continuar\n")
    else:
        print("Ocurrio un error al borrar el empleado")
        input("Presione cualquier tecla para continuar\n")
        return None
    
    
def insertarLibro(lstLibreria, rutaFile):
    print("\n\n1. Agregar Personal")
    
    cod = int(input("Ingrese codigo del libro: "))
    while existeId(cod, lstLibreria) != -1:
        # si existeId es -1 entonces no existe ese id en lstPersonal
        # si es diferente a -1, entonces el id y existe.
        print("--> Ya existe un libro con ese CODIGO")
        input("Presione cualquier tecla para continuar\n")
        cod = int(input("\nIngrese el CODIGO: "))
        
    titulo = input("Titulo: ")
    autor = input("AUtor: ")
    precio = float(input("Precio: "))
 
    
    dicLibro = {}
    dicLibro[cod] = {"titulo":titulo, "autor":autor, "precio":precio}
    lstLibreria.append(dicLibro)

    ##################################################################################
    try:
        fd = open(rutaFile, "r")
        print("ENTRE AC1")
        json.dump(dicLibro,fd)
        input()
    except Exception as e:
        try:
            fd = open(rutaFile, "w")
            print("ENTRE ACA2")
            input()
        except Exception as d:
            print("Error al intentar abrir el archivo\n", d)
            input("Presione cualquier tecla para continuar\n")
            return None
    try:
        linea = fd.readline()
        if linea.strip() != "":
            fd.seek(0)
            input()
            json.dump(dicLibro,fd)

    except Exception as e:
        print("Error al cargar la información\n", e)
        input("Presione cualquier tecla para continuar\n")
        return None
    
    # print(lstPersonal)
    try:
        if not fd.closed:
            fd.close()
    except Exception as e:
        print("Error al cerrar el archivo.\n", e, "\n")
        input("Presione cualquier tecla para continuar\n")
        return None
    return lstLibreria

    input()

    ###################################################################################
    #PARA AGREGAR LA LISTA DE LIBROS NUEVA A DISCO
    if guardarEmpleado(lstLibreria, ruta) == True:
        input("El libro ha sido registrado con éxito.\nPresione cualquier tecla para continuar...")
    else:
        input("Ocurrio algún error al guardar el libro.")

def menu():
    while True:
        try:
            print("\n" * 30)
            print("*** LIBRERIA ***".center(40))
            print("MENU".center(40))
            print("1. Insertar")
            print("2. Consultar")
            print("3. Editar")
            print("4. Borrar")
            print("5. Salir")
            op = int(input(">>> Opción (1-5)? "))
            if op < 1 or op > 5:
                print("Opción no válida. Escoja de 1 a 5.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 5.")
            input("Presione cualquier tecla para continuar...")
            
def cargarInfo(lstPersonal, ruta):
    try:
        fd = open(ruta, "r")
    except Exception as e:
        try:
            fd = open(ruta, "w")
        except Exception as d:
            print("Error al intentar abrir el archivo\n", d)
            input("Presione cualquier tecla para continuar\n")
            return None
    try:
        linea = fd.readline()
        if linea.strip() != "":
            fd.seek(0)
            lstPersonal = json.load(fd)
        else:
            lstPersonal = []
    except Exception as e:
        print("Error al cargar la información\n", e)
        input("Presione cualquier tecla para continuar\n")
        return None
    
    # print(lstPersonal)
    try:
        if not fd.closed:
            fd.close()
    except Exception as e:
        print("Error al cerrar el archivo.\n", e, "\n")
        input("Presione cualquier tecla para continuar\n")
        return None
    return lstPersonal
    
# *** PROGRAMA PRINCIPAL ***
rutaFile = "hader_cabrera/talleres/datpersonal.json"
lstLibreria = []
lstLibreria =cargarInfo(lstLibreria, rutaFile)
while True:
    op = menu()
    if op == 1:
        insertarLibro(lstLibreria, rutaFile)
    elif op == 2:
        # Modificar
        pass
    elif op == 3:
        borrarPersonal(lstLibreria, rutaFile)
    elif op == 4:
        # Ver
        pass
    else:
        # Salir
        print("\nGracias por usar el programa")
        break
