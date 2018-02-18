#encoding UTF-8
# Genaro Ortiz Durán, A01375315
#Descripción:Convertir horas en formato 24 a horas en formato 12.



def main():
    hora=int(input("¿Que hora es:"))
    if hora<12:
        print("La hora es:",hora,"AM")
    else:
        print("La hora es:",hora,"PM")


main()