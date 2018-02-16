# Autor: Diana Patricia Aguilar Martínez, A01745778
# Descripcion: Convertidor de formato 24hrs a formato 12hrs
# A partir de aquí escribe tu programa


def convertirHora(hora):
    final=""
    if hora > 12 :
        final= hora - 12
    elif hora ==0:
        final= 00
    else:
        final=hora
    return final


def definirStatus(hora):
    if hora > 12 and hora <=23:
        status= "p.m."
    else:
        status="a.m. "
    return status


def main():

    hora=int(input("inserte la hora [0, 23]: "))
    minutos=int(input("inserte los minutos[0, 60]: "))
    segundos=int(input("inserte los segundos [0, 60]: "))

    horaF = convertirHora(hora)
    status =definirStatus(hora)

    print(" tu hora equivale a las: ", horaF, ":",minutos,":", segundos, status )




main()