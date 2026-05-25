#Verificar se existem dois elementos repetidos
#que se encontram distantes no maximo k um do outro
v=[2,1,9,7,6,3,9,4,2,6,1,3]
k=int(input())
i=0
while i<len(v):
    j=i+1
    while j<len(v):
        if v[i]==v[j] and j-i==k:
            print(f"Sim o {v[i]} (nas posicoes {i+1} e {j+1})")
        j+=1
    i+=1 