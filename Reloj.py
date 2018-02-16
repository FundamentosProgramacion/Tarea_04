# Jossian Abimelec García Quijano
#convierte el horario de un formato de 24 a 12


def Calcularhora(hora, minuto, segundo):
    if hora==0:
        return 12
    elif hora>12:
        hora=hora-12
        return hora
    else:
        return hora
def main():
    hora=int(input("Teclea la hora en formato de 24 horas"))
    minuto = int(input("Teclea los minutos"))
    segundo = int(input("Teclea los segundos"))
    reloj=Calcularhora(hora, minuto, segundo)
    if hora>=12:
        print (reloj,":",minuto,":",segundo,"PM")
    else:
        print(reloj, ":", minuto, ":", segundo, "AM")


main()