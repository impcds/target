# 3) Descubra a lógica e complete o próximo elemento:

# a) 1, 3, 5, 7, ___

# b) 2, 4, 8, 16, 32, 64, ____

# c) 0, 1, 4, 9, 16, 25, 36, ____

# d) 4, 16, 36, 64, ____

# e) 1, 1, 2, 3, 5, 8, ____

# f) 2,10, 12, 16, 17, 18, 19, ____

def letra_a(x):
    '''Printa x numeros impares'''
    elemento = 1
    for i in range(x):
        print(elemento, end=', ' if i < x-1 else '\n')
        elemento += 2

    # print()

letra_a(5)

def letra_b(x):
    '''Printa uma sequência de x números, sendo cada número o dobro do seu antecessor.'''
    elemento = 2
    for i in range(x):
        print(elemento, end=', ' if i < x - 1 else '\n')
        
        elemento *= 2

letra_b(7)

def letra_c(x):
    '''Printa uma sequência de x números, pulando uma quantidade igual de números pares e impares,
    começando em 0 par e impar e incrementando em 1 a cada número exibido.'''
    pular = 0
    elemento = 0
    for i in range(x):
        print(elemento, end=', ' if i < x - 1 else '\n')
        if pular < 1:
            pular += 1
        else:
            pular += 2
        
        elemento += pular
    
letra_c(8)

def letra_d(x):
    '''Printa uma sequência de x números pares elevados ao quadrado'''
    base = 2
    for i in range(x):
        print(base ** 2, end=', ' if i < x - 1 else '\n')
        base += 2


letra_d(5)

def letra_e(x):
    '''Cada novo número é a soma dos dois anteriores, conhecido também como sequência de Fibonacci.'''
    a, b, c = 0, 1, 1

    for i in range(x):
        print(c, end=', ' if i < x - 1 else '\n')
        c = a + b
        a, b = b, c

letra_e(10)

def letra_f():
    '''Não encontrei a lógica naquela sequência'''
    print('Não consegui solucionar esta sequência.')

letra_f()

