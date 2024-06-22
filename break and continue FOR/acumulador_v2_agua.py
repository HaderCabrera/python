#ITERACION O CICLO CONTROLADO POR CANTIDAD

n = int(input("\ncuantos ususarios?"))
totalConsumo = 0
for i in range(1,n+1):
    print(f"datos del usuario #{i}")
    cod = input("COdigo?")
    nom = input("Nombre")
    est = input("Estado [V: vigente o S: suspendido]")
    estr = int(input("Estrato?"))
    consumo = float(input("Comsumo [cm**3]"))

    if est == "V" or est == "v":
        if estr == 1:
            tbas = 10000
        elif estr == 2:
            tbas = 20000
        elif estr== 3:
            tbas = 30000
        elif estr == 4:
            tbas = 45000
        elif estr == 5:
            tbas = 60000
        elif estr == 6:
            tbas = 70000
        else:
            tbas = 0
        
        #calcular valor de consumo
        valCons = consumo * 200
        #calcular valor a pagar
        calpagar = tbas + valCons
        #VALOR TOTAL A PAGAR DE TODOS LOS USUARIOS
        totalConsumo += calpagar

        #imprimir el informe del usuario

        print("\n","=" * 40)
        print("\tNOmbre: ",nom)
        print(f"\tValor tarifa basica: {tbas:,}")
        print(f"\tValor consumo: ${valCons:,}")
        print(f"\tValor de la factura de agua: ${calpagar:,.0f}")
    
#IMPRIMIR VALOR TOTAL A PAGAR ADE TODOS LOS USUARIO
print("\n","=" * 40)
print(f"El valor total a pagar es {totalConsumo:,.0f}")

