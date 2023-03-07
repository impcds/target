frase = input('Digite uma frase: ')

saida = ''

for letra in range(1, len(frase) + 1):

    saida += frase[-letra]


print(saida)

