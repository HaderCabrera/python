import random
#SI EL NOMBRE YA ESTA EN DISCO, NO LO DEJA JUGAR
def agregarNombre(msj):
    while True:
        try:
            player = input(msj)
            if player == "" or player.isalnum() == False:
                print("Nombre incorrecto. Digite números y letras.")
                continue
            archivoJugadores = open("hader_cabrera\\talleres\\topTenn.txt","r")
            for line in archivoJugadores:
                linea = line.strip()
                if linea.split(",")[0] == player:
                    print("El jugardor ya existe.")
                    return False
            return player
        except Exception as e:
            print(f"Error. Try again. {e}")

def agregarNumero(msj):      
    while True:
            try:
                intento = int(input(msj))
                if 1 < intento > 1000 :
                    print("Wrong number.[1 - 1000]>>> ")
                    continue
                return intento
            except  ValueError:
                print("Error. Digite un numero correcto.")
#SI ADIVINA DEVUELVE DOS VARIABLES, BANDERA Y EL INTENTO EN QUE LO LOGRO
#SI NO LO LOGRA EN LOS 10 INTENTOS DEVUELVE UN FALSE EN BANDERA
def adivinarNumero(nombre):
    adivinar = random.randint(1, 1000)
    print(adivinar)
    bandera = 0
    for i in range(11,1,-1):
        print(f"____Tienes {i-1} intentos____")
        intento = agregarNumero("Guess the number: ")
        if intento < adivinar:
            print(f"El número {intento} es menor.")
        elif intento > adivinar:
            print(f"el número {intento} es mayor.")
        elif intento == adivinar:
            return True, i
        bandera += 1
    return False, bandera      
#ORDENA LISTA DE JUGADORES GANADORES Y LOS LIMITA A 10
def metodoBurbuja(jugadores):

    players = len(jugadores)
    for i in range(0, players - 1):
        for h in range(i + 1, players):
            if jugadores[i][1] > jugadores[h][1]:
                t  = jugadores[i]
                jugadores[i] = jugadores[h]
                jugadores[h] = t
    if len(jugadores) <= 10:
        return jugadores
    else:
        return jugadores[0:10]
#LEE LOS JUGADORES GANADORES ALMACENADOS EN DISCO
def leerGanadores():
    jugadores = []
    fd = open("hader_cabrera\\talleres\\topTenn.txt","r")
    for line in fd:
        lineas = line.strip()
        jugadores.append(lineas.split(","))  
    return jugadores

def menu():
    print("_"*30)
    print("BIENVENIDO A GUESS_NUMBER")
    print("-"*30)
    print("1. Jugar.")
    print("2. Exit.")
    print("3. Eliminar marcador.")
    print("-"*30)
    while True:
        try:
            opcion = int(input(">>> Que desea realizar? "))
            if 1 < opcion > 3 :
                print("Wrong number.[1 - 3]>>> ")
                continue
            return opcion
        except  ValueError:
            print("Error. Digite un numero correcto.")

#MENU PRINCIPAL
while True:
    opcion = menu()
    if opcion == 1:
        player = agregarNombre("Ingrese el nombre del jugador: ")
        if player != False:
            while True:
                cond, intento = adivinarNumero(player)

                if cond == True:
                    print("\n")
                    print("     HAS ACERTADO, CONGRATULATION!!!\n")

                    againTurno = input(">>> Desea intentar de nuevo? (S/N) ")
                    if againTurno == "S" or againTurno == "s":
                        continue
                    else:
                        print("Gracias por jugar, vuelve pronto!")
                        fd = open("hader_cabrera\\talleres\\topTenn.txt","a")
                        fd.write(player + "," + str(12 - intento) + "\n")
                        fd.close()
                        topp = leerGanadores()
                        top = metodoBurbuja(topp)
                        print("_"*15,"TOP 10","_"*15)    
                        for i in range(0,len(top)):
                            if player == top[i][0]:
                                print("="*40)
                                print(f'Player: {top[i][0]}       Intentos: {top[i][1]}')
                                print("="*40)
                            else:
                                print(f'Player: {top[i][0]}       Intentos: {top[i][1]}')
                        print("_"*40)
                        input()
                        break
                if cond == False:
                    tryAgain = input(">>> YOU LOSS. TRY AGAIN? (S/N) ")
                    if tryAgain == "S" or tryAgain == "s":
                        continue
                    else:
                        print("LOSER, GOODBYE")
                        break
            
    elif opcion == 2:
        print("GRACIAS POR JUGAR, VUELVA PRONTO!")
        break
    
    elif opcion == 3:
        bandera = 0
        while True:
            contraseña = input(" >>Digite la contraseña de admin: ")
            if contraseña == "admin":
                fd = open("talleres\\topTenn.txt","w")
                fd.write("")
                fd.close()
            else:
                print(" Contraseña incorrecta. Try again.")
                bandera += 1
                if bandera >= 3:
                    print("Número de veces maximo. Vuelva luego.".center(35))
                    break
                continue
            
            break
