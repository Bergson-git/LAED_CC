#a)
class No:

  def __init__(self, val=0, prox=None):
    self.val = val
    self.prox = prox

def elemento_mais_frequente(p):
  if p is None:
    return None, 0

  contagem = {}
  atual = p

  while atual != None:
    if atual.val in contagem:
      contagem[atual.val] += 1
    else:
      contagem[atual.val] = 1
    atual = atual.prox

  mais_frequente = None
  max_qtd = 0

  for val, qtd in contagem.items():
    if qtd > max_qtd:
      max_qtd = qtd
      mais_frequente = val

  return mais_frequente, max_qtd

#criando a lista: 8 -> 3 -> 8 -> 5 -> 8 -> 3
n6 = No(3)
n5 = No(8, n6)
n4 = No(5, n5)
n3 = No(8, n4)
n2 = No(3, n3)
p = No(8, n2)

aux = p
while aux != None:
  print(aux.val, end=" -> " if aux.prox else "\n")
  aux = aux.prox

elem, qtd = elemento_mais_frequente(p)
print(f"{elem} é o elemento que aparece mais vezes, com {qtd} ocorrências")

#b)
#complexidade de tempo: O(n) pois o algoritmo passa de nó em nó para contar a frequência 
# dos elementos
#complexidade de espaço: O(u), onde u é o número de elementos únicos na lista, para armazenar as contagens no dicionário.