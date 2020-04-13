sw = True
def ingreso():
    global a,b
    a=float(input("Ingrese el primer número:\n"))
    b=float(input("Ingrese el segundo número\n"))
def suma():
    print('El resultado es: ', a+b)
def resta():
    print('El resultado es: ', a-b)
def multiplicacion():
    print('EL resultado es: ', a*b)
def division():
    if (b == 0):
        print('NO se puede dividir entre 0')
    else:
        print('El resutado es: ', a/b)

while sw:
    print("1. Suma")
    print("2. Resta")
    print("3. Multipicacion")
    print("4. Division")
    print("5. Cerrar Calculadora")
    opcion=int(input("Ingrese una opcion:\n"))
    if(opcion==1):
        ingreso()
        suma()

    elif(opcion==2):
        ingreso()
        resta()

    elif(opcion==3):
        ingreso()
        multiplicacion()

    elif(opcion==4):
        ingreso()
        division()
    elif(opcion==5):
        sw=False