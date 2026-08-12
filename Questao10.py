#a)
class No:

  def __init__(self, val=0, ant=None, prox=None):
    self.val= val
    self.ant= ant
    self.prox= prox

def encontrarsublista(L, x):
  idx= 0
  while idx < len(L) - 1 and L[idx + 1]!= None and x >= L[idx + 1].val:
    idx+= 1
  return idx

def busca(L, x):
  if not L:
    return False

  idx= encontrarsublista(L, x)
  atual= L[idx]

  while atual!= None and atual.val<= x:
    if atual.val== x:
      return True
    atual= atual.prox

  return False

def insercao(L, x):
  if not L:
    return L

  idx= encontrarsublista(L, x)
  novo= No(x)

  if L[idx] is None:
    L[idx]= novo
    return L

  atual= L[idx]

  if x< atual.val:
    novo.prox= atual
    atual.ant= novo
    L[idx]= novo
    return L

  while atual.prox!= None and atual.prox.val< x:
    atual= atual.prox

  novo.prox= atual.prox
  novo.ant= atual
  if atual.prox!= None:
    atual.prox.ant= novo
  atual.prox= novo

  return L

def remocao(L, x):
  if not L:
    return L

  idx= encontrarsublista(L, x)
  atual= L[idx]

  while atual!= None and atual.val!= x:
    atual= atual.prox

  if atual!= None:
    if atual.ant!= None:
      atual.ant.prox= atual.prox
    else:
      L[idx]= atual.prox

    if atual.prox!= None:
      atual.prox.ant= atual.ant

  return L

l0_n2= No(9)
l0_n1= No(2, prox=l0_n2)
l0_n2.ant= l0_n1

l1_n2= No(19)
l1_n1= No(15, prox=l1_n2)
l1_n2.ant= l1_n1

l2_n2= No(49)
l2_n1= No(31, prox=l2_n2)
l2_n2.ant= l2_n1

L= [l0_n1, l1_n1, l2_n1]

def imprimir_L(L):
  for i, sublista in enumerate(L):
    print(f"L[{i}] -> ",end="")
    aux= sublista
    if aux is None:
      print("vazia")
    while aux!= None:
      print(aux.val, end=" <-> " if aux.prox else "\n")
      aux= aux.prox


print("antes")
imprimir_L(L)

print("testando a busca")
print("Busca(L, 19):", busca(L, 19))
print("Busca(L, 25):", busca(L, 25))

print("teste da inserção")
L= insercao(L, 17)
imprimir_L(L)

print("teste da remoção")
L= remocao(L, 15)
imprimir_L(L)


#b)
# Considerando 'k' como o número de sublistas e 'm' como o número médio 
# de elementos em cada sublista:
# 1) Busca(L, x): O(k + n/k) no pior caso usando busca linear no vetor L 
# 2) Inserção(L, x): O(k + n/k) para localizar a sublista correta e encontrar o ponto de 
#    inserção dentro da sublista encadeada.
# 3) Remoção(L, x): O(k + n/k) para localizar a sublista e o elemento a ser removido.
