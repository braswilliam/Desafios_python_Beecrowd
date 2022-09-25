vezes, tamanho = map(int, input().split())
titas = []

for i in range(vezes):
    tita_final = ''
    entrada = input().split()
    entrada[-1] = int(entrada[-1])

    if entrada[-1] > tamanho:
        for idex in entrada[0:-1]:
            tita_final += idex + " "
        print(tita_final.strip())