#a)
class No:

  def __init__(self, val=0, ant=None, prox=None):
    self.val= val
    self.ant= ant
    self.prox= prox


def atualizar(p, x, y):
  atual= p

  while atual!= None and atual.val!= x:
    atual= atual.prox

  if atual is None:
    return p

  atual.val= y

  if atual.ant!= None:
    atual.ant.prox= atual.prox
  else:
    p= atual.prox  

  if atual.prox!= None:
    atual.prox.ant= atual.ant

  atual.ant= None
  atual.prox= None

  if p is None:
    return atual

  if atual.val < p.val:
    atual.prox= p
    p.ant= atual
    return atual

  aux= p
  while aux.prox!= None and aux.prox.val < atual.val:
    aux= aux.prox

  atual.prox= aux.prox
  atual.ant= aux
  if aux.prox!= None:
    aux.prox.ant= atual
  aux.prox= atual

  return p

n5= No(15)
n4= No(10, prox=n5)
n5.ant= n4

n3= No(9, prox=n4)
n4.ant= n3

n2= No(5, prox=n3)
n3.ant= n2

p= No(3, prox=n2)
n2.ant= p

print("antes")
aux= p
while aux!= None:
  print(aux.val,end=" <-> " if aux.prox else "\n")
  aux= aux.prox

p= atualizar(p, 9, 2)

print("depois")
aux= p
while aux!= None:
  print(aux.val,end=" <-> " if aux.prox else "\n")
  aux= aux.prox


#b)
# complexidade de tempo: O(n) pois no pior caso o algoritmo percorre a lista para 
# encontrar o elemento e realiza outra passagem para colocá-lo na posição correta.
