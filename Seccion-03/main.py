num1 = int(input("Ingrese un numero -> "))

while num1 > 0:
    if num1 % 1:
        print('El numero es primo')
    else:
        print("El numero no es primo")
    num1 = int(input("Ingrese un numero -> "))
