n = int(input("Ingrese un número-> "))

contador = 0
numero = 2

while contador < n:
    num_primo = True
    for i in range(2, numero):
        if numero % i == 0:
            num_primo = False
            break
    if num_primo:
        print(numero)
        contador += 1
    numero += 1



    
