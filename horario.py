#Autor: Andrés Reyes Rangel
#Cambiar el formato de la hora de 24 hrs a 12hrs.

def calcularHora(hora, minutos, segundos):
    if hora == 24:
        hora12 = 0
    else:
        hora12 = hora - 12
    minutos = minutos
    segundos = segundos
    return hora12, minutos, segundos

def main():
    hora = int(input("Ingresa la hora: "))
    minutos = int(input("Ingresa los minutos: "))
    segundos = int(input("Ingresa los segundos: "))

    formato12hrs = calcularHora(hora, minutos, segundos)

    print("La hora es: %02d:%02d:%02d" % formato12hrs)

main()