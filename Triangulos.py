#Autor: Andrés Reyes Rangel.
#Imprimir que tipo de triangulo es dependiendo su medida.

def calcularTriangulo(ladoA, ladoB, ladoC):
    triangulo = ()
    if ladoA == 0 and ladoB == 0 and ladoC == 0:
        triangulo = "El triangulo no existe"
    elif ladoA==ladoB and ladoB==ladoC:
        triangulo = "El tipo de triangulo es equilatero"
    elif ladoA==ladoB and ladoA!=ladoC or ladoA==ladoC and ladoA!=ladoB or ladoB==ladoC and ladoB!=ladoA:
        triangulo = "El tipo de triangulo es isoceles"
    elif ladoA!=ladoB and ladoB!=ladoC:
        triangulo = "El tipo de triangulo es rectangulo"

    return triangulo


def main():
    ladoA = int(input("Ingresa la primer medida de tu triangulo: "))
    ladoB = int(input("Ingresa la segunda medida de tu triangulo: "))
    ladoC = int(input("Ingresa la tercer medida de tu triangulo: "))

    tipo = calcularTriangulo(ladoA, ladoB, ladoC)

    print(tipo)

main()