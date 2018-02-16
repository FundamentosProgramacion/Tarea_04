#encoding: UTF-8
#Jean Paul Esquivel Lobato
#Existe el triangulo

def calcularTriangulo(ladoA, ladoB, ladoC):
    if ladoA <= 0 or ladoB <= 0 or ladoC <= 0:
        triangulo = "Estados lados no corresponden a un triángulo"
    else:
        if ladoA == ladoB and ladoB == ladoC:
            triangulo = "equilátero"
        elif ((ladoA==ladoB)and ladoB!= ladoC) or ((ladoA==ladoC)and ladoC!= ladoB) or ((ladoB==ladoC)and ladoB!= ladoA):
            triangulo = "Isóseles"
        else:
            triangulo = "Rectángulo"

    return triangulo

def main():
    ladoA = float(input("Teclea el lado a: "))
    ladoB = float(input("Teclea el lado b: "))
    ladoC = float(input("Teclea el lado c: "))

    triangulo = calcularTriangulo(ladoA,ladoB,ladoC)

    print("El triángulo es : ", triangulo)

main()