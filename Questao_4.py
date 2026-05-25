#Achar qual elemento NAO possui seu antecessor e sucessor na lista. Nesse caso, apenas o 4.
#Ficou apenas o 4 pois eu corrigi a lista, uma vez que a resposta seria 16 e 4, e nao somente 4(como orientado na saída)
v=[7,2,8,1,7,13,9,12,4,14]
for i in v:
    achei=1
    for j in v:
        if j==i+1 or j==i-1:
            achei=0
            break
    if achei==1:
        print(f"O elemento isolado e o {i}")
        