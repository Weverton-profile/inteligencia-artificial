import random

def diagonal_direita(matriz, linha, coluna, usadas):
  superio_linha = linha - 1
  superior_coluna = coluna + 1
  inferior_linha = linha + 1
  inferior_coluna = coluna + 1
  while superio_linha >= 0 and superior_coluna < len(matriz):
    #print(linha, ' ',coluna)
    #print(matriz[superio_linha][superior_coluna])
    usadas.add((superio_linha, superior_coluna))
    superio_linha -= 1
    superior_coluna += 1

  while inferior_linha < len(matriz) and inferior_coluna < len(matriz):
    #print(linha, ' ',coluna)
    #print(matriz[inferior_linha][inferior_coluna])
    usadas.add((inferior_linha, inferior_coluna)) 
    inferior_linha += 1
    inferior_coluna += 1
  return

def diagonal_esquerda(matriz, linha, coluna, usadas):
  superio_linha = linha - 1
  superior_coluna = coluna - 1
  inferior_linha = linha + 1
  inferior_coluna = coluna - 1
  while superio_linha >= 0 and superior_coluna >= 0:
    #print(linha, ' ',coluna)
    #print(matriz[superio_linha][superior_coluna])
    usadas.add((superio_linha, superior_coluna))
    superio_linha -= 1
    superior_coluna -= 1

  while inferior_linha < len(matriz) and inferior_coluna >= 0:
    #print(linha, ' ',coluna)
    #print(matriz[inferior_linha][inferior_coluna])
    usadas.add((inferior_linha, inferior_coluna))
    inferior_linha += 1
    inferior_coluna -= 1
  return

def coluna_inferior(matriz, linha, coluna, usadas):
  while linha < len(matriz):
    #print(linha, ' ',coluna)
    #print(matriz[linha][coluna])
    usadas.add((linha, coluna))
    linha += 1
  return

def coluna_superior(matriz, linha, coluna, usadas):
  while linha >= 0:
    #print(linha, ' ',coluna)
    #print(matriz[linha][coluna])
    usadas.add((linha, coluna))
    linha -= 1
  return

def linha_direita(matriz, linha, coluna, usadas):
  while coluna < len(matriz):
    #print(linha, ' ',coluna)
    #print(matriz[linha][coluna])
    usadas.add((linha, coluna))
    coluna += 1
  return

def linha_esquerda(matriz, linha, coluna, usadas):
  while coluna >= 0:
    #print(linha, ' ',coluna)
    #print(matriz[linha][coluna])
    usadas.add((linha, coluna))
    coluna -= 1
  return

# matriz = [['A', 'B', 'C', 'D', 'E', 'F'],
#           ['G', 'H', 'I', 'J', 'K', 'L'],
#           ['M', 'N', 'O', 'P', 'Q', 'R'],
#           ['S', 'T', 'U', 'V', 'W', 'X'],
#           ['Y', 'Z', '1', '2', '3', '4'],
#           ['5', '6', '7', '8', '9', '0']]
# usadas = {0}
# coluna_superior(matriz, 1 - 1, 2, usadas)
# coluna_inferior(matriz, 1 + 1, 2, usadas)
# linha_direita(matriz, 1, 2 + 1, usadas)
# linha_esquerda(matriz, 1, 2 - 1, usadas)
# diagonal_direita(matriz, 1, 2, usadas)
# diagonal_esquerda(matriz, 1, 2, usadas)
# print(len(usadas))
# for coordenadas in usadas:
#   print(coordenadas)

def posicao_aleatoria(matriz, usadas):
  count = 0
  linha = random.randint(0, len(matriz) - 1)
  coluna = random.randint(0, len(matriz) - 1)
  while count < len(matriz):
    if (linha, coluna) not in usadas:
      matriz[linha][coluna] = 'Q'
      count += 1
      usadas.add((linha, coluna))
      coluna_superior(matriz, linha - 1, coluna, usadas)
      coluna_inferior(matriz, linha + 1, coluna, usadas)
      linha_direita(matriz, linha, coluna + 1, usadas)
      linha_esquerda(matriz, linha, coluna - 1, usadas)
      diagonal_direita(matriz, linha, coluna, usadas)
      diagonal_esquerda(matriz, linha, coluna, usadas)
    else:
      linha = random.randint(0, len(matriz) - 1)
      coluna = random.randint(0, len(matriz) - 1)
    if count < len(matriz) and len(usadas) >= (rainhas*rainhas):
      limite = 0
      count = 0
      usadas.clear()
      matriz.clear
      matriz = [ [' ' for i in range(rainhas)] for j in range(rainhas)]
  exibe_tabuleiro(matriz)
  
    
def exibe_tabuleiro(matriz):
  for i in range(len(matriz)):
    for j in range(len(matriz)):
      print('|', end='')
      print(matriz[i][j], end='')
      if j == len(matriz) - 1:
        print('|')
  return

usadas = {0}

rainhas = 25 #substitua pela quantidade de rainhas que deseja testar
matriz = [ [' ' for i in range(rainhas)] for j in range(rainhas)]
posicao_aleatoria(matriz, usadas)