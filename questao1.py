v=[ 9, 42, 21, 14, 28, 3, 19, 32 ,46, 6]
i=0
while i<10:
    if (v[i]%2!=0):
        m=v[i]
        break
    i+=1
while i<10:
    if (v[i]%2!=0 and v[i]>m):
        m=v[i]
        break
    i+=1
print(f"O maior numero impar e {m}")