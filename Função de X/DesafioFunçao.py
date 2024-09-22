#Importar a Biblioteca numpy
import numpy as np

# Configurações que podem ser alteradas
TAMANHO_POP = 10
PERCENT_MUTACAO = 0.01
NUM_GERACOES = 100
PONTOS_DE_CROSSOVER = 2
ELITISMO = True
PERCENT_ELITE = 0.2
MIN_X = -10
MAX_X = 10
BITS = 20

#Funções que compõe o Algoritmo Genético
def funcao(x):
    return x**3 - 6*x + 14

#Transformar de binário para decimal
def bin_pra_dec(b):
    decimal = int(''.join(map(str, b)), 2)
    return MIN_X + (decimal / (2**BITS - 1)) * (MAX_X - MIN_X)

#Definindo os indivíduos que compõe a população
class Individuo:
    def __init__(self, genoma=None):
        if genoma is None:
            self.genoma = np.random.randint(2, size=BITS)
        else:
            self.genoma = genoma
        self.aptidao = self.avaliar()

#Avaliando a qualidade do indivíduo
    def avaliar(self):
        x = bin_pra_dec(self.genoma)
        return funcao(x)

#Seleciona os melhores indivíduos através do torneio(queremos o com menor aptidão/solução)
def selecionar(populacao):
    torneio = np.random.choice(populacao, size=2)
    return min(torneio, key=lambda ind: ind.aptidao)

#Função para combinarmos o genoma dos pais com os filhos, gerando novos genomas 
def crossover(pai1, pai2):
    ponto_corte1 = np.random.randint(1, BITS - 1)
    if PONTOS_DE_CROSSOVER == 2:
        ponto_corte2 = np.random.randint(ponto_corte1 + 1, BITS)
        filho_genoma = np.concatenate((pai1.genoma[:ponto_corte1], pai2.genoma[ponto_corte1:ponto_corte2], pai1.genoma[ponto_corte2:]))
    else:
        filho_genoma = np.concatenate((pai1.genoma[:ponto_corte1], pai2.genoma[ponto_corte1:]))
    return Individuo(genoma=filho_genoma)

#Função de mutação dos genes(usando o percentual de mutação definido no início do código)
def mutacao(individuo):
    for i in range(BITS):
        if np.random.rand() < PERCENT_MUTACAO:
            individuo.genoma[i] = 1 - individuo.genoma[i]

#Função do algoritmo genético em si, combinando as funções anteriores. Buscando os melhores resultados dentro no número de gerações
def algoritmo_genetico(tamanho_pop=TAMANHO_POP, percent_mutacao=PERCENT_MUTACAO, num_geracoes=NUM_GERACOES):
    populacao = [Individuo() for _ in range(tamanho_pop)]
    melhores = []

    for geracao in range(num_geracoes):
        nova_populacao = []

        if ELITISMO:
            num_elite = int(tamanho_pop * PERCENT_ELITE)
            elite = sorted(populacao, key=lambda ind: ind.aptidao)[:num_elite]
            nova_populacao.extend(elite)

        while len(nova_populacao) < tamanho_pop:
            pai1 = selecionar(populacao)
            pai2 = selecionar(populacao)
            filho = crossover(pai1, pai2)
            mutacao(filho)
            nova_populacao.append(filho)

        populacao = nova_populacao
        melhores.append(min(populacao, key=lambda ind: ind.aptidao))

    melhor_individuo = min(melhores, key=lambda ind: ind.aptidao)
    x_min = bin_pra_dec(melhor_individuo.genoma)
    aptidao_min = melhor_individuo.aptidao

    return x_min, aptidao_min

#Executa o código se o script for executado diretamente
if __name__ == "__main__":
    x_min, aptidao_min = algoritmo_genetico(
        tamanho_pop=10,
        percent_mutacao=0.01,
        num_geracoes=100
    )
    print(f'Valor de x para mínimo da função {x_min:.4f} resultando em {aptidao_min:.4f}')