import random
jugadores = {}

def agregarNombre(msj):
    while True:
        try:
            player = input(msj)
            if player == "" or player.isalnum() == False:
                print("Nombre incorrecto. Digite números y letras.")
                continue
            return player
        except Exception as e:
            print(f"Error. Try again.")

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

def adivinarNumero(nombre):
    player = {}
    adivinar = random.randint(1, 1000)
    print(adivinar)
    for i in range(11,1,-1):
        print(f"____Tienes {i-1} intentos____")
        intento = agregarNumero("Guess the number: ")
        if intento < adivinar:
            print(f"El número {intento} es menor.")
        elif intento > adivinar:
            print(f"el número {intento} es mayor.")
        elif intento == adivinar:
            player["intento"] = 12 - i
            jugadores[nombre] = player
            return True
    return False       

def metodoBurbuja(jugadores):
    lstPLayers = list(jugadores.items())
    players = len(lstPLayers)
    for i in range(0, players - 1):
        for h in range(i + 1, players):
            if lstPLayers[i][1]["intento"] > lstPLayers[h][1]["intento"]:
                t  = lstPLayers[i]
                lstPLayers[i] = lstPLayers[h]
                lstPLayers[h] = t
    return lstPLayers

def menu():
    print("_"*30)
    print("BIENVENIDO A GUESS_NUMBER")
    print("-"*30)
    print("1. Jugar.")
    print("2. Exit.")
    print("-"*30)
    while True:
        try:
            opcion = int(input(">>> Que desea realizar? "))
            if 1 < opcion > 2 :
                print("Wrong number.[1 - 2]>>> ")
                continue
            return opcion
        except  ValueError:
            print("Error. Digite un numero correcto.")

#MENU PRINCIPAL
while True:
    opcion = menu()
    if opcion == 1:
        player = agregarNombre("Ingrese el nombre del jugador: ")
        while True:
            cond = adivinarNumero(player)
            top = metodoBurbuja(jugadores)
            if cond == True:
                print("\n")
                print("     HAS ACERTADO, CONGRATULATION!!!\n")
                print("_"*15,"TOP 10","_"*15)
                for i in range(0,len(top)):
                    if player == top[i][0]:
                        print("="*40)
                        print(f'Player: {top[i][0]}       Intentos: {top[i][1]["intento"]}')
                        print("="*40)
                    else:
                        print(f'Player: {top[i][0]}       Intentos: {top[i][1]["intento"]}')
                print("_"*40)

                againTurno = input(">>> Desea intentar de nuevo? (S/N) ")
                if againTurno == "S" or againTurno == "s":
                    continue
                else:
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
