sueldo = 1_100_000
sueldoMInimo = 1_160_000

if sueldo <= sueldoMInimo:
    auxTrans = 140_000
else:
    auxTrans = 0

print(f"AUxilio de transporte ${auxTrans:,}")

#EJERCICIO DE CONDICIONES}

nombre = input("NOmbre del estudiante")
nota = int(input("ingrese nota del estudiante [0 - 100]"))

if nota >= 0 and nota <= 59 :
    notaCual = "D"
elif nota >= 60 and nota <= 79 :
    notaCual = "C"
elif nota >= 80 and nota <= 89 :
    notaCual = "B"
elif nota >= 90 and nota <= 100 :
    notaCual = "A"

else:
    notaCual = "Nota no valida"


print

