# Autor: Carlos Martínez Rodríguez
# Descripción: Programa que determina el tipo de triágulo dando sus lados

# Función que determina que tipo de triángulo es con base en los lados dados por el usuario
def tipoTriangulo(ladoA, ladoB, ladoC):
    if (ladoA == ladoB and ladoB == ladoC):
        return "Equilátero"
    elif (ladoA == ladoB or ladoA == ladoC or ladoB == ladoC):
        return "Isocéles"
    elif (ladoA != ladoB or ladoB != ladoC or ladoA != ladoC):
        return "Rectánuglo"
    else:
        return "Estos lados no corresponden a un triángulo."

def main():
    # Entradas
    ladoA = int(input("Lado a: "))
    ladoB = int(input("Lado b: "))
    ladoC = int(input("Lado c: "))

    triangulo = tipoTriangulo(ladoA,ladoB,ladoC)

    # Salidas
    print("El triángulo es de tipo: %s" % triangulo)


main()