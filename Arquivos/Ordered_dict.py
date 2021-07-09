"""
Módulo Collections: Ordered Dict

é um dicionario que garante a ordem de incerção dos elementos
"""
from collections import OrderedDict

dict = {"a": 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}

for chave, valor in dict.items():
    print(f'chave={chave}: valor={valor}')

print("=====================================")
dict = OrderedDict({"a": 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5})

for chave, valor in dict.items():
    print(f'chave={chave}: valor={valor}')
