#buscar elementos en una lista y devolver, si lo encuenta
# devuelve la posicion, de lo contrario -1

def indez(lista,elemento):
    for i in range(len(lista)):
        if lista[i] == elemento:
            return i
    return -1

#buscar un elemento en una lista, si lo encuentra
#devuelve TRUE de lo contrario FALSE

def indezz(lista,elemento):
    for i in lista:
        if i == elemento:
            return True
    return False

Nombres = ["Hader","Yobany","Cabrera","Guarin"]
buscar = "Cabrera"
print(f"El elemento {buscar} esta en la posicion: {indezz(Nombres,buscar)}")