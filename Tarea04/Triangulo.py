#Carlos Ochoa
#Define el nombre de un triangulo

def main():
    ladoA=int(input("Mide el lado A: "))
    ladoB=int(input("Mide el lado B: "))
    ladoC=int(input("Mide el lado C: "))

    if ladoA==ladoB and ladoA==ladoC and ladoB==ladoC:
        print ("Es un triangulo equilatero")

    elif ladoA==ladoB or ladoA==ladoC or ladoB==ladoC:
        print ("Es un triangulo isoceles")

    elif (ladoA**2+ladoB**2)==ladoC**2:
        print ("Es un triangulo rectangulo")

main()