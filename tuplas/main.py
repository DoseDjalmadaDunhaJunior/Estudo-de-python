# para declarar uma tupla pode ser de duas formas
#tuplas são definidas pelas virgulas e não pelos elementos
t1 = (1,2,3,4,5,6,7,8,9)
# ou
t2 = 1,2,3,4,5,6,7,8,9

# para colocar 1 elemento em uma tupla tem que fazer assim:
t3 = (1,)
t4 = 1,

t5 = tuple(range(10))
t6 = ("bom dia pessoal", "boa tarde pessoal",)
s1, s2 = t6
print(s1)
print(s2)

#metodos para adição e remoção de elementos NÃO existem
#aquelas funcoes sum,max,min e len funcionam

print(sum(t5))
print(max(t5))
print(min(t5))
print(len(t5))

# para contar a quantidade de um elemento

t1 = 'a','b','c','d', 'e','f','b','a','c','b',

print(t1.count('b'))