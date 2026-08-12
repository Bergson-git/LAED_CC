#a)
#O Radix Sort exige que o passo de coleta mantenha a estabilidade.
# Se as filas forem substituídas por pilhas, a ordem relativa dos elementos
# com o mesmo dígito será invertida a cada passo, destruindo a ordenação obtida nos passos anteriores.
#
#Contra exemplo: 
#Considere ordenar a sequência: 15, 12
#
# 1) Passagem (Unidades):
#   - 15 vai para o balde 5.
#   - 12 vai para o balde 2.
#   - Coleta (independe de fila ou pilha pois estão em baldes diferentes): 12, 15
#
# 2) Passagem (Dezenas):
#   - 12 entra no balde 1.
#   - 15 entra no mesmo balde 1.
#
#   Com fila:
#     - O balde 1 contém: 12, 15 (12 entrou primeiro, sai primeiro).
#     - Sequência coletada: [12, 15] - isso é certo
#
#   Com pilha:
#     - O balde 1 empilha 12 e depois 15.
#     - Quando desempilha sai o 15 e depois o 12.
#     - Sequência coletada: [15, 12] - isso é errado pois inverteu o resultado da ordenação anterior.




#b)
def radixsort(v):

  filas1= [[] for i in range(10)]
  for num in v:
    d= num % 10
    filas1[d].append(num)

  coleta1= []
  for f in filas1:
    for elem in f:
      coleta1.append(elem)

  filas2= [[] for i in range(10)]
  for num in coleta1:
    d= (num// 10)% 10
    filas2[d].append(num)

  coleta2= []
  for f in filas2:
    for elem in f:
      coleta2.append(elem)

  filas3= [[] for i in range(10)]
  for num in coleta2:
    d= (num // 100) % 10
    filas3[d].append(num)

  coleta3= []
  for f in filas3:
    for elem in f:
      coleta3.append(elem)

  return filas1, coleta1, filas2, coleta2, filas3, coleta3


v= [481, 329, 143, 612, 937, 480, 256]
f1, c1, f2, c2, f3, c3= radixsort(v)

print("Passagem unidades")
for i in range(10):
  print(f"Fila {i}: {f1[i]}")
print("Coleta 1:", c1)

print("Passagem dezenas")
for i in range(10):
  print(f"Fila {i}: {f2[i]}")
print("Coleta 2:", c2)

print("Passagem centenas")
for i in range(10):
  print(f"Fila {i}: {f3[i]}")
print("Coleta 3:", c3)


#c)
# A complexidade do radix sort para n strings de comprimento fixo L sobre um alfabeto 
# de tamanho x é O(L*(n + x))

# O Merge Sort realiza O(n log n) comparações entre elementos. 
# Como comparar duas strings de comprimento L leva O(L) no pior caso, o tempo total
# do Merge Sort é O(L*n log n).

# Dessa forma, quando L é fixo e x <= n, o Radix Sort opera em tempo linear em relação
# ao tamanho total da entrada O(L*n), sendo mais rapido que o
# Merge Sort por não ter o fator logarítmico O(log n) das comparações.