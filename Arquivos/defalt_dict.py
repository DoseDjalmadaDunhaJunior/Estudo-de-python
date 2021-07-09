"""
Modulo Collections - Default Dict

usando o default dict não gera KeyError

lambda são funcioes sem nome que podem ou não receber entradas
"""
from collections import defaultdict

dicionario = defaultdict(lambda: 0)

print(dicionario)
dicionario["nome"] = "jose"
dicionario["idade"] = 23
dicionario["sexo"] = "masculino"

x = input("insira a chave que busca ")
print(dicionario[x])
if dicionario[x] == 0:
    y = input("o que colocar nessa chave? ")
    dicionario[x] = y

print(dicionario)