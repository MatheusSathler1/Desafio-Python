# Algoritmo Genético para Minimização de Função

Este projeto implementa um algoritmo genético para encontrar o valor de **x** que minimiza a função \( f(x) = x^3 - 6x + 14 \) no intervalo [-10, 10]. O algoritmo busca a solução ideal através de técnicas evolutivas, incluindo seleção por torneio, crossover, e mutação.

## Descrição

O algoritmo genético simula o processo de evolução, onde uma população de indivíduos (soluções representadas em binário) evolui ao longo de várias gerações. Cada indivíduo é avaliado com base na função objetivo, e os melhores indivíduos são selecionados para gerar novos filhos através de crossover. O processo é repetido até que o número máximo de gerações seja atingido.

### Parâmetros Configuráveis

- **TAMANHO_POP**: Tamanho da população (número de indivíduos).
- **PERCENT_MUTACAO**: Probabilidade de mutação em cada gene.
- **NUM_GERACOES**: Número de gerações que o algoritmo deve executar.
- **PONTOS_DE_CROSSOVER**: Número de pontos de corte para o crossover (1 ou 2).
- **ELITISMO**: Se `True`, preserva os melhores indivíduos de cada geração.
- **PERCENT_ELITE**: Percentual da população que será preservada através do elitismo.
- **MIN_X / MAX_X**: Limites inferior e superior do intervalo para **x**.
- **BITS**: Número de bits para representar cada indivíduo.

### Classes e Funções

- **Individuo**: Representa um indivíduo (solução). Cada indivíduo é composto por um genoma binário que codifica um valor de **x**.
- **funcao(x)**: A função objetivo que estamos minimizando.
- **bin_pra_dec(b)**: Converte um genoma binário para um valor decimal de **x** no intervalo [-10, 10].
- **selecionar**: Seleciona dois indivíduos da população usando um torneio e retorna o indivíduo com melhor aptidão (menor valor da função).
- **crossover**: Realiza o crossover entre dois pais para gerar um novo filho.
- **mutacao**: Aplica a mutação a um indivíduo, alterando bits aleatórios com base na taxa de mutação.
- **algoritmo_genetico**: Executa o processo evolutivo, retornando o valor de **x** que minimiza a função e seu valor correspondente.

## Como Executar

Este código requer Python 3.x e a biblioteca `numpy`.
Para executar o algoritmo genético e encontrar o mínimo da função, basta rodar o script principal. A solução será impressa no terminal, mostrando o valor de **x** que minimiza a função e o valor mínimo correspondente.
