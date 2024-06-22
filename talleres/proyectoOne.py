#DOS JUGADORES
#JUGAR, IMPRIMIR TABLA DE CLASIFICATORIA 
#SALIR
import time
import json

def ingresarJugador(msj):
    while True:
        try:
            nom = input(msj)
            nom = nom.strip()
            if len(nom) == 0 or not nom.isalnum():
                print("Nombre inválido")
                continue
            return nom
        except Exception as e:
            print("Error al ingresar el nombre.", e)

def crearMatrix():
    matrix = []
    for i in range(3):
        fila = [0] * 3
        matrix.append(fila)
    
    contador = 1
    for f in range(3):
        for c in range(3):
            matrix[f][c] = contador
            contador += 1
    return matrix

def menu():
    while True:
        try:
            print("="*35)
            print("TRIQUI // MENU".center(35))
            print("="*35)
            print("1. Jugar.")
            print("2. Tabla clasificatoria.")
            print("3. Salir.")
            print("-"*35)

            opc = int(input(("\n>>>Digite una opcion: ")))
            if opc < 1 or opc > 3:
                print("Opción no válida. Escoja de 1 a 3.")
                input("Presione cualquier tecla para continuar...")
                continue
            return opc
        except ValueError:
            print("Opción no válida. Escoja de 1 a 3.")
            input("Presione cualquier tecla para continuar...")

def llenarMatrix(matJuego,casilla, ficha):

    if casilla == 1:
        if matJuego[0][0] == 1:
            matJuego[0][0] = ficha
        else:
            print("La casilla ya esta en uso.")
            return False
    elif casilla == 2:
        if matJuego[0][1] == 2:
            matJuego[0][1] = ficha
        else:
            print("La casilla ya esta en uso.")
            return False
    if casilla == 3:
        if matJuego[0][2] == 3:
            matJuego[0][2] = ficha
        else:
            print("La casilla ya esta en uso.")
            return False
    elif casilla == 4:
        if matJuego[1][0] == 4:
            matJuego[1][0] = ficha
        else:
            print("La casilla ya esta en uso.")
            return False

    if casilla == 5:
        if matJuego[1][1] == 5:
            matJuego[1][1] = ficha
        else:
            print("La casilla ya esta en uso.")
            return False
    elif casilla == 6:
        if matJuego[1][2] == 6:
            matJuego[1][2] = ficha
        else:
            print("La casilla ya esta en uso.")
            return False
    if casilla == 7:
        if matJuego[2][0] == 7:
            matJuego[2][0] = ficha
        else:
            print("La casilla ya esta en uso.")
            return False
    elif casilla == 8:
        if matJuego[2][1] == 8:
            matJuego[2][1] = ficha
        else:
            print("La casilla ya esta en uso.")
            return False
    elif casilla == 9:
        if matJuego[2][2] == 9:
            matJuego[2][2] = ficha
        else:
            print("La casilla ya esta en uso.")
            return False
                     
    return matJuego

def imprimirJuego(matJuego):

    for e in range(3):
        print("+-----+-----+-----+")
        print(f"|  {matJuego[e][0]}  |  {matJuego[e][1]}  |  {matJuego[e][2]}  |")
        print(f"|     |     |     |")
    print("+-----+-----+-----+")

def validarGanador(matJuego):
#DEVUELVE TRUE SI GANA
        for f in range(len(matJuego)):
            if matJuego[f][0] == matJuego[f][1] and matJuego[f][0] == matJuego[f][2] and matJuego[f][0] != 0 :
                return True
            elif matJuego[0][f] == matJuego[1][f] and matJuego[0][f] == matJuego[2][f] and matJuego[0][f] != 0:
                return True
        if matJuego[0][0] == matJuego[1][1] and matJuego[0][0] == matJuego[2][2] and matJuego[2][0] != 0:
            return True 
        elif matJuego[2][0] == matJuego[1][1] and matJuego[2][0] == matJuego[0][2] and matJuego[2][0] != 0:
            return True 
        return False

