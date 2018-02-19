#Autor: Nataly Paulina Lopez Salazar
#Con los valores de los lados del triangulo se dira que tipo de trianguo es.

def calcularTipo(lado1,lado2,lado3): #Compara los numeros dados por el teclado para dirigir el caso al cual corresponde.
    if lado1==lado2 and lado2==lado3:
         return "Equilatero"

    elif lado1==lado2 and lado2!=lado3:
        return "Isósceles"

    elif lado1!=lado2 and lado2!=lado3 and lado1!=lado3:
        return "Escaleno"
    else:
        return "No existe este triangulo"

def main():
    print("Tipos de triangulos")
    lado1 = int(input("Valor del lado 1: "))
    lado2 = int(input("Valor del lado 2: "))
    lado3 = int(input("Valor del base: "))

    triangulo = calcularTipo(lado1,lado2,lado3)
    print("Tu tipo de triangulo es:",triangulo)

main()