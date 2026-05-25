#Verificar se existe um elemento X que aparece K vezes na lista
#Eu corrigi, pois se for "ao menos K vezes", a saída ficaria diferente da esperada
a=[7,1,9,1,7,3,9,2,1,6,8,3]#Este serve apenas para nao haver perda de informação
v=[7,1,9,1,7,3,9,2,1,6,8,3]
k=int(input())
for i in v:
    cont=0
    num=i
    for idx,j in enumerate(v):
        if num==j:
            cont+=1
            v[idx]=0
    if cont==k:
        print(num)
