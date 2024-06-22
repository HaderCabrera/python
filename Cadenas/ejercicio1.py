num = input("ingrese nnumero")

if num.startswith("+") and num.count("-") == 2:
    partes = num.split("-")
    print("EL telefono es:",partes[1])
else:
    print("Error.el formato no cumple con el formato")