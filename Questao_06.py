#Verificar se as listas U e V sao permutações uma da outra
u=[1,2,3,4,5,6,7,8,9,10]
v=[7,2,3,1,6,5,9,10,4,8]
cont=0
for i in u:
    for j in v:
        if i==j:
            cont+=1
            break
if cont==len(v):#poderia ser len(u) também
    print("Sao permutações")
else:
    print("Nao sao permutações")

