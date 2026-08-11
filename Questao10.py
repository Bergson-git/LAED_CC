#a)
class No:

  def __init__(self, val=0, prox=None):
    self.val = val
    self.prox = prox


def intersecao(p1, p2):
  elementos_p2 = set()
  atual = p2
  while atual != None:
    elementos_p2.add(atual.val)
    atual = atual.prox

  p3 = None
  ult = None
  vistos = set()

  atual = p1
  while atual != None:
    if atual.val in elementos_p2 and atual.val not in vistos:
      vistos.add(atual.val)
      novo = No(atual.val)

      if p3 is None:
        p3 = novo
        ult = novo
      else:
        ult.prox = novo
        ult = novo

    atual = atual.prox

  return p3

#lista p1: 3 -> 9 -> 2 -> 6 -> 4
a5 = No(4)
a4 = No(6, a5)
a3 = No(2, a4)
a2 = No(9, a3)
p1 = No(3, a2)

#lista p2: 4 -> 5 -> 2 -> 9 -> 3
b5 = No(3)
b4 = No(9, b5)
b3 = No(2, b4)
b2 = No(5, b3)
p2 = No(4, b2)

#p1
print("p1:", end=" ")
aux = p1
while aux != None:
  print(aux.val, end=" -> " if aux.prox else "\n")
  aux = aux.prox

#p2
print("p2:", end=" ")
aux = p2
while aux != None:
  print(aux.val, end=" -> " if aux.prox else "\n")
  aux = aux.prox


p = intersecao(p1, p2)

#resultado
print("p: ", end=" ")
aux = p
while aux != None:
  print(aux.val, end=" -> " if aux.prox else "\n")
  aux = aux.prox

#b)
#complexidade de tempo: O(n + m), onde n é o número de nós de p1 e m é o número de nós de p2
#complexidade de espaço: O(m + k), onde m é o espaço ocupado pelo conjunto de elementos 
# de p2 e k é o número de nós criados na nova lista resultante.