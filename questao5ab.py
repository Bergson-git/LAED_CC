#Verificar se existem dois elementos na lista L tais que
#um deles e o dobro do outro( esse meu algoritmo resolve uma lista ordenada e desordenada)
v=[9,42,21,14,25,3,19,33,45,6]
aux=1
for i in range(0,10):
    for j in range(0,10):
        if v[i]*2==v[j]:
            print(f"Sim, os numeros {v[i]} e {v[j]}")
            aux=0

if aux==1:
    print("Nao tem")