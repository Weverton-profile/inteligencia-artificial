tipo_de_busca = ['largura', 'profundidade', 'A*', 'gulosa']
distancias_bucareste = [[366, 'Arad'],
                        [0, 'Bucareste'],
                        [160, 'Craiova'],
                        [242, 'Drobeta'],
                        [161, 'Eforie'],
                        [176, 'Fagaras'],
                        [77, 'Giurgiu'],
                        [151, 'Hirsova'],
                        [226, 'Lasi'],
                        [244, 'Lugoj'],
                        [241, 'Mehadia'],
                        [234, 'Neamt'],
                        [380, 'Oradea'],
                        [100, 'Pitesti'],
                        [193, 'Riminieu Vilcea'],
                        [253, 'Sibiu'],
                        [329, 'Timisoara'],
                        [80, 'Urziceni'],
                        [199, 'Vaslui'],
                        [374, 'Zerind']]

mapa_romenia = [['Arad', [[75, 'Zerind'], [140, 'Sibiu'], [118,'Timisoara']]],
                ['Bucareste', [[90, 'Giurgiu'], [101, 'Pitesti'], [211, 'Fagaras'], [85, 'Urziceni']]],
                ['Craiova', [[120, 'Drobeta'], [146, 'Riminieu Vilcea'], [138, 'Pitesti']]],
                ['Drobeta', [[75, 'Mehadia'], [120, 'Craiova']]],
                ['Eforie', [[86, 'Hirsova']]],
                ['Fagaras', [[99, 'Sibiu'], [211, 'Bucareste']]],
                ['Giurgiu', [[90, 'Bucareste']]],
                ['Hirsova', [[98, 'Urziceni'], [86, 'Eforie']]],
                ['Lasi', [[87, 'Neamt'], [92, 'Vaslui']]],
                ['Lugoj', [[111, 'Timisoara'], [70, 'Mehadia']]],
                ['Mehadia', [[70, 'Lugoj'], [75, 'Drobeta']]],
                ['Neamt', [[87, 'Lasi']]],
                ['Oradea', [[71, 'Zerind'], [151, 'Sibiu']]],
                ['Pitesti', [[97, 'Riminieu Vilcea'], [138, 'Craiova'], [101, 'Bucareste']]],
                ['Riminieu Vilcea', [[97, 'Pitesti'], [146, 'Craiova'], [80, 'Sibiu']]],
                ['Sibiu', [[80, 'Riminieu Vilcea'], [99, 'Fagaras'], [140, 'Arad'], [151, 'Oradea']]],
                ['Timisoara', [[118, 'Arad'], [111, 'Lugoj']]],
                ['Urziceni', [[85, 'Bucareste'], [98, 'Hirsova']]],
                ['Vaslui', [[142, 'Urziceni'], [92, 'Lasi']]],
                ['Zerind', [[75, 'Arad'], [71, 'Oradea']]]
                ]

visitados = []
distancia = 0
borda = []

def caminho(origem, algoritmo):
  if algoritmo not in tipo_de_busca:
    raise Exception("Algoritmo não implementado")
  else:
    if algoritmo == 'largura': largura(origem)
    elif algoritmo == 'profundidade': profundidade(origem)
    elif algoritmo == 'A*': busca_estrela(origem)
    else: gulosa(origem)


def largura(origem):
  global borda
  buscando = True
  while len(borda) != 0 or buscando:
    if origem == 'Bucareste':
      print(f'{origem}')
      break
    print(f'{origem} -> ', end="")
    visitados.append(origem)
    for i in range(len(mapa_romenia)):
      if origem == mapa_romenia[i][0]:
        for j in range(len(mapa_romenia[i][1])):
          borda.append(mapa_romenia[i][1][j])
        while borda[0][1] in visitados:
          borda.pop(0)
          origem = borda[0][1]
    origem = borda[0][1]

def profundidade(origem):
  global borda
  buscando = True
  while len(borda) != 0 or buscando:
    if origem == 'Bucareste':
      print(f'{origem}')
      break
    print(f'{origem} -> ', end="")
    visitados.append(origem)
    for i in range(len(mapa_romenia)):
      if origem == mapa_romenia[i][0]:
        for j in range(len(mapa_romenia[i][1])):
          borda.append(mapa_romenia[i][1][j])
        while borda[len(borda) - 1][1] in visitados:
          borda.pop(len(borda) - 1)
          origem = borda[len(borda) - 1][1]
    origem = borda[len(borda) - 1][1]

def busca_estrela(origem):
  global borda
  global distancia
  buscando = True
  while len(borda) != 0 or buscando:
    if origem == 'Bucareste':
      print(f'{origem}, Distancia total: {distancia}')
      break
    print(f'{origem} -> ', end="")
    visitados.append(origem)
    for i in range(len(mapa_romenia)):
      if origem == mapa_romenia[i][0]:
        for j in range(len(mapa_romenia[i][1])):
          borda.append(mapa_romenia[i][1][j])
        for i in range(len(borda)):
          for j in range(len(distancias_bucareste)):
            if borda[i][1] == distancias_bucareste[j][1]:
              borda[i][0] += distancias_bucareste[j][0]
        borda = sorted(borda)
        while borda[0][1] in visitados:
          borda.pop(0)
          origem = borda[0][1]
    print(f'{borda[0][0]} {borda[0][1]}, ')
    for i in range(len(distancias_bucareste)):
      if borda[0][1] == distancias_bucareste[i][1]:
        distancia += borda[0][0] - distancias_bucareste[i][0]
    origem = borda[0][1]

def gulosa(origem):
  global borda
  global distancia
  buscando = True
  while len(borda) != 0 or buscando:
    if origem == 'Bucareste':
      print(f'{origem}, Distancia total: {distancia}')
      break
    print(f'{origem} -> ', end="")
    visitados.append(origem)
    for i in range(len(mapa_romenia)):
      if origem == mapa_romenia[i][0]:
        for j in range(len(mapa_romenia[i][1])):
          borda.append(mapa_romenia[i][1][j])
        borda = sorted(borda)
        while borda[0][1] in visitados:
          borda.pop(0)
          origem = borda[0][1]
    print(f'{borda[0][0]} {borda[0][1]}, ')
    distancia += borda[0][0]
    origem = borda[0][1]

caminho('Lugoj', 'A*')