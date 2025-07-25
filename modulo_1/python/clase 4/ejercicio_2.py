palabra = "banana"
contador = {}
for letra in palabra:
    contador[letra] = contador.get(letra, 0) + 1
print(contador)