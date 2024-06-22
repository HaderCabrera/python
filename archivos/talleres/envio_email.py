fd = open("hader_cabrera/archivos/mbox-short.txt","r")
fdCorreos = open("hader_cabrera/archivos/correosEnviados.txt","w")


correos = set()

for linea in fd:
    if linea.startswith("From:"):
        email = (linea.split()[1])
        correos.add(email)
        sorted(correos, reverse=True)
for email in correos:
    mensaje = (f"{email} enviado [ok]")

    print (mensaje)
    fdCorreos.write(mensaje+"\n")
fd.close()
fdCorreos.close()