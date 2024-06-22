fd = open("hader_cabrera/archivos/primeras claases/nombres.txt","r")

fd2 = open("hader_cabrera/archivos/primeras claases/nombres_bak.txt","w")

for linea in fd:
    #print(linea, end="") # barre el documento linea por linea
    fd2.write(linea)

fd2.close()
fd.close()

print("Procreso terminado")