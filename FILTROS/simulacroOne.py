almacenAcme = {}
listAlmacen = []
def filtro(id):
    tamaño = len(listAlmacen)
   # if tamaño > 0:
    for i in range(len(listAlmacen)):
        listaValores = listAlmacen[i].values()
        if id in listaValores:
            return True
def leerInt(msj):
    while True:
        try:
            id = int(input(msj))
            if id < 0:
                print("Ingrese un número positivo mayor a cero...")
                continue
            return id
        except ValueError:
            print("Error. Número invalido. ingrese número correcto")
def leerName(msj):
    while True:
        try:
            nombre = input(msj)
            nombre = nombre.strip()
            if len(nombre) == 0 or not nombre.isalnum():
                print("Nombre inválido")
                continue
            return nombre
        except Exception as e:
            print("Error al ingresar el nombre.", e)      
def ingresarValor(msj):
    while True:
        try:
            precio = float(input("Ingrese el valor del producto: "))
            if precio <= 0:
                print("Valor invalido. Debe ser mayor a 0. ")
                continue
            return precio
        except ValueError:
            print("Error al ingresar el valor del producto. Ingrese numero valido.")
def menu():
    while True:
        try:
            print("*** PRODUCTOS ACME ***".center(40))
            print("MENU".center(40))
            print("1. Agregar producto")
            print("2. Modificar producto")
            print("3. Eliminar producto")
            print("4. Listar varios productos")
            print("5. Estrategia de mercadeo")
            print("6. Salir")
            op = int(input(">>> Opción (1-6)? "))
            if op < 1 or op > 6:
                print("Opción no válida. Escoja de 1 a 6.")
                input("Presione cualquier tecla para continuar...")
                continue
            return op
        except ValueError:
            print("Opción no válida. Escoja de 1 a 6.")
            input("Presione cualquier tecla para continuar...")
def agregarProducto():
    print("\n\n*** 1. Agregar producto\n")
    datosProducto = {}
    #####
    dateProductos = {}
    #####
    id = leerInt("Ingrese el ID(Cod númerico) del producto: ")
    bandera = filtro(id)
    if bandera == True:
        print("El producto ya esta, para modificar vaya a la opcion 2.")
        input()
    else: 
        nombre = leerName("Ingrese el nombre del producto sin espacio: ")
        valorProducto = ingresarValor("Ingrese el valor del producto: ")
        cantidad = leerInt("Ingrese cuantas cantidad hay del producto: ")
        #CREO DIC DEL PRODUCTO
        datosProducto["nombre"] = nombre
        datosProducto["valorProducto"] = valorProducto
        datosProducto["cantidad"] = cantidad
        #CREO LISTA DEL PRODUCTO
        dateProductos["id"] = id
        dateProductos["nombre"] = nombre
        dateProductos["valorProducto"] = valorProducto
        dateProductos["cantidad"] = cantidad
        #AGREGO EL PRODUCTO AL ALMACEN CON LLAVE ID
        almacenAcme[id] = datosProducto
        #AGREGO EL PRODUCTO AL ALMACEN 
        listAlmacen.append(dateProductos)
def modificarProducto():
    producto = leerInt("Ingrese el ID del producto que quiere modificar: ")
    print("====QUE DESEA MODIFICAR?==== ")
    print("     1. Nombre")
    print("     2. Precio")
    print("     3. Cantidad")
    
    op = leerInt("Ingrese el dato que desea modificar: ")
    if op > 0 and op <= 3:
        if op == 1:
            almacenAcme[producto]["nombre"] = leerName("Ingrese el nuevo nombre del producto: ")
        if op == 2:
            almacenAcme[producto]["valorProducto"] = ingresarValor("Ingrese el nuevo precio del producto: ")
        if op == 3:
            almacenAcme[producto]["cantidad"] = leerInt("Ingrese el nuevo precio del producto: ")
    else:
        print("Digite un numero entre el 3 y el 1>>>")
def eliminarProducto():
    while True:
        try:
            producto = leerInt("Ingrese el ID del producto que quiere eliminar: ")
            del almacenAcme[producto]
            print(f"Elimine el producto {producto} de la base de datos.")
            break
        except KeyError:
            print("El producto no esta en la base de datos de ACME...")
def datosAlmacen():
    for k,v in almacenAcme.items():
        print(f"================__*{k}*__================")
        print(f'Producto =            {v["nombre"]}')
        print(f'Valor producto =    {v["valorProducto"]:,.0f}COP')
        print(f'Cantidad =          {v["cantidad"]} ')
        print("="*39) 
    input()   
def metodoBurbuja():
    #METODO BURBUJA
    N = len(listAlmacen)
    for i in range (0,N-1):
        for j in range(i+1,N):
            if listAlmacen[i]["valorProducto"] > listAlmacen[j]["valorProducto"]:
                t = listAlmacen[i]
                listAlmacen[i] = listAlmacen[j]
                listAlmacen[j] = t
    return listAlmacen
def estrategiaMercadeo(almacen):
    bandera = 0
    while True:
        if len(almacen) <= 5:
            for m in range(len(almacen)):
                print(f'===============__*{almacen[m]["id"]}*__===============')
                print(f'Producto =  {almacen[m]["nombre"]}')
                print(f'Precio =    {almacen[m]["valorProducto"]:,.0f}COP')
                print(f'Cantidad =  {almacen[m]["cantidad"]}')
                print("="*40)
            input()   
            break
        elif len(almacen) > 5:
            for m in range(len(almacen)):
                    print(f'===============__*{almacen[m]["id"]}*__===============')
                    print(f'Producto =  {almacen[m]["nombre"]}')
                    print(f'Precio =    {almacen[m]["valorProducto"]:,.0f}COP')
                    print(f'Cantidad =  {almacen[m]["cantidad"]}')
                    print("="*40)
                    bandera += 1
                    if bandera == 5:
                        input("Digite cualquier tecla para continuar >>> ")
                        bandera = 0
            input()
            break
while True:
    op = menu()
    if op == 1:
        agregarProducto()
    elif op == 2:
        modificarProducto()
    elif op == 3:
        eliminarProducto()     
    elif op == 4:
        datosAlmacen()
    elif op == 5:
        almacen = metodoBurbuja()
        estrategiaMercadeo(almacen)
    elif op == 6:
        print("\n\nGracias por usar el software. Adios")
        break