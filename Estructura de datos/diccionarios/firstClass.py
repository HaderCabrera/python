empleado = {"nombre": "Hader Cabrera" , "Cargo": "Programador","Salario": 4000000}
#OBTENER DATO DENTRO DEL DICCIONARIO
print(empleado["Cargo"])
print(empleado.get("Cargo"))

#PONER MENSAJE CUANDO NO EXISTE LLAVE // me devuelve valor
print(empleado.get("Apellido","NO EXITE")) #DEVUELVE NONE POR DEFECTO
#print(empleado("Apellido")) #DEVUELVE ERROR

#AGREGAR LLAVE A DICCIONARIO
empleado["sexo"] = "Masculino"
print(empleado)
    #agregar con set: si no exite la crea, si exite devuelve el 
    #valor original e imprimie para ambos casos
print(empleado.setdefault("Localidad","Bucaramanga"))

#MoODIFICAR SALAROIO
empleado["Salario"] = 4500000
print(empleado)

#BORRAR LLAVE CON SU VALOR
del empleado["sexo"]
print(empleado)

#BORRAR TODO EL DICCIONARIO
#empleado = {}
#empleado.clear()
#del empleado #LA FUNCION DEL BORRA VARIABLE

#COPIAR DICCIONARIO SIN MODIFICAR EL INICIAL
oficina = empleado.copy()
print(oficina)
oficina["salario"] = 5000000
print(oficina)
print(empleado)

#FROMKEYS

#ITEMS: COMBIERTE LLAVE Y VALOR DE LLAVE EN UNA TUPLA DENTRO DE
        #UNA LISTA
print(empleado.items())

#KEYS DEVUELVE LISTADO DE TODAS LAS LLAVES
print(empleado.keys())

#VALUE DEVUELVE LISTADO CON LOS VALORES EL DICCIONARIO
print(empleado.values())

#pop ELIMINA LLAVE Y VALOR DE LLAVE pero devuelve el VALOR
print(empleado.pop("salario"))
#ELIMINAR ULTIMA LLAVE Y VALOR
print(empleado.popitem())