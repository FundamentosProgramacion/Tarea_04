#Autor : Karla Fabiola Ramirez Martinez
#Descripcion


def triangulo(l1,l2,l3):
    tipo= " "
    if l1 == l2 and  l1== l3:
        tipo="Equilatero"
    elif l1 ==l2 or l1==l3:
        tipo="Isosceles"
    elif l1 >l2 or l1>l2







def main():
    #Aqui pide los lados
    lado1=int(input("Dame el primer lado: "))
    lado2= int(input("Dame el segundo lado: "))
    lado3= int(input("Dame el tercer lado: "))
    triangulo= calcularTriangulo(lado1,lado2,lado3)

    print triangulo





main()