#a)
class No:

  def __init__(self, val=0, prox=None):
    self.val= val
    self.prox= prox


def particionar(p, k):
  pmenor= None  
  pmaior= None  
  ultmenor= None
  ultmaior= None

  atual= p
  while atual!= None:
    proximo= atual.prox
    atual.prox= None  

    if atual.val<= k:
      if pmenor is None:
        pmenor= atual
        ultmenor= atual
      else:
        ultmenor.prox= atual
        ultmenor= atual
    else:
      if pmaior is None:
        pmaior= atual
        ultmaior= atual
      else:
        ultmaior.prox= atual
        ultmaior= atual

    atual= proximo

  if pmenor is None:
    return pmaior

  ultmenor.prox= pmaior
  return pmenor



n5= No(1)
n4= No(6, n5)
n3= No(5, n4)
n2= No(2, n3)
p= No(9, n2)

k= 5


aux= p
while aux!= None:
  print(aux.val,end=" -> " if aux.prox else "\n")
  aux= aux.prox

p= particionar(p, k)


aux= p
while aux!= None:
  print(aux.val,end=" -> " if aux.prox else "\n")
  aux= aux.prox

#b)
#complexidade de tempo: O(n) pois o algoritmo realiza uma única varredura 
# percorrendo cada elemento uma vez.
