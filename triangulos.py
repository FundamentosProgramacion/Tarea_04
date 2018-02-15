#Mirna Fernanda Zertuche Calvillo A01373852
#Determina si es posible un tríangulo con las medidas y si es así qué tipo de triángulo es

def calcularTriangulo(ladoA, ladoB, ladoC):
    if ladoA==ladoB and ladoB==ladoC:
        return "equilátero"
    elif ((ladoA==ladoB)and ladoB!= ladoC) or ((ladoA==ladoC)and ladoC!= ladoB) or ((ladoB==ladoC)and ladoB!= ladoA):
        return "Isóseles"
    else:
        return "Rectángulo"



def main():
    ladoA = float(input("Lado 1 del triángulo: "))
    ladoB = float(input("Lado 2 del triángulo: "))
    ladoC = float(input("Lado 3 del triángulo: "))
    if ladoA<= 0 or ladoB<= 0 or ladoC<= 0:
        print("Estos lados no corresponden a un triángulo")
    else:
        tipoDeTriangulo = calcularTriangulo(ladoA,ladoB,ladoC)
        print("El triángulo es : ", tipoDeTriangulo)

main()