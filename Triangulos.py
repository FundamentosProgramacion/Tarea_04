#Autor : Karla Fabiola Ramirez Martinez
#Descripcion Te dice que tipo de triangulo es

#Al parecer no tenia la libreria math asi que de momento ultilizare **0.5
#Esta sera la funcion que nos dira que triangulo es
def calcularTriangulo(l1,l2,l3):
    #La variable tipo ira cambiando segun se cumplan o no las condiciones
    tipo= "Esto no es un triangulo"
    #if para saber si es un triangulo equilatero
    if l1 == l2 and  l1== l3:
        tipo="Equilatero"
        return tipo
    #if para saber si es un triangulo isosceles
    elif l1 ==l2 or l1==l3:
        tipo="Isosceles"
        return tipo
    #Ifs para saber si es un triangulo rectangulo
    elif l1 >l2 and l1>l3 :
        if l1==((l2**2+l3**2)**0.5):
            tipo = "Rectangulo"
            return tipo
    elif l2>l3 and l2>l1:
        if l2==((l1 ** 2+l3 ** 2)**0.5):
            tipo = "Rectangulo"
            return tipo
    elif l3>l2 and l3>l1:
        if (l3)==((l2**2+l1 ** 2)**0.5):
            tipo = "Rectangulo"
            return tipo
        #si no se cumple ninguna de las condiciones anteriores regresara el valor de tipo original
        else:
            return tipo



#Funcion principal
def main():
    #Aqui pide los lados
    lado1=float(input("Dame el primer lado: "))
    lado2= float(input("Dame el segundo lado: "))
    lado3= float(input("Dame el tercer lado: "))
    triangulo= calcularTriangulo(lado1,lado2,lado3)

    print (triangulo)





main()