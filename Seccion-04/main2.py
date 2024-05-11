frase = 'La perseverancia lleva al triunfo en cualquier desafio que enfrentes en la vida'
vocales = 'aAeEiIoOuU'
cantidad_vocales = ''
consonantes = 0
for i in frase:
    if i in vocales:
        cantidad_vocales += i
    else:
        if i != ' ':
            consonantes += 1
print(f"Las vocales encontradas en la frase son: {cantidad_vocales}")
print(f"Las consonantes encontradas en la frase son: {consonantes}")
