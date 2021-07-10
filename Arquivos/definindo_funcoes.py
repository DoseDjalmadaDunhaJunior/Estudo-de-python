"""
Definindo Funções
 pequenos trechos de codigos que realizam farefas especificas
"""

#exemplo de utilização de função


#cores = ['verde', 'amarelo', 'azul', 'branco', 'vermelho']

from random import random

def soma(a,b):
    print(f"vou somar {a} + {b}:")
    return a+b

def divide(a,b):
    print(f"a divisão de {a} com {b} é:")
    return a/b

def multipica(a,b):
    print(f"a multiplicação de {a} por {b} é:")
    return a*b

def subtracao(a,b):
    print(f"a subtração de {a} por {b} é:")
    return a-b

def joga():
    # gera um valor entre 0 e 1
    valor = random()
    if(valor > 0.5):
        return "Cara"
    return "Coroa"

s = soma
d = divide
m = multipica
sub = subtracao
for n in range(10):
    print("========================")
    print(soma(n,n+1))
    print(divide(n,n+1))
    print(multipica(n,n+1))
    print(subtracao(n,n+1))
    print(joga())


print("=============TAMBEM DA CERTO==========")
for n in range(10):
    print("========================")
    print(s(n,n+1))
    print(d(n,n+1))
    print(m(n,n+1))
    print(sub(n,n+1))
    print(joga())



