#Aplicar o particiona e a bolha nas 2 partes separadas pelo K
v=[6,5,3,8,9,1,2,10,4,7]
#particiona
k=v[0]
i=1
j=len(v)-1
while i<=j:
    if (v[i]>k and v[j]<k):
        aux=v[i]
        v[i]=v[j]
        v[j]=aux
        i+=1
        j-=1
    elif (v[i]<=k):
        i+=1
    elif (v[j]>=k):
        j-=1
aux=v[0]
v[0]=v[i-1]
v[i-1]=aux
print(v)
#usando o algoritmo da bolha para a primeira parte
fim=j
for i in range(0,fim):
    for i in range(fim):
        if (v[i]>v[i+1]):
            aux=v[i]
            v[i]=v[i+1]
            v[i+1]=aux
print(v)
#usanco o algoritmo da bolha para a segunda parte
for i in range(fim,len(v)-1):
    for i in range(fim,len(v)-1):
        if (v[i]>v[i+1]):
            aux=v[i]
            v[i]=v[i+1]
            v[i+1]=aux
print(v)
