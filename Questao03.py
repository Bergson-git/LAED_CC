#a)
class No:

  def __init__(self, val=0, ant=None, prox=None):
    self.val= val
    self.ant= ant
    self.prox= prox

def trocar(p, a, b):
  ant= a.ant
  prox= b.prox

  if ant!= None:
    ant.prox= b
  else:
    p= b 
  if prox!= None:
    prox.ant= a

  b.ant= ant
  b.prox= a
  a.ant= b
  a.prox= prox

  return p


def varredura(p):
  if p is None or p.prox is None:
    return p

  atual= p
  while atual!= None and atual.prox!= None:
    if atual.val > atual.prox.val:
      p= trocar(p, atual, atual.prox)
    else:
      atual= atual.prox

  return p

n5= No(1)
n4= No(5, prox=n5)
n5.ant= n4

n3= No(8, prox=n4)
n4.ant= n3

n2= No(3, prox=n3)
n3.ant= n2

p= No(9, prox=n2)
n2.ant= p


print("antes")
aux= p
while aux!= None:
  print(aux.val,end=" <-> " if aux.prox else "\n")
  aux= aux.prox

p= varredura(p)

print("depois")
aux= p
while aux!= None:
  print(aux.val,end=" <-> " if aux.prox else "\n")
  aux= aux.prox


#b)
# complexidade de tempo: O(n) pois o algoritmo realiza uma varredura percorrendo 
# os n elementos da lista 
