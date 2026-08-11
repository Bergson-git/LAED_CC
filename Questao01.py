#a)
class No:

  def __init__(self, val=0, prox=None):
    self.val = val
    self.prox = prox

def maior_no_fim(p):
  if p is None or p.prox is None:
    return p

  maior = p
  ant_maior = None

  atual = p
  ant = None

  while atual != None:
    if atual.val > maior.val:
      maior = atual
      ant_maior = ant
    ant = atual
    atual = atual.prox

  ult = ant 

  if maior == ult:
    return p

  if maior == p:
    p = p.prox
  else:
    ant_maior.prox = maior.prox


  ult.prox = maior
  maior.prox = None

  return p

#testando
#criando a lista 5 -> 8 -> 13 -> 2 -> 10
n5 = No(10)
n4 = No(2, n5)
n3 = No(13, n4)
n2 = No(8, n3)
p = No(5, n2)

aux = p
while aux != None:
  print(aux.val, end=" -> " if aux.prox else "\n")
  aux = aux.prox

p = maior_no_fim(p)

aux = p
while aux != None:
  print(aux.val, end=" -> " if aux.prox else "\n")
  aux = aux.prox

#b)
#complexidade de tempo: O(n) pois o algoritmo percorre os n elementos uma vez para pegar o maior e 
#colocar no final
#complexidade de espaço:O(1) pois é um algoritmo in-place.