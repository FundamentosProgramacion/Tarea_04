#Autor Karla Fabiola Ramirez Martinez
#Descripcion calcula el precio a pagar


#Funcion que calcula el descuento
def calcularTotal(p):
    #El precio de cada paquete es de $1500
    precio=1500
   #Descuento de 50%
    if p>=100:
        total=(precio*0.5)*p
        return total
    #Descuento de 40%
    elif  p>=50:
        total =(precio*0.6)*p
        return total
    #Descuento de 30%
    elif p>=20:
        total =(precio*0.7)*p
        return total
    #Descuento de 20%
    elif p>=10:
        total =(precio*0.8)*p
        return total
    #Sin descuento
    elif p<10 and p>0:
        total =(precio)*p
        return total
    else:
        total="Error "
        return total



#Funcion principal
def main():
    paquetes=int(input("¿Cuantos paquetes?"))
    total=calcularTotal(paquetes)
    print("El precio total seria: $",total)




main()