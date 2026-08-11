#a)
class No:

  def __init__(self, val=0, prox=None):
    self.val = val
    self.prox = prox


def tem_repetido(p):
  vistos = set()
  atual = p

  while atual != None:
    if atual.val in vistos:
      return True 
    vistos.add(atual.val)
    atual = atual.prox

  return False 

# Criando a lista: 2 -> 9 -> 7 -> 4 -> 1
n5 = No(1)
n4 = No(4, n5)
n3 = No(7, n4)
n2 = No(9, n3)
p = No(2, n2)

aux = p
while aux != None:
  print(aux.val, end=" -> " if aux.prox else "\n")
  aux = aux.prox


if tem_repetido(p):
  print("Sim")
else:
  print("Não")

#b)
#complexidade de tempo: O(n) pois o algoritmo percorre a lista no máximo uma vez 
# e as operações no conjunto (set) têm tempo médio O(1).
#complexidade de espaço: O(u), onde u é a quantidade de elementos únicos armazenados no conjunto