# 2) Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores 
# (exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número,
#  ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# IMPORTANTE:

# Esse número pode ser informado através de qualquer entrada de sua preferência ou pode ser previamente definido no código;

def fibo():
    '''Pede um número inteiro e verifica se o mesmo faz parte da sequência de Fibonacci.'''

    num = int(input('Digite um número inteiro: '))


    # Há dois locais que podem retornar sim, então coloquei dentro dessa váriavel..
    pertence = f'O número {num} pertence a sequência de Fibonacci.'

    a, b = 0, 1

    if num == 0 or num == 1:
        return pertence
    
    while b < num:
        c = a + b
        a, b = b, c

        if c == num:
            return pertence
        
    return f'O número {num} não pertence a sequência de Fibonacci.'


print(fibo())

