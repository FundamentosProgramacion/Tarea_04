# encoding: UTF-8
# Sebastian Morales Martin
# Tarea_04
import getpass
user = getpass.getuser()
def calcularDescuento(cantidad):
    MENSAJE = ''
    if cantidad < 10:
        precio = 1500 * cantidad
        mensaje = ('-TOTAL: %10.2f'% precio)
    elif cantidad >=10 and cantidad < 20:
        descuento = (cantidad * 1500) * 0.20
        precio = (cantidad * 1500) - descuento
        mensaje = ('-DESCUENTO 20 POR CIENTO!!\n-CANTIDAD DESCONTADA: %10.2f\n-TOTAL: %10.2f' % (descuento, precio))
    elif cantidad >=20 and cantidad < 50:
        descuento = (cantidad * 1500) * 0.30
        precio = (cantidad * 1500) - descuento
        mensaje = ('-DESCUENTO 30 POR CIENTO!!\n-CANTIDAD DESCONTADA: %10.2f\n-TOTAL: %10.2f' % (descuento, precio))
    elif cantidad >=50 and cantidad < 100:
        descuento = (cantidad * 1500) * 0.40
        precio = (cantidad * 1500) - descuento
        mensaje = ('-DESCUENTO 40 POR CIENTO!!\n-CANTIDAD DESCONTADA: %10.2f\n-TOTAL: %10.2f' % (descuento, precio))
    elif cantidad >=100:
        descuento = (cantidad * 1500) * 0.50
        precio = (cantidad * 1500) - descuento
        mensaje = ('-DESCUENTO 50 POR CIENTO!!\n-CANTIDAD DESCONTADA: %10.2f\n-TOTAL: %10.2f' % (descuento, precio))
    return mensaje


def main():
    print('Hola %s!!!\n' % user)
    paquetes = int(input('Teclea la cantidad de paquetes que desea comprar: '))
    if paquetes < 0:
        print('ERROR')
    else:
        print(calcularDescuento(paquetes))



main()