# Análise Estatística de Despesas Públicas com Excel

Este projeto tem como objetivo aplicar conceitos básicos de estatística descritiva e regressão linear simples utilizando exclusivamente o Microsoft Excel, com dados reais de despesas públicas mensais do Governo Federal, disponibilizados pelo Banco Central do Brasil (SGS 22703).

## Objetivo

Demonstrar a capacidade do Excel em realizar análises estatísticas básicas, com visualizações e interpretações claras. O projeto também visa destacar como essas análises poderiam ser replicadas em linguagens como Python, mas aqui optou-se por realizar todo o processo no Excel para reforçar o domínio da ferramenta.

## Fonte dos Dados

- **Banco Central do Brasil (BACEN) - SGS 22703**
- Indicador: Despesas pagas pelo Governo Federal (em bilhões de R$), dados mensais.
- Período: Janeiro de 2022 a Maio de 2024
- Arquivo utilizado: `transacoes_despesas_mensal.csv`

## Etapas do Projeto

### 1. Limpeza e Formatação

- Ajuste dos dados importados: nomes de colunas e datas.
- Conversão de valores para número.
- Ajustes visuais e de número (milhares, uma casa decimal).

### 2. Estatística Descritiva

- Fórmulas aplicadas no Excel:
  - **Média**: `=MÉDIA(B2:B30)`
  - **Mediana**: `=MED(B2:B30)`
  - **Desvio Padrão**: `=DESVPAD(B2:B30)`
  - **Mínimo e Máximo**: `=MÍNIMO(B2:B30)`, `=MÁXIMO(B2:B30)`

### 3. Visualização

- Gráfico de linha das despesas ao longo do tempo.
- Eixo Y ajustado com separador de milhar e 1 casa decimal.

### 4. Regressão Linear Simples

- Criada nova aba com:
  - **Coluna A**: Índice de período (`=LIN()-1`)
  - **Coluna B**: Valores de despesa.
- Gráfico de Dispersão com marcadores.
- Adicionada linha de tendência com:
  - Equação da reta
  - Valor de R²

### 5. Interpretação

- O R² foi utilizado como medida da capacidade preditiva da reta.
- Observou-se uma tendência crescente nos gastos públicos ao longo do tempo, com boa aderência da linha de tendência.

## Considerações

Embora essa análise possa ser feita com Python, pandas, matplotlib e outras bibliotecas, a escolha pelo Excel visa mostrar que é possível realizar análises robustas mesmo com ferramentas tradicionais. Este projeto também pode ser útil para contextos corporativos onde o Excel é a principal ferramenta disponível.

## Imagens Geradas

- `imagens/estatisticas_excel.png` — Estatísticas descritivas
- `imagens/grafico_linha_despesas.png` — Gráfico de linha mensal
- `imagens/grafico_dispersao_regressao.png` — Gráfico de regressão com equação e R²

## Estrutura do Projeto

