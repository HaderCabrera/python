a = input("Igrese una cadena de caracteres [a-z]")
b = a.lower()
cont = 0
sizeCadena = len(b)

while cont < sizeCadena -1 :
    
        if b[cont] == b[cont+1]:
            b = b.replace(b[cont],"",1)
            print(b)
            b = b.replace(b[cont],"",1)
            print(b)
            sizeCadena = len(b)
            if cont != 0:
                cont -= 1
        else:
            cont += 1
        if b == "":
             print("CADENA VACIA")
    
        
    


