archivo = open("hader_cabrera/archivos/primeras claases/salas.txt","w")
#IMPRIMIR UN CARACTER O UNA CADENA
archivo.write("Sputnik\n")
archivo.write("Apolo\n")
archivo.write("Artemisa\n")
#IMPRIMIR UNA LISTA DE DATOS
archivo.writelines(["houston\n","artemis\n"])
archivo.close()