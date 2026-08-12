#a)
class No:

  def __init__(self, val=0, ant=None, prox=None):
    self.val= val
    self.ant= ant
    self.prox= prox


def transformarlistaDelistas(p, k):
  if p is None or k<= 0:
    return []

  n= 0
  atual= p
  while atual!= None:
    n+= 1
    atual= atual.prox

  tbase= n// k
  resto= n% k

  L= []
  atual= p

  for i in range(k):
    if atual is None:
      break

    L.append(atual) 

    tatual= tbase + (1 if i < resto else 0)

    for _ in range(tatual - 1):
      if atual.prox!= None:
        atual= atual.prox

    proximo_inicio= atual.prox
    atual.prox= None
    if proximo_inicio!= None:
      proximo_inicio.ant= None

    atual= proximo_inicio

  return L

valores= [1, 3, 7, 10, 13, 18, 21, 27]
p= None
ultimo= None

for v in valores:
  novo= No(v)
  if p is None:
    p= novo
    ultimo= novo
  else:
    ultimo.prox= novo
    novo.ant= ultimo
    ultimo= novo

k= 4 

print("Lista:")
aux= p
while aux!= None:
  print(aux.val, end=" <-> " if aux.prox else "\n")
  aux= aux.prox

L= transformarlistaDelistas(p, k)

print("\nLista de listas:")
for i, sublista in enumerate(L):
  print(f"L[{i}] -> ",end="")
  aux= sublista
  while aux!= None:
    print(aux.val,end=" <-> " if aux.prox else "\n")
    aux= aux.prox


#b)
# complexidade de tempo: O(n) onde n é o número total de nós da lista original