def jugar():
    player1 = ingresarJugador("Ingrese el nickname del jugador 1: ")
    player2 = ingresarJugador("Ingrese el nickname del jugador 2: ")
    ficha = []
    jugadores = []
    fichaInicio = input(f"Indique con que ficha quiere jugar {player1} -> X-O: ")
    if fichaInicio == "X" or fichaInicio == "x":
        jugadores.append(player1)
        jugadores.append(player2)
    elif fichaInicio == "O" or fichaInicio == "o":
        jugadores.append(player2)
        jugadores.append(player1)
    ficha.append("x")
    ficha.append("O")
    input(">>>Presione cualquier tecla para iniciar")

    bandera = 0
    for e in range(3):
        print("+-----+-----+-----+")
        print(f"|  {e+1+bandera}  |  {e+2+bandera}  |  {e+3+bandera}  |")
        print(f"|     |     |     |")
        bandera += 2 
    print("+-----+-----+-----+")

    dicJugadores = {player1:{"tiros": 0, "tiempo": 0},player2:{"tiros": 0, "tiempo": 0}}
    dicGanador = {}
    matJuego = crearMatrix()
    tiros = 0
    inicioTime = 0
    finalTIme = 0
    while True:
            orden = 0
            for i in jugadores:
                if tiros < 9:
                    while True:
                        inicioTime = time.time()
                        casilla = int(input(f" {i}. Indique el numero donde quiere jugar: "))
                        finalTIme = time.time()
                        tiempoEjecucion = finalTIme - inicioTime
                        dicJugadores[i]["tiempo"] = tiempoEjecucion 
                        if llenarMatrix(matJuego,casilla,ficha[orden]) == False:
                            continue
                        imprimirJuego(matJuego)
                        orden = 1
                        tiros += 1
                        dicJugadores[i]["tiros"] += 1                        
                        if validarGanador(matJuego) == True:
                            dicJugadores[i]["nombre"] = i
                            print(f"Ha ganado {i}!!! ") 
                            input() 
                            return dicJugadores[i]
                        else:
                            break 
                else:
                    return False                                        

def metodoBurbuja(datosDisco):
    N = len(datosDisco)
    for i in range (0,N-1):
        for j in range (i+1,N):
            if datosDisco[i]["tiros"] > datosDisco[j]["tiros"]:
                t = datosDisco[i]
                datosDisco[i] = datosDisco[j]
                datosDisco[j] = t
            elif datosDisco[i]["tiros"] == datosDisco[j]["tiros"]:
                if datosDisco[i]["tiempo"] > datosDisco[j]["tiempo"]:
                    t = datosDisco[i]
                    datosDisco[i] = datosDisco[j]
                    datosDisco[j] = t

    return(datosDisco)

def cargarGanadores(ganadores):
    
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

def listarGanadores(ganadores):
    print("="*50)
    for i in range(len(ganadores)):
        print(f'Player: {ganadores[i]["nombre"]}  Tiros: {ganadores[i]["tiros"]}  Tiempo: {ganadores[i]["tiempo"]:.3f} seg')
        print("-"*50)    
    print("="*50)
    input()

#PROGRAMA PRINCIPAL
datosDisco = []
primerGanador = []
while True:
    opc = menu()
    if opc == 1:
        ganador = jugar()
        if ganador == False:
            print("EMPATE")
            input()
        else:
            datosDisco = getGanadores()
            if datosDisco == False:
                primerGanador.append(ganador)
                cargarGanadores(primerGanador)
            else:
                datosDisco.append(ganador)
                metodoBurbuja(datosDisco)
                cargarGanadores(datosDisco)
    elif opc == 2:
        datosDisco = getGanadores()
        if datosDisco == False:
            print("No hay ganadores hasta el momento. ")
            input()
        else:
            listarGanadores(datosDisco)
    elif opc == 3:
        break