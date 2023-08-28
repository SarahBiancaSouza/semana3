numero = int(input('Diga um número: '))

soma_impares = 0

for n in range(1, numero+1, 1):
    if n % 2 != 0:
        soma_impares += n

print(f"A soma dos números ímpares até {numero} é: {soma_impares}")
