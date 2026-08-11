#a)
class No:

  def __init__(self, val=0, prox=None):
    self.val = val
    self.prox = prox

def intercalar(p1, p2):

  if p1 is None:
    return p2
  if p2 is None:
    return p1

  if p1.val < p2.val:
    p = p1
    p1 = p1.prox
  else:
    p = p2
    p2 = p2.prox

  ult = p 

  while p1 != None and p2 != None:
    if p1.val < p2.val:
      ult.prox = p1
      p1 = p1.prox
    else:
      ult.prox = p2
      p2 = p2.prox
    ult = ult.prox
 
  if p1 != None:
    ult.prox = p1
  else:
    ult.prox = p2

  return p

#lista p1: 3 -> 6 -> 7 -> 10 -> 13
a5 = No(13)
a4 = No(10, a5)
a3 = No(7, a4)
a2 = No(6, a3)
p1 = No(3, a2)

#lista p2: 2 -> 4 -> 9 -> 11 -> 12
b5 = No(12)
b4 = No(11, b5)
b3 = No(9, b4)
b2 = No(4, b3)
p2 = No(2, b2)

print("p1:", end=" ")
aux = p1
while aux != None:
  print(aux.val, end=" -> " if aux.prox else "\n")
  aux = aux.prox

print("p2:", end=" ")
aux = p2
while aux != None:
  print(aux.val, end=" -> " if aux.prox else "\n")
  aux = aux.prox

p = intercalar(p1, p2)

print("p: ", end=" ")
aux = p
while aux != None:
  print(aux.val, end=" -> " if aux.prox else "\n")
  aux = aux.prox

#b)
#complexidade de tempo: O(n + m), onde n e m são os tamanhos das listas p1 e p2. 
#complexidade de espaço: O(1) (in-place), pois reutiliza os nós 
# originais apenas alterando os ponteiros, sem criar novos nós.