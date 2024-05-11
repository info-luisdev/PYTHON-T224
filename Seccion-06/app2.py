def numeros_amigos(num1, num2):
    suma1 = sum(i for i in range(1, num1) if num1 % i == 0)
    suma2 = sum(i for i in range(1, num2) if num2 % i == 0)
    return suma1 == num2 and suma2 == num1

num1 = int(input("Ingrese el primer número -> "))
num2 = int(input("Ingrese el segundo número -> "))

if numeros_amigos(num1, num2):
    print(f"{num1} y {num2} son números amigos.")
else:
    print(f"{num1} y {num2} no son números amigos.")
