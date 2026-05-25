#Este codigo responde a questao 02, que pede para encontrar késimo maior elemento.
#Ela também responde a 01, que pede para encontrar o terceiro maior. Basta digitar 3 
v=[9,42,21,14,25,3,19,33,45,6]
k=int(input())
i=0
j=0
while i<k:
    m=v[i]
    while j<len(v):
        if v[j]>=m:
            m=v[j]
            posM=j
        j+=1
    aux=v[i]
    v[i]=m
    v[posM]=aux
    i+=1
    j=i
print(m)