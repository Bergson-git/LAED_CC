#a)
class No:

  def __init__(self, val=0, prox=None):
    self.val= val
    self.prox= prox

def elementofrequente(p):
  if p is None:
    return None, 0

  contagem= {}
  atual= p

  while atual!= None:
    if atual.val in contagem:
      contagem[atual.val]+= 1
    else:
      contagem[atual.val]= 1
    atual= atual.prox

  frequente= None
  quantmax= 0

  for val,qtd in contagem.items():
    if qtd> quantmax:
      quantmax= qtd
      frequente= val

  return frequente, quantmax

n6= No(3)
n5= No(8, n6)
n4= No(5, n5)
n3= No(8, n4)
n2= No(3, n3)
p= No(8, n2)

aux= p
while aux!= None:
  print(aux.val,end=" -> " if aux.prox else "\n")
  aux= aux.prox

elem, qtd = elementofrequente(p)
print(f"{elem} é o elemento que aparece mais vezes. {qtd} ocorrências")

#b)
#complexidade de tempo: O(n) pois o algoritmo passa de nó em nó para contar a frequência 
# dos elementos
