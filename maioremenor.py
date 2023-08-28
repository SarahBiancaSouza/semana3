n = int(input('Diga o número:'))

menor = n  # Começamos com o valor inserido como o menor e o maior número
maior = 0  # Inicializamos o maior como 0

for c in range(0, n + 1, 1):
    print(c)

    if c < menor:
        menor = c

    if c > maior:
        maior = c

print(f'Menor: {menor}')
print(f'Maior: {maior}')
print('Fim')


