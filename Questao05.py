#a)
class No:

  def __init__(self, val=0, pos=0, ant=None, prox=None):
    self.val= val
    self.pos= pos
    self.ant= ant
    self.prox= prox


def construiresparso(V):
  p= None
  ultimo= None

  for i in range(len(V)):
    if V[i]!= 0:
      novo= No(V[i], i + 1) 

      if p is None:
        p= novo
        ultimo= novo
      else:
        ultimo.prox= novo
        novo.ant= ultimo
        ultimo= novo

  return p

V= [0, 3, 0, 0, 0, 5, 0, 2, 0, 0, 8, 0, 0, 7, 0]

print(V)

p= construiresparso(V)

print("Lista encadeada")
aux= p
while aux!= None:
  print(f"[{aux.val} | {aux.pos}]", end=" <-> " if aux.prox else "\n")
  aux= aux.prox

#b)
# complexidade de tempo: O(n) onde n é o tamanho total do vetor V
