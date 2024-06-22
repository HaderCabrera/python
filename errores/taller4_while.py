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
    while True:
        try:
            codeNumber = input("\nIngrese el codigo del estudiante [1,2,...,n]: ")
            codeNumber = codeNumber.strip()
            if len(codeNumber) == 0 or codeNumber.isdigit == False:
                print("!Formato invalido¡")
                continue
            break
        except ValueError:
            print(f"Error al ingresar codigo de estudiante.")
    while True:
        try:
            name = input("Ingrese el nombre del estudiante: ")
            name = name.strip()
            if len(name) == 0 or name.isalnum() == False:
                print("Formato de nombre invalido")
                continue
            break
        except Exception as e:
            print(f"Error.Nombre invalido.{e}")
    while True:
        try:
            programStudent = input(f"Ingrese el programa al que perteneces, donde:\n             [1]->{program1}\n             [2]->{program2}\n             [3]->{program3}:\nEl programa es= ")
            programStudent = programStudent.strip()
            if len(programStudent) == 0 or programStudent.isdigit == False:
                print("Formato del programa invalido")
                continue
            break
        except ValueError:
            print(f"Error.formato de programa invalido.")
    while True:
        try:
            discount = input(f"Digite del 1 al 3 dependiendo del estudiante, donde:\n             [1]->{discount1}\n             [2]->{discount2}\n             [3]->{discount3}:\nEl programa es= ")
            discount = discount.strip()
            if len(discount) == 0 or discount.isdigit == False:
                print("Formato de beca invalido invalido")
                continue
            break
        except ValueError:
            print(f"Error.formato de beca invalido.")   
        
     |r   if programStudent == 1:
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


