lanche = (input()).split()
tipo, quant = lanche

tipo = int(tipo)
quan = float(quant)
total = 0.0

#print(float(quant) * 5.00)

if tipo == 1:
    total = float(quant) * 4.00
elif tipo == 2:
    total = float(quant)* 4.50
elif tipo == 3:
    total = float(quant) * 5.00
elif tipo == 4:
    total = float(quant) * (2.00)
elif tipo == 5:
    total = float(quant) * 1.50

print(f'Total: R$ {total:.2f}')
