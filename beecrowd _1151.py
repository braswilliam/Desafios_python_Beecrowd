entrada = int(input())
index = 0
lista = []
while index < entrada:
    if index == 0 or index == 1:
        lista.append(index)

    if index > 1:
        x = lista[index - 2] + lista[index - 1]

        lista.append(x)
    index = index + 1
for j in range(0, entrada):
    lista[j] = str(lista[j])

lista = ' '.join(lista)
print(lista)
