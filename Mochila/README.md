# Algoritmo Genético para Problema da Mochila

Este projeto implementa um algoritmo genético para resolver uma variação do clássico **Problema da Mochila (Knapsack Problem)**. O objetivo é maximizar o valor total dos itens selecionados sem exceder o peso máximo permitido.

## Descrição

O problema da mochila é definido por uma lista de itens, cada um com um peso e um valor associado. Dada uma capacidade máxima de peso, o desafio é selecionar itens de modo que o valor total seja maximizado sem ultrapassar o limite de peso.

Este algoritmo utiliza uma abordagem evolutiva com os seguintes passos:

- Geração de uma população inicial aleatória
- Avaliação do fitness de cada indivíduo (solução) com base no valor total dos itens selecionados
- Seleção dos indivíduos mais aptos
- Crossover entre os indivíduos selecionados para gerar descendentes
- Mutação de indivíduos com base em uma taxa de mutação
- Execução ao longo de múltiplas gerações para encontrar a melhor solução.

## Estrutura do Código

- `calcular_peso`: Calcula o valor e o peso total de um indivíduo (solução).
- `calcular_media_pesos`: Retorna a média dos pesos dos itens selecionados.
- `avaliar`: Avalia se o indivíduo está dentro do limite de peso e retorna seu valor total.
- `gerar_populacao`: Gera uma população inicial de soluções aleatórias.
- `selecionar`: Seleciona os indivíduos com os melhores fitness (valor).
- `cruzar`: Realiza o crossover entre dois indivíduos para gerar novos filhos.
- `mutar`: Aplica mutações a um indivíduo com base em uma taxa de mutação.
- `algoritmo_genetico`: Função principal que executa o algoritmo genético e retorna o melhor indivíduo de cada geração.

## Como Executar

Para rodar este código, você precisa de Python 3.x e do pacote `numpy`.
A função `algoritmo_genetico` será executada e imprimirá o valor, o indivíduo (solução) e a média dos pesos selecionados para cada geração.
