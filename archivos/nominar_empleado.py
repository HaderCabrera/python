fd = open("hader_cabrera/archivos/datos_empleado.dat","r")

listEmpleados = []
listEmpleado = []
for empleado in fd:
    if not empleado.startswith("ID"):
        listEmpleado = empleado.split(",")
        print(f"ID = {listEmpleado[0]}")
        print(f"NOMBRE = {listEmpleado[1]}")
        print(f"EDAD = {listEmpleado[2]}")
        print(f"SEXO = {listEmpleado[3]}")
        print(f"TELEFONO = {listEmpleado[4]}")
        print("-------------------------")
    # listEmpleados.append(listEmpleado)
        print(listEmpleado)
        input()
fd.close()
# for i in range(1,len(listEmpleado)):
#     print(f"ID = {listEmpleados[0]}")
#     print(f"NOMBRE = {listEmpleados[1]}")
#     print(f"EDAD = {listEmpleados[2]}")
#     print(f"SEXO = {listEmpleados[3]}")
#     print(f"TELEFONO = {listEmpleados[4]}")
#     print("-------------------------")

