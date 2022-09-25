T=int(input())
lista=[]
pj=0
pi=0
while pi <(1000):
    lista.append(pj)
    print('N[{}] = {}'.format(pi, pj))
    if pj<(T - 1):
        pj = pj + 1
    else:
        pj == T - 1
        pj = 0
    pi = pi + 1