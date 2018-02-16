#Mirna Fernanda Zertuche Calvillo A01373852
#Convierte la hora de formato de 24horas a 12 horas

def convertirHora(hora):
    if hora == 12:
        return hora
    else:
        hora12= hora-12
        return hora12


def calcularHora(hora, minutos, segundos):
    if hora in range(1,12):
        return ("La hora: %02i:%02i:%02i a.m" % (hora, minutos, segundos))
    elif hora == 00:
        hora= 12
        return ("La hora: %02i:%02i:%02i a.m" % (hora, minutos, segundos))
    else:
        hora12= convertirHora(hora)
        return ("La hora: %02i:%02i:%02i p.m" % (hora12, minutos, segundos))



def main():
    hora= int(input("Hora:"))
    minutos= int(input("Minutos:"))
    segundos= int(input("Segundos:"))
    calculoHora= calcularHora(hora,minutos,segundos)
    print(calculoHora)


main()
