#Mirna Fernanda Zertuche Calvillo A01373852
#Programa que calcula el área y perímetro de dos rectagulos y determina cual es el mayor o si son iguales.

def calcularArea(ladoA, ladoB):
    area = ladoA * ladoB
    return area


def calcularPeri(ladoA, ladoB):
    perimetro = ladoA * 2 + ladoB * 2
    return perimetro


def compararR(areaR1, areaR2):
    if areaR1 == areaR2:
        return "Las áreas son iguales"
    elif areaR1> areaR2:
        return  "El primer rectangulo tiene  mayor área"
    else:
        return "El segundo rectángulo tiene mayor área"


def main():
    ladoA = float(input("Base del rectángulo primero: "))
    ladoB = float(input("Áltura del rectángulo priemro: "))
    ladoC = float(input("Base del rectángulo segundo: "))
    ladoD = float(input("Altura del rectángulo segundo: "))
    #Para no hacer muy largo el nombre de la variable usare "R" como sustituto de Rectángulo
    areaR1 = calcularArea(ladoA,ladoB)
    areaR2 = calcularArea(ladoC, ladoD)
    perimetroR1 = calcularPeri(ladoA,ladoB)
    perimetroR2 = calcularPeri(ladoC,ladoD)
    comparación = compararR(areaR1,areaR2)
    print("El área y perimetro del rectángulo primero es: Área: %.2f"%areaR1, "Perímetro: %.2f"%perimetroR1)
    print("El área y perimetro del rectángulo segundo es: Área: %.2f"%areaR2, "Perímetro: %.2f"%perimetroR2)
    print(comparación)

main()