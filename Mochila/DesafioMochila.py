#Importar a Biblioteca numpy
import numpy as np

#Valores de entrada(Podem ser modificados)
pesos_e_valores = [[2, 10], [4, 30], [6, 300], [8, 10], [8, 30], [8, 300], [12, 50], [25, 75], [50, 100], [100, 400]]
peso_max = 100
num_de_cromossomos = 150
geracoes = 50

#Função para calcular o peso
def calcular_peso(individuo, pesos_e_valores):
    peso_total = sum(pesos_e_valores[i][0] for i in range(len(individuo)) if individuo[i] == 1)
    valor_total = sum(pesos_e_valores[i][1] for i in range(len(individuo)) if individuo[i] == 1)
    return valor_total, peso_total

#Função para calcular a média dos pesos
def calcular_media_pesos(individuo, pesos_e_valores):
    pesos_marcados = [pesos_e_valores[i][0] for i in range(len(individuo)) if individuo[i] == 1]
    if pesos_marcados:
        return np.mean(pesos_marcados)
    else:
        return 0

#Aqui checamos se o indivídio está abaixo do peso máximo
def avaliar(individuo, pesos_e_valores, peso_max):
    valor_total, peso_total = calcular_peso(individuo, pesos_e_valores)
    if peso_total <= peso_max:
        return valor_total
    else:
        return 0  

#Função que gera a nossa população onde os indivíduos são listas binárias aleatórias
def gerar_populacao(n, tamanho_individuo):
    return [np.random.randint(2, size=tamanho_individuo).tolist() for _ in range(n)]

#Função que seleciona os indivíduos com os melhores fitness, ordenando e limpando metade
def selecionar(populacao, fitnesses):
    indices = np.argsort(fitnesses)[::-1]
    selecionados = [populacao[i] for i in indices[:len(populacao)//2]]
    return selecionados

#Função que realiza o crossover entre os genomas para gerar novos filhos
def cruzar(pai1, pai2):
    ponto_corte = np.random.randint(1, len(pai1)-1)
    filho1 = pai1[:ponto_corte] + pai2[ponto_corte:]
    filho2 = pai2[:ponto_corte] + pai1[ponto_corte:]
    return filho1, filho2

#Aqui aplicamos uma mutaçao nos indivíduos gerados a partir da taxa de mutação
def mutar(individuo, taxa_mutacao):
    return [1 - gene if np.random.rand() < taxa_mutacao else gene for gene in individuo]

#Essa função é nosso algoritmo genético, combinando as funções anteriores e registrando o melhor indivíduo de cada geração
def algoritmo_genetico(pesos_e_valores, peso_max, num_de_cromossomos, geracoes, taxa_mutacao=0.01):
    tamanho_individuo = len(pesos_e_valores)
    populacao = gerar_populacao(num_de_cromossomos, tamanho_individuo)
    melhor_individuo_da_geracao = []

    for geracao in range(geracoes):
        fitnesses = [avaliar(individuo, pesos_e_valores, peso_max) for individuo in populacao]
        melhor_individuo = populacao[np.argmax(fitnesses)]
        media_pesos = calcular_media_pesos(melhor_individuo, pesos_e_valores)
        melhor_individuo_da_geracao.append((np.max(fitnesses), melhor_individuo, media_pesos))
        
        populacao_selecionada = selecionar(populacao, fitnesses)
        nova_populacao = []
        while len(nova_populacao) < num_de_cromossomos:
            pai1, pai2 = np.random.choice(len(populacao_selecionada), 2, replace=False)
            filho1, filho2 = cruzar(populacao_selecionada[pai1], populacao_selecionada[pai2])
            nova_populacao.append(mutar(filho1, taxa_mutacao))
            nova_populacao.append(mutar(filho2, taxa_mutacao))
        
        populacao = nova_populacao[:num_de_cromossomos]

    return melhor_individuo_da_geracao



#Imprime o resultado de cada geração do nosso algoritmo genético
resultado_final = algoritmo_genetico(pesos_e_valores, peso_max, num_de_cromossomos, geracoes)
for valor, individuo, media_pesos in resultado_final:
    print(f"Valor: {valor}, Individuo: {individuo}, Média dos pesos selecionados: {media_pesos:.2f}")