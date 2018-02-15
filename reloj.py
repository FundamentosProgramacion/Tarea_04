#Mirna Fernanda Zertuche Calvillo A01373852
#Convierte la hora de formato de 24horas a 12 horas

def convertirHora(hora):
    if hora == 12:
        return hora
    else:
        hora12= hora-12
        return hora12


def main():
    hora= int(input("Hora:"))
    minutos= int(input("Minutos:"))
    segundos= int(input("Segundos:"))
    if hora in range(1,12):
        print("La hora: %02i:%02i:%02i" % (hora, minutos, segundos),"a.m")
    elif hora == 00:
        hora= 12
        print("La hora: %i:%02i:%02i" % (hora, minutos, segundos),"a.m.")
    else:
        hora12= convertirHora(hora)
        print("La hora: %i:%02i:%02i" % (hora12, minutos, segundos),"p.m")


main()