'''
Modulo Collections - Counter
conhecido como conteiners de alta performace

'''
#importando o counter
from collections import Counter

#podemos usar qualquer iteravel
l1 = [11,1,1,1,2,2,2,2,3,3,3,3,3,4,4,4,4,5,5,5,5,9,9,9,9,9]
#usando o counter, aqui ele vai imprimir a ocorrencia e a quantidade de ocorrencias
r1 = Counter(l1)
print(r1)

print("==============string===================")
print(Counter("abacate"))


print("==============caso 3===================")
txt = """Tem que ter brilho questionador e tonalidade inquietante.
A mim não interessam os bons de espírito nem os maus de hábitos.
Fico com aqueles que fazem de mim louco e santo.
Deles não quero resposta, quero meu avesso.
Que me tragam dúvidas e angústias e agüentem o que há de pior em mim.
Para isso, só sendo louco.
Quero os santos, para que não duvidem das diferenças e peçam perdão pelas injustiças.
Escolho meus amigos pela alma lavada e pela cara exposta.
Não quero só o ombro e o colo, quero também sua maior alegria.
Amigo que não ri junto, não sabe sofrer junto.
Meus amigos são todos assim: metade bobeira, metade seriedade.
Não quero risos previsí"""

p = txt.split()
print(p)
oi = Counter(p)
print(oi)
print("=================")

#encontrando as 5 palavras com mais ocorrencias
print(oi.most_common(5))