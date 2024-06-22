program1 = "Técnico en sistemas"
program2 = "Técnico en desarrollo de videojuegos"
program3 = "Técnico en animación digital"
discount1 = "Beca por rendimiento"
discount2 = "Beca cultural"
discount3 = "SIN beca"
costProgram1 = 800000
costProgram2 = 1000000
costProgram3 = 1200000
bandera = True
costMatriculas = 0

while bandera == True:
    codeNumber = input("\nIngrese el codigo del estudiante: ")
    name = input("Ingrese el nombre del estudiante: ")
    programStudent = int(input(f"Ingrese el programa al que perteneces, donde:\n             [1]->{program1}\n             [2]->{program2}\n             [3]->{program3}:\nEl programa es= "))
    discount = int(input(f"Digite del 1 al 3 dependiendo del estudiante, donde:\n             [1]->{discount1}\n             [2]->{discount2}\n             [3]->{discount3}:\nEl programa es= "))
    if programStudent == 1:
        if discount == 1:
            cost2pay = costProgram1/2
            costMatriculas += cost2pay
            print(f"El valor de la matricula de {name} es {cost2pay:,.0f}COP")
        elif discount == 2:
            cost2pay = costProgram1*(1-0.4)
            costMatriculas += cost2pay
            print(f"El valor de la matricula de {name} es {cost2pay:,.0f}COP")
        else:
            cost2pay = costProgram1
            costMatriculas += cost2pay
            print(f"El valor de la matricula de {name} es: ${cost2pay:,.0f}COP")
    if programStudent == 2:
        if discount == 1:
            cost2pay = costProgram2
            costMatriculas += cost2pay
            print(f"El valor de la matricula de {name} es: ${cost2pay:,.0f}COP")
        elif discount == 2:
            cost2pay = costProgram2*(1-0.4)
            costMatriculas += cost2pay
            print(f"El valor de la matricula de {name} es: ${cost2pay:,.0f}COP")
        elif discount == 3:
            cost2pay = costProgram2
            costMatriculas += cost2pay
            print(f"El valor de la matricula de {name} es: ${cost2pay:,.0f}COP")
    if programStudent == 3:
        if discount == 1:
            cost2pay = costProgram3/2
            costMatriculas += cost2pay
            print(f"El valor de la matricula de {name} es: ${cost2pay:,.0f}COP")
        elif discount == 2:
            cost2pay = costProgram3*(1-0.4)
            costMatriculas += cost2pay
            print(f"El valor de la matricula de {name} es: ${cost2pay:,.0f}COP")
        elif discount == 3:
            cost2pay = costProgram3
            costMatriculas += cost2pay
            print(f"El valor de la matricula de {name} es: ${cost2pay:,.0f}COP")
    bandera2 = input("¿Desea continuar? ")
    if bandera2 == "SI" or bandera2 == "si":
            bandera = True
    else:
            bandera = False


