# encoding: UTF-8
# Sebastian Morales Martin
# Tarea_04
import getpass
user = getpass.getuser()

def calcularPerimetro(x, y):    #calcula el perimetro de un rectángulo con las dimensiones dadas
    perimetro = (2 * x) + (2 * y)
    return perimetro


def calcularArea(x, y):     # calcula el área de un rectángulo con las dimensiones dadas
    area = x * y
    return area


def definirMayorArea(area1, area2): #define el área mayor por desigualdades
    resultado = ''
    if area1 > area2:
        resultado = 'La primer área es mayor.'
    elif area1 < area2:
        resultado = 'La segunda área es mayor.'
    else:
        resultado = 'Ambas áreas son iguales.'
    return resultado

def main():
    print('Hola %s!!!'% user)

    base1 = int(input('Teclea la base del primer rectángulo: '))
    altura1 = int(input('\nTeclea la altura del primer rectángulo: '))
    base2 = int(input('\nTeclea la base del segundo rectángulo: '))
    altura2 = int(input('\nTeclea la altura del segundo rectángulo: '))

    perimetro1 = calcularPerimetro(base1, altura1)
    perimetro2 = calcularPerimetro(base2, altura2)
    area1 = calcularArea(base1, altura1)
    area2 = calcularArea(base2, altura2)

    areaMayor = definirMayorArea(area1, area2)

    print('\n-Perímetro primer rectángulo: %d'
          '\n-Área primer rectángulo: %d'
          '\n-Perímetro segundo rectángulo: %d'
          '\n-Área segundo rectángulo: %d'
          '\n'
          '\n-%s'
          %(perimetro1, area1, perimetro2, area2, areaMayor))


main()
