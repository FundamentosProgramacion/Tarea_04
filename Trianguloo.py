#Autor: Ricardo Cornejo
#Regresa tipo de triangulo de acuerdo con datos de los lados.

def lados(a,b, c):
    if a**2+b**2 == c**2 or b**2 == c**2-a**2 or a**2 == c**2-b**2:
        return "Triangulo Rectangulo"
    elif a==b and c==a and b==c:
        return "Triangulo Equilatero"
    elif a==b and c!=a or b==c and a!=b:
        return "Triangulo Isoloceles"
    else:
        return "Estos lados no corresponden a un trianuglo"

def main():
    LadoA=int(input("Teclea el valor del lado A: "))
    LadoB=int(input("Teclea el valor del lado B: "))
    LadoC=int(input("Teclea el valor del lado C: "))
    resultado = lados(LadoA,LadoB,LadoC)
    return resultado

main()