dicEscuela = {}
bandera = True
while bandera == True:
    dicEstudiantes = {}
    if bandera == True:
        codigo = int(input("Ingrese el codigo del estudiante: "))
        if codigo == 999:
            break
        else:
            dicEstudiantes["Nombre"] = input("Ingrese el nombre del estudiante: ")
            dicEstudiantes["Note1"] = float(input("Ingrese la nota 1 del estudiante [0 - 5.0]"))
            dicEstudiantes["Note2"] = float(input("Ingrese la nota 2 del estudiante [0 - 5.0]"))
            dicEstudiantes["Note3"] = float(input("Ingrese la nota 3 del estudiante [0 - 5.0]"))
        
        dicEscuela[codigo] = dicEstudiantes

#CALCULAR NOTA DEFINITIVA
def calPromedio(nota1,nota2,nota3):
    promedio = (nota1 * 0.3) + (nota2 * 0.3) + (nota3 * 0.4)
    return promedio

#recorrer lista de tuplas 
for c, d in dicEscuela.items():
    nota1 = d["Note1"]  
    nota2 = d["Note2"]
    nota3 = d["Note3"]
    nota = calPromedio(nota1,nota2,nota3)
    if nota >= 3:
        print(f'El estudiante {d["Nombre"]} [{c}] aprobo con una nota de {nota:.2f}')
    else:
        print(f'El estudiante {d["Nombre"]} [{c}] reprobo la materia con una nota de {nota:.2f}')
    

