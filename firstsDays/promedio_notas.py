#capturar las notas de un curso y calcular el promedio de estas.

cant = int(input("cantidad de notas: "))
sumaNotas = 0
for i in range(1, cant+1):
    nota = float(input(f"Ingrese la nota #{i}"))
    sumaNotas = sumaNotas + nota # sumaNOtas + = nota

prom = sumaNotas / cant

print(f"el promedio del curso es {prom:.2f}")