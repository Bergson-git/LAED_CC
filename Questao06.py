#a)
class No:

  def __init__(self, val=0, pos=0, ant=None, prox=None):
    self.val= val
    self.pos= pos
    self.ant= ant
    self.prox= prox

def buscaindice(p, k):
  atual= p
  while atual!= None:
    if atual.pos== k:
      return atual.val
    atual= atual.prox
  return 0

def buscavalor(p, x):
  atual= p
  while atual!= None:
    if atual.val== x:
      return atual.pos
    atual= atual.prox
  return -1

def atualizacao(p, x, k):
  atual= p

  while atual!= None and atual.pos< k:
    atual= atual.prox

  if atual!= None and atual.pos== k:
    if x!= 0:
      atual.val= x
    else:
      if atual.ant!= None:
        atual.ant.prox= atual.prox
      else:
        p= atual.prox

      if atual.prox!= None:
        atual.prox.ant= atual.ant

  elif x!= 0:
    novo= No(val=x, pos=k)

    if p is None or k< p.pos:
      novo.prox= p
      if p!= None:
        p.ant= novo
      p= novo
    else:
      aux= p
      while aux.prox!= None and aux.prox.pos< k:
        aux= aux.prox

      novo.prox= aux.prox
      novo.ant= aux
      if aux.prox!= None:
        aux.prox.ant= novo
      aux.prox= novo

  return p

n5= No(9, 17)
n4= No(1, 12, prox=n5)
n5.ant= n4

n3= No(10, 9, prox=n4)
n4.ant= n3

n2= No(5, 7, prox=n3)
n3.ant= n2

p= No(4, 3, prox=n2)
n2.ant= p

print("valor na posicao 9:", buscaindice(p, 9))
print("valor na posicao 5 (nao explicitada):", buscaindice(p, 5))

print("Posicao do valor 10:", buscavalor(p, 10))
print("Posicao do valor 99 (nao existe):", buscavalor(p, 99))

print("\nLista antes :")
aux= p
while aux!= None:
  print(f"[{aux.val} | {aux.pos}]", end=" <-> " if aux.prox else "\n")
  aux= aux.prox

p= atualizacao(p, 15, 9)  
p= atualizacao(p, 8, 5)   

print("\nLista depois")
aux= p
while aux!= None:
  print(f"[{aux.val} | {aux.pos}]", end=" <-> " if aux.prox else "\n")
  aux= aux.prox


#b)
# Considerando 'm' como o numero de elementos nao nulos armazenados na lista encadeada:
# 1) Buscaindice: O(m) no pior caso, pois necessita percorrer a lista encadeada ate encontrar 
# a posicao k.
# 2) Buscavalor: O(m) no pior caso, pois necessita percorrer os nós ate encontrar o valor x.
# 3) Atualizacao: O(m) no pior caso, pois precisa fazer a busca linear pela posicao 
# k para atualizar, inserir ou remover um nó.

