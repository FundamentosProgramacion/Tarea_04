#Ricardo Cornejo
#Convierte formato de 24hrs a formato de 12hrs

def Conversion(hrs,min,seg):
    if hrs >= 13:
        return (hrs - 12)
    else:
        return hrs
def main ():
    horas = int(input("Teclea hora: "))
    minutos = int(input("Teclea minutos: "))
    segundos = int(input("Teclea segundos:" ))
    tiempoFinal = Conversion(horas, minutos, segundos)
    if horas >= 13:
        print ("Son las "  +str(tiempoFinal),":"+str(minutos),":"+str(segundos), "p.m.")
    else:
        print ("Son las:" + str(tiempoFinal), ":"+ str(minutos), ":"+ str(segundos), "a.m.")


main()