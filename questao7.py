v=[9,2,7,7,2,2,1,7,7,9]
cont=0
i=0
j=i+1

while i<9:
    while j<10:
        if v[i]>v[j]:
            cont+=1
        j+=1
    i+=1
    j=i+1
print(cont)