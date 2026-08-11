#a)
class No:

  def __init__(self, val=0, prox=None):
    self.val= val
    self.prox= prox


def separar(p):
  p1= None 
  p2= None  
  ultimp= None
  ultpar= None

  atual= p
  while atual!= None:
    proximo= atual.prox
    atual.prox= None  

    if atual.val%2!= 0: 
      if p1 is None:
        p1= atual
        ultimp= atual
      else:
        ultimp.prox= atual
        ultimp= atual
    else: 
      if p2 is None:
        p2= atual
        ultpar= atual
      else:
        ultpar.prox= atual
        ultpar= atual

    atual= proximo

  return p1, p2

n5= No(7)
n4= No(10, n5)
n3= No(5, n4)
n2= No(8, n3)
p= No(2, n2)

aux= p
while aux!= None:
  print(aux.val,end=" -> " if aux.prox else "\n")
  aux= aux.prox

p1,p2= separar(p)

print("impares")
aux= p1
while aux!= None:
  print(aux.val,end=" -> " if aux.prox else "\n")
  aux= aux.prox

print("pares")
aux= p2
while aux!= None:
  print(aux.val,end=" -> " if aux.prox else "\n")
  aux = aux.prox

#b)
#complexidade de tempo: O(n), pois o algoritmo percorre os n elementos da lista apenas uma vez.
