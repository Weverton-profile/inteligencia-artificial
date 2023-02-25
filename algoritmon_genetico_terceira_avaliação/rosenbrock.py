import random
import numpy as np
import math

n = 4

def rosenbrock_function(x):
    return sum(100.0*(x[1:]-x[:-1]**2.0)**2.0 + (1-x[:-1])**2.0)
    
def gerar_populacao(count, tam):
    return [gerar_cromossomo(tam) for _ in range(count)]

def algoritmo_genetico(tamanho_populacao, geracoes):
    populacao = gerar_populacao(tamanho_populacao, n)
    for geracao in range(geracoes):
        nova_populacao = []
        for i in range(tamanho_populacao):
            pai_um = torneio(populacao)
            pai_dois = torneio(populacao)
            # O ALGORITMO SEMPRE FAZ CRUZAMENTO
            filho_um, filho_dois = cruzamento(pai_um, pai_dois)
            filho_um = mutacao(filho_um)
            filho_dois = mutacao(filho_dois)
            nova_populacao.append(filho_um)
            nova_populacao.append(filho_dois)
        populacao = nova_populacao
        populacao.sort(key=lambda x: x.aptidao)
        #print(f'Geracao: {geracao + 1}, Melhor aptidao: {populacao[0].aptidao}')
    melhor_cromossomo = populacao[0]
    return melhor_cromossomo.genes, melhor_cromossomo.aptidao

class Cromossomo:
    def __init__(self, genes):
        self.genes = genes
        self.aptidao = rosenbrock_function(genes)

def gerar_cromossomo(tam):
    genes = np.random.uniform(-2.048, 2.048, size=tam)
    return Cromossomo(genes)

# METODO UTILIZADO PARA A SELEÇÃO
def torneio(populacao):
    p1 = random.choice(populacao)
    p2 = random.choice(populacao)
    return p1 if p1.aptidao < p2.aptidao else p2

def cruzamento(p1, p2):
    c = random.randint(1, len(p1.genes)-1)
    genes_um = np.concatenate((p1.genes[:c], p2.genes[c:]))
    genes_dois = np.concatenate((p2.genes[:c], p1.genes[c:]))
    return Cromossomo(genes_um), Cromossomo(genes_dois)

def mutacao(cromossomo):
    genes = np.copy(cromossomo.genes)
    for i in range(len(genes)):
        # TAXA DE MUTAÇÃO IGUAL A 2%
        if random.uniform(0, 1) <= 0.02:
            genes[i] = np.random.uniform(-2.048, 2.048)
    return Cromossomo(genes)

resultado = algoritmo_genetico(100, 500)
print(f'Melhor solucao: {resultado[0]}, Melhor aptidao: {resultado[1]}')