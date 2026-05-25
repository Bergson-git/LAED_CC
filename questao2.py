#Encontrar o segundo maior impar
v=[19,42,21,14,28,3,9,32,46,6]
i=0
while i<10:
    if v[i]%2!=0:
        m=v[i]
        m2=v[i]
        break
    i+=1
i=0
while(i<10):
    if v[i]%2!=0 and v[i]>m:
        m=v[i]
    i+=1
i=0
while i<10:
    if v[i]%2!=0 and v[i]>m2 and v[i]<m:
        m2=v[i]
    i+=1
print(f"o segundo maior impar e {m2}")