numero_oculto = 48
cantidad_intentos = 4

adivinar_intento = int(input("Ingrese un numero para adivinar -> "))

while numero_oculto != adivinar_intento and cantidad_intentos > 0:
    print(f"Numero no adivnado. Vuelva a intentarlo. Tienes {cantidad_intentos} intentos restantes")
    adivinar_intento = int(input("Ingrese un numero para adivinar -> "))
    cantidad_intentos -= 1
if numero_oculto == adivinar_intento:
    print(f"Felicidades. Has adivinado el numero {numero_oculto}")
    
else:
    print("Usted a perdido")





















