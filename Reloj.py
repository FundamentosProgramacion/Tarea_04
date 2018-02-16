#encoding: UTF-8
#Jean Paul Esquivel Lobato
#Hora a las 24

def calcularformato12(hora):
        if hora == 0:
            h = "12"
        elif hora == 1:
            h = "1"
        elif hora == 2:
            h = "2"
        elif hora == 3:
            h = "3"
        elif hora == 4:
            h = "4"
        elif hora == 5:
            h = "5"
        elif hora == 6:
            h = "6"
        elif hora == 7:
            h = "7"
        elif hora == 8:
            h = "8"
        elif hora == 9:
            h = "9"
        elif hora == 10:
            h = "10"
        elif hora == 11:
            h = "11"
        elif hora == 12:
            h = "12"
        elif hora == 13:
            h = "1"
        elif hora == 14:
            h = "2"
        elif hora == 15:
            h = "3"
        elif hora == 16:
            h = "4"
        elif hora == 17:
            h = "5"
        elif hora == 18:
            h = "6"
        elif hora == 19:
            h = "7"
        elif hora == 20:
            h = "8"
        elif hora == 21:
            h = "9"
        elif hora == 22:
            h = "10"
        elif hora == 23:
            h = "11"

        return h


def calcularforDyN(hora):
    if hora >= 0 and hora <=12:
        t = "AM"
    else:
        t = "PM"

    return t

def main():
    hora = int(input("Teclea la hora en horario de 24 hrs. [0,23]: "))
    minutos = int(input("Teclea los minutos: "))
    segundos = int(input("Teclea los segundos: "))

    formato12 = calcularformato12(hora)
    formatoAmPm = calcularforDyN(hora)

    print("En formato de 24hrs. Son las:",hora,":",minutos,":",segundos,"hrs.")
    print("En formato de 12 horas. Son las:", formato12,":",minutos,":",segundos,formatoAmPm)

main()