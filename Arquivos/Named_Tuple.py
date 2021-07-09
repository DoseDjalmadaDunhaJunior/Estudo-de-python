"""
Named Tuple
são tuplas nomeadas
"""

from collections import namedtuple

#precisamos definir nome e parametros

#forma 1 - declaração

dog = namedtuple('dog', 'idade raça nome')

#forma 2 - declaração

dog = namedtuple('dog', 'idade, raça, nome')

#forma 3 - declaração

dog = namedtuple('dog', ['idade', 'raça', 'nome'])


#usando
ray = dog(idade=2, raça='lulu', nome='amy')
print(ray)
print(ray.idade) #idade
print(ray[1]) #raça
print(ray[2]) #nome