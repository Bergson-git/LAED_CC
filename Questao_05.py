matriz = [
    [3, 9, 4, 2, 4, 1, 8, 5, 1],
    [1, 2, 3, 4, 5, 6, 7, 8, 9], 
    [5, 8, 2, 3, 9, 8, 4, 1, 7],
    [8, 3, 4, 2, 3, 1, 3, 9, 4], 
    [3, 7, 2, 9, 4, 2, 1, 2, 3], 
    [7, 5, 3, 1, 2, 4, 5, 8, 2],
    [4, 7, 3, 6, 5, 1, 9, 3, 2],
    [1, 5, 3, 2, 9, 8, 7, 6, 5], 
    [3, 9, 4, 2, 4, 1, 8, 5, 1]  
]
for i in range(9):
    for j in range(9):
        print(matriz[i][j],end=" ")
    print()
for i in range(9):
    for k in range(i+1,9):
        igualdade=0
        for q in range(9):
            if matriz[i][q]==matriz[k][q]:
                igualdade+=1
        
        if igualdade==9:
            print(f"A linha {i + 1} e igual a linha {k + 1}")