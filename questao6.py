v=[9,42,21,14,25,3,19,33,45,6]
dif=abs(v[0]-v[1])
for i in range(0,10):
    for j in range(0,10):
        if j==i:
            break
            
        mod=abs(v[i]-v[j])
        if mod<dif:
            dif=mod
print(f"A menor diferença entre os elementos é {dif}")