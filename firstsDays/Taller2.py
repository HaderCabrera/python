imprimir = "*"

#EJERCICIO 1
for x in range(6):
  if x != 3 :
    print("*"*x) 
     

#EJERCICIO 2
print(imprimir*8)
print(imprimir ," "*4, imprimir)
print(imprimir ," "*4, imprimir)
print(imprimir ," "*4, imprimir)
print(imprimir*8)

#EJERCICIO 3
VALORHORA = 20000
horasTRabajadas = int(input("Cuantas horas trabajo el empleado? "))
sueldoBruto = horasTRabajadas * VALORHORA
print("el valor del sueldo bruto es: $ {:,.2f}".format(sueldoBruto))
descuentoEPS = sueldoBruto * 0.04
descuentoPension = sueldoBruto * 0.04
sueldoNeto = sueldoBruto - ( descuentoEPS + descuentoPension )
print("El valor del sueldo neto es: $ {:,.2f}".format(sueldoNeto))

#EJERCICIO 4

SEGUNDOS = int(input("ingrese la cantidad de  segundos :"))
horas = SEGUNDOS // 3600
minutos = (SEGUNDOS - horas*3600) // 60
rest = SEGUNDOS - (horas*3600 + minutos*60)
print(horas,"horas\n",minutos,"minutos\n ",rest,"segundos")

#EJERCICIO 5

NOTA = float(input("Ingrese la nota de 0.0 a 5.0"))
curva = (NOTA * 0.8 ) + 1
print(f"La nueva nota es: {curva:.2f}")
