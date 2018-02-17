# encoding: UTF-8
# Sebastian Morales Martin
# Tarea_04
import getpass
user = getpass.getuser()


def calcularHora12(cantidad):
    if cantidad >12:
        hora12 = cantidad -12
    elif cantidad == 0:
        hora12 = 12
    else:
        return cantidad
    return hora12


def determinarAMPM(cantidad):
    AMPM = ''
    if cantidad == 0:
        AMPM = 'AM'
    elif cantidad <12:
        AMPM = 'AM'
    else:
        AMPM = 'PM'
    return AMPM


def main():
    print('Hola %s!!!' % user)
    hora24 = int(input('Teclea la hora: '))
    minuto = int(input('Teclea los minutos: '))
    segundo = int(input('Teclea los segundos'))

    hora12 = calcularHora12(hora24)
    AMPM = determinarAMPM(hora24)
    print('Las %d:%d:%d en formato 24 horas son las %d:%d:%d %s en 12 horas'% (hora24, minuto, segundo, hora12, minuto, segundo, AMPM))


main()
