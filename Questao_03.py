#Encontrar o elemento mais proximo da media da lista de numeros
v=[5,3,1,10,2,13,9,12,4,7]
soma=0
for i in v:
    soma+=i
media=soma/(len(v))
base=abs(v[0]-media)
for i in v:
    distancia=abs(i-media)
    if distancia<base:
        base=distancia
        elemento=i
print(elemento)
    