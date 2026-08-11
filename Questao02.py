#a)
class No:

  def __init__(self, val=0, prox=None):
    self.val = val
    self.prox = prox


def separar(p):
  p1 = None 
  p2 = None  
  ult_imp = None
  ult_par = None

  atual = p
  while atual != None:
    proximo = atual.prox
    atual.prox = None  

    if atual.val % 2 != 0: 
      if p1 is None:
        p1 = atual
        ult_imp = atual
      else:
        ult_imp.prox = atual
        ult_imp = atual
    else: 
      if p2 is None:
        p2 = atual
        ult_par = atual
      else:
        ult_par.prox = atual
        ult_par = atual

    atual = proximo

  return p1, p2



#criando a lista 2 -> 8 -> 5 -> 10 -> 7
n5 = No(7)
n4 = No(10, n5)
n3 = No(5, n4)
n2 = No(8, n3)
p = No(2, n2)

aux = p
while aux != None:
  print(aux.val, end=" -> " if aux.prox else "\n")
  aux = aux.prox

p1, p2 = separar(p)

# ímpares
aux = p1
while aux != None:
  print(aux.val, end=" -> " if aux.prox else "\n")
  aux = aux.prox

# pares
aux = p2
while aux != None:
  print(aux.val, end=" -> " if aux.prox else "\n")
  aux = aux.prox

# b)
# Complexidade de tempo: O(n), pois o algoritmo percorre os n elementos da lista apenas uma vez.
# Complexidade de espaço: O(1) (in-place), pois a separação é feita apenas alterando os ponteiros já existentes, sem criar novos nós.