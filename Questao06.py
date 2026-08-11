#a)
class No:

  def __init__(self, val=0, prox=None):
    self.val = val
    self.prox = prox


def particionar(p, k):
  p_menor = None  
  p_maior = None  
  ult_menor = None
  ult_maior = None

  atual = p
  while atual != None:
    proximo = atual.prox
    atual.prox = None  

    if atual.val <= k:
      if p_menor is None:
        p_menor = atual
        ult_menor = atual
      else:
        ult_menor.prox = atual
        ult_menor = atual
    else:
      if p_maior is None:
        p_maior = atual
        ult_maior = atual
      else:
        ult_maior.prox = atual
        ult_maior = atual

    atual = proximo

  if p_menor is None:
    return p_maior

  ult_menor.prox = p_maior
  return p_menor



#lista: 9 -> 2 -> 5 -> 6 -> 1
n5 = No(1)
n4 = No(6, n5)
n3 = No(5, n4)
n2 = No(2, n3)
p = No(9, n2)

k = 5


aux = p
while aux != None:
  print(aux.val, end=" -> " if aux.prox else "\n")
  aux = aux.prox

p = particionar(p, k)


aux = p
while aux != None:
  print(aux.val, end=" -> " if aux.prox else "\n")
  aux = aux.prox

#b)
#complexidade de tempo: O(n) pois o algoritmo realiza uma única varredura 
# percorrendo cada elemento uma vez.
#complexidade de espaço: O(1) (in-place), pois apenas reorganiza as conexões dos ponteiros existentes sem alocar memória para novos nós.