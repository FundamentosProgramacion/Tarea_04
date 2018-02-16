# Autor: Diana Patricia Aguilar Martínez, A01745778
# Descripcion: Este programa lee los lados de un triangulo y te die que tipo de triángulo es
# A partir de aquí escribe tu programa

def comparacionLados(ladoA, ladoB, base1):
    tipo=""

    if ladoA>0 and ladoB >0 and base1 >0:

        if ladoA==ladoB and ladoB ==base1 and base1==ladoA:
            tipo= "equilatero"

        elif ladoA == ladoB and ladoA!= base1 and ladoB!=base1:
            tipo="isóceles"

        elif ladoA!= ladoB and ladoB!=base1 and ladoA!=base1:
            tipo="escaleno"
    else:
        tipo="Estos datos no corresponden a un triangulo"

    return tipo

def main():
    lado1=int(input("Teclee el valor del lado derecho: "))
    lado2=int(input("Teclee el valor del lado izquierdo: "))
    base= int(input("Teclee el valor de la base: "))
    tipoTriangulo= comparacionLados(lado1, lado2, base )

    print ("Tu triángulo es: ", tipoTriangulo)


main()