# Autor: Carlos Martínez Rodríguez
# Descripción: Convertir el sistema horario de 24 horas a formato de 12 horas

# Función que asigna el periodo AM o PM al sistema horario de 12 hrs
def asignarPeriodo(hora):
    if (hora > 12):
        return "PM"
    else:
        return "AM"

# Función que convierte al sistema horario de 24 hrs a 12 hrs tomando como paramentro las horas que da el usuario
def convertirTiempo(hora):
    if (hora > 12):
        h = hora - 12
    elif (hora == 0):
        h = 12
    else:
        h = hora
    return h

# Función Main
def main():
    print("Ingesa el tiempo en formato de 24 hrs")
    hora = int(input("Hora : "))
    min = int(input("Minutos: "))
    seg = int(input("Segundos: "))

    print("La hora en formato 12 hrs es: %.2i:%.2i:%.2i %s" % (convertirTiempo(hora), min, seg, asignarPeriodo(hora)))

main()