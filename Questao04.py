#a)
class No:

  def __init__(self, val=0, ant=None, prox=None):
    self.val= val
    self.ant= ant
    self.prox= prox

def particionar(p, k):
  if p is None:
    return p

  q= p
  r= p
  while r.prox!= None:
    r= r.prox

  while q!= None and r!= None and q!= r and q.ant!= r:
    while q!= None and q!= r and q.ant!= r and q.val<= k:
      q= q.prox

    while r!= None and q!= r and q.ant!= r and r.val> k:
      r= r.ant

    if q!= None and r!= None and q!= r and q.ant!= r:
      q.val, r.val= r.val, q.val

  return p

n5= No(13)
n4= No(17, prox=n5)
n5.ant= n4

n3= No(9, prox=n4)
n4.ant= n3

n2= No(5, prox=n3)
n3.ant= n2

p= No(12, prox=n2)
n2.ant= p

k= 10

print("antes")
aux= p
while aux!= None:
  print(aux.val, end=" <-> " if aux.prox else "\n")
  aux= aux.prox

p= particionar(p, k)

print("depois")
aux= p
while aux!= None:
  print(aux.val, end=" <-> " if aux.prox else "\n")
  aux= aux.prox

#b)
# complexidade de tempo: O(n) pois os ponteiros q e r caminham em sentidos opostos 
# até se encontrarem
