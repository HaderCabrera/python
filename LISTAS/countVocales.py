letras = []
while True:
    letra = input("Ingrese una letra alfabetica: ")
    if letra.isalpha() == True:
        letras.append(letra)
    else:
        print("Letra invalida\n")
        continue
    bandera = input("Desea continudad? [s/n]>>>> ")
    if bandera.lower() != "s":
        break

vocales = ["a","e","i","o","u"]
contVocales = [0]*5
for i in letras:
    if i in vocales:
        posicion = vocales.index(i) 
        contVocales[posicion] += 1
# imprimir cantidad vocales
for a in range(len(vocales)):
    print(f" {vocales[a]} == {contVocales[a]}")