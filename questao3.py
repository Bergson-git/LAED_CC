
def func(v,numero): 
    i=0
    aux=0
    while numero>0:
        while i<len(v):
            if v[i]==numero and aux==0:
                print(f"O numero {numero} esta na lista")
                return 0
            if v[i]==numero and aux==1:
                print(f"Nao esta la,mas eu encontrei {numero}")
                return 0
            i+=1
        aux=1
        numero-=1
        i=0
    return 0
v=[9,42,3,14,28,21,19,32,46,6]
func(v,13)