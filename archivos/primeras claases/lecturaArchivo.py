archivo = open("hader_cabrera/archivos/primeras claases/nombres.txt","r")
texto = archivo.read()
#El descriptor queda al final del archivo
print(texto)

#mover descriptor al inicio del archivo
archivo.seek(0)
#tomar una linea 
texto2 = archivo.readline()
print(texto2)

texto3 = archivo.readlines()
print(texto3)
archivo.close