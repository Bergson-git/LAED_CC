#a)
class No:

  def __init__(self, val="", prox=None):
    self.val= val
    self.prox= prox

def verificarbalanceamento(expressao):
  topo= None
  pares= {')': '(', ']': '[', '}': '{'}
  abridores= {'(', '[', '{'}
  fechadores= {')', ']', '}'}

  for i, char in enumerate(expressao):
    if char in abridores:
      novo= No(char, topo)
      topo= novo

    elif char in fechadores:
      if topo is None:
        return False, f"Erro na posição {i}: fechador '{char}' sem abridor correspondente"

      desempilhado= topo.val
      topo= topo.prox

      if desempilhado!= pares[char]:
        return False, f"Erro na posição {i}: fechador '{char}' não combina com abridor '{desempilhado}'"

  if topo != None:
    return False, f"Erro: abridor '{topo.val}' não foi fechado"

  return True, "Válida"

cadeias= ["({[]})","({[]}]","({[]}[()]{})"]

for exp in cadeias:
  valida, msg= verificarbalanceamento(exp)
  print(f"Cadeia '{exp}':{msg}")

#b)
#complexidade de tempo: O(n), onde n é o comprimento da expressão
#complexidade de espaço: O(n) no pior caso, pois se a expressão contiver apenas abridores, 
# a pilha encadeada armazenará até n nós na memória.

#c)
# 1) ({[]}): VÁLIDA. Todos os delimitadores foram empilhados e desempilhados na ordem correta.
# 2) ({[]}]: INVÁLIDA. Erro na posição 5: o fechador ']' tenta fechar o abridor '('
# 3) ({[]}[()]{}):  VÁLIDA. Todos os blocos foram fechados corretamente.