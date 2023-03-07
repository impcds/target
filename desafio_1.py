# Observe o trecho de código abaixo:

# int INDICE = 13, SOMA = 0, K = 0;

# enquanto K < INDICE faça

# {

# K = K + 1;

# SOMA = SOMA + K;

# }

# imprimir(SOMA);

# Ao final do processamento, qual será o valor da variável SOMA?

indice = 13
soma = 0

for i in range(indice):
    soma += i

print(soma)
