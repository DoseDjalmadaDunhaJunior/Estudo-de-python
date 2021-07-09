"""
Deque
é uma lista de alta performace

"""

from collections import deque

#criando deques

deq = deque("josé djama")
print(deq)

# adicionando elementos no deque
deq.append('@')
print(deq)
deq.remove('@')
print(deq)
deq.pop()
print(deq)
deq.append('a')
print(deq)