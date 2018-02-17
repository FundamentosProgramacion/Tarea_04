# encoding: UTF-8
# Sebastian Morales Martin
# Tarea_04
import getpass
user = getpass.getuser()
def definirTriangulo(a, b, c):                  #busca el tipo de triangulo y define primero si el triangulo existe para empezar
    reply = ''
    if a == 0 or b == 0 or c == 0:
        reply = "Estos lados no corresponden a un triángulo"
    elif a!=b and b==c or b!=c and a==c or b!=c and a==b:
        reply = 'Isósceles'
    elif a!=b and a!= c and b != c:
        reply = 'Escaleno'
    elif a == b and a == c:
        reply = 'Equilatero'
    return reply

def main():
    print('Hola %s!!!' % user)
    lado1 = int(input('Teclea A: '))
    lado2 = int(input('Teclea B: '))
    lado3 = int(input('Teclea C: '))
    triangle = definirTriangulo(lado1, lado2, lado3)
    print('El triangulo es %s' % triangle)

main()