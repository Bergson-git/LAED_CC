#a)
class No:

  def __init__(self, val=0, prox=None):
    self.val = val
    self.prox = prox

def inverter(p):
  ant = None
  atual = p

  while atual != None:
    prox_no = atual.prox  
    atual.prox = ant 
    ant = atual  
    atual = prox_no 

  return ant 

#criando a lista 3 -> 2 -> 5 -> 9 -> 4
n5 = No(4)
n4 = No(9, n5)
n3 = No(5, n4)
n2 = No(2, n3)
p = No(3, n2)

aux = p
while aux != None:
  print(aux.val, end=" -> " if aux.prox else "\n")
  aux = aux.prox

p = inverter(p)

aux = p
while aux != None:
  print(aux.val, end=" -> " if aux.prox else "\n")
  aux = aux.prox

#b)
#Complexidade de tempo: O(n), pois o algoritmo percorre os n nós da lista encadeada apenas uma vez.
#Complexidade de espaço: O(1) (in-place), pois altera apenas as 
#conexões de ponteiros existentes usando variáveis auxiliares simples, sem alocar nova memória.