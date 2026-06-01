v=[6,5,3,8,9,1,2,10,4]
#ordenando os primeiros 2/3 do vetor
k=int(((2/3)*len(v))-1)
for i in range(k):
    for i in range(k):
        if (v[i]>v[i+1]):
            aux=v[i]
            v[i]=v[i+1]
            v[i+1]=aux
print(v)
#ordenando os ultimos 2/3 do vetor
j=int((1/3)*len(v))
for i in range(j,len(v)-1):
    for i in range(j,len(v)-1):
        if (v[i]>v[i+1]):
            aux=v[i]
            v[i]=v[i+1]
            v[i+1]=aux
print(v)
#ordenando os primeiros 2/3 do vetor novamente
for i in range(k):
    for i in range(k):
        if (v[i]>v[i+1]):
            aux=v[i]
            v[i]=v[i+1]
            v[i+1]=aux
print(v)