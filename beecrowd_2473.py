user = input().split()
sort = input().split()
result = ['azar', 'azar', 'azar', 'terno', 'quadra', 'quina', 'sena']
print(result[len(list(set(user).intersection(sort)))])


