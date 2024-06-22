matDatos = [
    [ "O", "X", "0"],
    ["0" , "X", "0"],
    ["O" , "O", "X"]
]

bandera = 0
for f in range(len(matDatos)):
    if matDatos[f][0] == matDatos[f][1] and matDatos[f][0] == matDatos[f][2]:
        print("HAY GANADOR")
    if matDatos[0][f] == matDatos[1][f] and matDatos[0][f] == matDatos[2][f]:
        print("HAY GANADOR")       
      