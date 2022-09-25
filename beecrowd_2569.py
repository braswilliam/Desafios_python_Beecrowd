n1,op,n2 = input().split()

n11 = n1.replace('7','0')
n22 = n2.replace('7','0')
if op == '+':
  res = int(n11) + int(n22)
  res2 = str(res).replace('7','0')
  print(int(res2))
else:
  res = int(n11) * int(n22)
  res2 = str(res).replace('7','0')
  print(int(res2))
