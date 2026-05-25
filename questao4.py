#Verificar se existe algum numero ımpar
#que aparece um numero ımpar de vezes na lista
v=[9,2,7,7,2,2,1,7,7,9]
i=0
k=0
cont=0
print("Sim, o ",end="")
while i<len(v):
    while k<len(v):
        if v[i]==v[k] and v[i]%2!=0:
            cont+=1
        k+=1
    if cont%2!=0 and v[i]%2!=0:
        print(f"{v[i]} ",end="")
    i+=1
    cont=0
    k=0
