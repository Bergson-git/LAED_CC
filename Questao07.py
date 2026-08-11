#a)
class No:

  def __init__(self, val=0, prox=None):
    self.val = val
    self.prox = prox

def remover_copias(p, k):
  
  while p != None and p.val == k:
    p = p.prox

  if p is None:
    return None
  
  atual = p
  while atual.prox != None:
    if atual.prox.val == k:
      atual.prox = atual.prox.prox 
    else:
      atual = atual.prox 

  return p

#criando a lista: 1 -> 3 -> 3 -> 2 -> 3 -> 2
n6 = No(2)
n5 = No(3, n6)
n4 = No(2, n5)
n3 = No(3, n4)
n2 = No(3, n3)
p = No(1, n2)

k = 3
aux = p
while aux != None:
  print(aux.val, end=" -> " if aux.prox else "\n")
  aux = aux.prox

p = remover_copias(p, k)

aux = p
while aux != None:
  print(aux.val, end=" -> " if aux.prox else "\n")
  aux = aux.prox

#b)
#complexidade de tempo: O(n) pois o algoritmo percorre a lista apenas uma vez.
#complexidade de espaço: O(1) (in-place) pois altera apenas os ponteiros dos nós existentes.