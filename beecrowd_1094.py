numeros = int(input())
corlhos = 0
ratos = 0
sapos = 0

for i in range(1, numeros + 1):
    entrada = input().split()
    a, b, = entrada
    if b == 'C':
        corlhos = corlhos + int(a)
    if b == 'R':
        ratos = ratos + int(a)
    if b == 'S':
        sapos = sapos + int(a)

total = corlhos + ratos + sapos
p_coelhos = (corlhos / total) * 100
p_ratos = (ratos / total) * 100
p_sapos = (sapos / total) * 100

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {corlhos}')
print(f'Total de ratos: {ratos}')
print(f'Total de sapos: {sapos}')
print(f'Percentual de coelhos: {p_coelhos:.2f} %')
print(f'Percentual de ratos: {p_ratos:.2f} %')
print(f'Percentual de sapos: {p_sapos:.2f} %')
