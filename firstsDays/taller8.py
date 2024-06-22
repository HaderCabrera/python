
# punto numero 2
def quitarTexto (texto):
    resultado= ""
    for i in texto:
        if i.isdigit():
            resultado += i
    return resultado

datos = 'aaaaaa1.2b2cde110230'
resultado = quitarTexto(datos)
print(resultado)

#punto numero 3 

def calcular_total_con_iva(cantidad_sin_iva, porcentaje_iva):
    iva = cantidad_sin_iva * (porcentaje_iva / 100)
    total = cantidad_sin_iva + iva
    return total

cantidad_sin_iva = 100
porcentaje_iva = 16
total_factura = calcular_total_con_iva(cantidad_sin_iva, porcentaje_iva)
print(f"El total de la factura es: {total_factura}")
