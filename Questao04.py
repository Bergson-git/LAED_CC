#a)
class No:

  def __init__(self, val=0, prox=None):
    self.val= val
    self.prox= prox

def duplicarimpares(p):
  atual= p

  while atual!= None:
    if atual.val%2!= 0: 
      novo= No(atual.val, atual.prox)  
      atual.prox= novo 
      atual= novo.prox  
    else:
      atual= atual.prox  

  return p

n4= No(3)
n3= No(6, n4)
n2= No(7, n3)
p= No(2, n2)

aux= p
while aux!= None:
  print(aux.val,end=" -> " if aux.prox else "\n")
  aux= aux.prox

p= duplicarimpares(p)

aux= p
while aux!= None:
  print(aux.val,end=" -> " if aux.prox else "\n")
  aux= aux.prox

#b)
#complexidade de tempo: O(n) pois o algoritmo passa por cada nó da lista apenas uma vez.
