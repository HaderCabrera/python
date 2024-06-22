def prepararCafe(insumo1, insumo2):
    salida = ""
    if insumo1.lower() == "cafe" and insumo2.lower() == "agua":
        salida = "tinto"
    else:
        salida = "Daño la cafetera"
    return salida

#USO DE LA FUNCION
taza = prepararCafe("cafe","agua")
print(taza)
