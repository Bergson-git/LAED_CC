#a)
class No:
  
  def __init__(self, val=0, ant=None, prox=None):
    self.val= val
    self.ant= ant
    self.prox= prox

def elementocentral(p):
  if p is None:
    return None

  q1= p
  q2= p
  
  while q2.prox!= None and q2.prox.prox!= None:
    q1= q1.prox
    q2= q2.prox.prox

  return q1.val

n5= No(8)
n4= No(2, prox=n5)
n5.ant= n4

n3= No(5, prox=n4)
n4.ant= n3

n2= No(9, prox=n3)
n3.ant= n2

p= No(3, prox=n2)
n2.ant= p

aux= p
while aux!= None:
  print(aux.val,end=" <-> " if aux.prox else "\n")
  aux= aux.prox

central= elementocentral(p)
print("Elemento central:", central)

#b)
#complexidade de tempo: O(n) pois o algoritmo faz uma única passagem pela lista
