
def crearMatrix(m,n):
  matrix = []
  for i in range(m):
    fila = [0] * n
    matrix.append(fila)
  return matrix

def llenarMatrix(matrix):
  contador = 1
  for f in range(len(matrix)):
    for c in range(len(matrix[f])):
      matrix[f][c] = contador
      contador += 1  

def imprimirMatrix(matrix):
  for f in range(len(matrix)):
    for c in range(len(matrix[f])):
      print(matrix[f][c], end=" ")
    print()

def menu(smj):
  print("_"*40)
  print("PATRONES DE MATRICES M*N DONDE M = N".center(40))
  print("_"*40)
  print("1. PATRON 1\t\t2. PATRON 2")
  print("3. PATRON 3\t\t4. PATRON 4")
  print("5. PATRON 5\t\t6. PATRON 6")
  print("7. PATRON 7\t\t8. PATRON 8")
  print("9. Cambiar tamaño de matrix.".center(40))
  print("      10. Salir.")
  print("_"*40)
  op = int(input(smj))
  return op

filas = int(input(">>> Ingrese numero de filas: "))
matrix = crearMatrix(filas,filas)

while True:
    op = menu(">>> Elija una opc: ")
    if op == 1:
        contador = 1
        for f in range(len(matrix)):
            for c in range(len(matrix[f])):
                matrix[f][c] = contador
                contador += 1
        imprimirMatrix(matrix)
        input()
    elif op == 2:
        numeros = []
        bandera = 0
        for k in range(1,filas+1):
            numeros.append(k)
        for f in range(len(matrix)):
            if bandera == 0:
                for c in range(len(matrix[f])):
                    matrix[f][c] = numeros[c]
                    bandera = 1
            else:
                rev = numeros[::-1]
                for c in range(len(matrix[f])):
                    matrix[f][c] = rev[c]
                    bandera = 0
        imprimirMatrix(matrix)
        input()
    elif op == 3:
        for f in range(len(matrix)):
            for c in range(len(matrix)):
                if f == c:
                    matrix[f][c] = 1
                else:
                    matrix[f][c] = 0
        imprimirMatrix(matrix)
        input()
    elif op == 4:
        bandera = 0
        for f in range(len(matrix)):
            for c in range(len(matrix[f])):
                if c == (len(matrix) - 1) - bandera:
                    matrix[f][c] = 1
                    bandera += 1
                else:
                   matrix[f][c] = 0
        imprimirMatrix(matrix)
        input()
    elif op == 5:
        for f in range(len(matrix)):
            for c in range(len(matrix[f])):
                if f >= c:
                    matrix[f][c] = 1
                else:
                    matrix[f][c] = 0
        imprimirMatrix(matrix)
        input()
    elif op == 6:
        for f in range(len(matrix)):
            for c in range(len(matrix[f])):
                if f <= c:
                    matrix[f][c] = 1
                else:
                    matrix[f][c] = 0
        imprimirMatrix(matrix)
        input()
    elif op == 7:
        contador = 1
        for c in range(len(matrix[1])):
            for f in range(len(matrix)):     
                matrix[f][c] = contador
                contador += 1
        imprimirMatrix(matrix)
        input()
    elif op == 8:
        for c in range(len(matrix[1])):
            factor = (-1 )** c
            for f in range(len(matrix)):
                if c <= f:
                    if factor == 1:     
                        matrix[f][c] = "A"
                    else:
                        matrix[f][c] = "B"
                else:
                    matrix[f][c] = ""
        
        imprimirMatrix(matrix)
        input()
    elif op == 9:
        filas = int(input("Ingrese numero de filas:  "))
        matrix = crearMatrix(filas,filas)
    elif op == 10:
       break