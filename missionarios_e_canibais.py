import time
borda = []
visitados = []
passos = [[1, 0], [0, 1], [1, 1], [2, 0], [0, 2]]

def arvore_de_busca(estado):
  borda.append(estado)
  while len(borda) != 0:
    elemento = borda[len(borda) - 1]
    if teste(elemento): break
    v = nao_visitado(elemento)
    if v == -1: borda.pop()
    else: 
      visitados.append(v)
      borda.append(v)
  return borda

def resolver(estado):
  resultado = []
  for (i, j) in passos:
    res = mover_barco(estado[:], i, j)
    if res == None: continue
    if (esta_morto(res[0], res[1], res[2], res[3])): continue
    if res in visitados: continue
    resultado.append(res)
  return resultado

def esta_morto(mO, cO, mD, cD):
  if (mO < cO and mO > 0) or (mD < cD and mD) > 0: return True
  return False

def nao_visitado(elemento):
  l = resolver(elemento)
  if len(l) > 0: return l[0]
  else: return -1

def teste(estado):
  if (estado[2] == 3 and estado[3] == 3 ): return True
  else: return False
 
def mover_barco(estado, nM=0, nC=0):
  if nM + nC > 2: return
  if estado[4] == 0:
    mO = 0
    cO = 1
    mD = 2
    cD = 3
    
  else:
    mO = 3
    cO = 2
    mD = 1
    cD = 0
  
  if estado[mO] == 0 and estado[cO] == 0: return

  estado[-1] = 1 - estado[-1]

  for i in range(min(nM, estado[mO] )):
    estado[mO] -= 1
    estado[mD] += 1

  for i in range(min(nC, estado[cO] )):
    estado[cO] -= 1
    estado[cD] += 1

  return estado

# estado[0] = M do Lado esquerdo, estado[2] = M do lado direito
# estado[1] = C do Lado esquerdo, estado[3] = C do lado direito
# estado[4] = Posição do Barco sendo 0 esquerda e 1 direita
estado = [3, 3, 0, 0, 0]
inicio = time.time()
res = arvore_de_busca(estado)
for i in range(len(res)):
  md = abs(res[i][0] - res[i - 1][0])
  cd = abs(res[i][1] - res[i - 1][1])
  barco = res[i][4] - res[i-1][4]
  if barco == 1: s = '->'
  else: s = '<-'
  print(f'Missionarios: {md} {s}')
  print(f'Canibais: {cd} {s}')
  print(f'M esquerda: {res[i][0]}, C esquerda: {res[i][1]}, M direita: {res[i][2]}, C direita {res[i][3]}')
fim = time.time()
print(fim - inicio)