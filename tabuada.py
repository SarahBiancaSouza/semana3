numero = int(input('Qual número você quer a tabuada?'))

for n in range(1, 11, 1):
    print(n, 'X', numero, '=', n*numero)
print('Fim')