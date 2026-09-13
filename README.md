# Checkpoint - Pré-processamento de Transcrições TOTVS

## Integrantes

- Victor Alves - RM565723
- João Guilherme - RM565244
- Matheus Kitamura - RM563205
- Gustavo Barroso - RM565705

## Objetivo

Neste checkpoint, fizemos a primeira parte do pré-processamento das transcrições do Challenge TOTVS.

A ideia foi organizar algumas falas em listas, fazer uma limpeza simples dos textos e verificar quais termos já aparecem exatamente no catálogo. Os termos que não foram encontrados ficam separados para serem trabalhados com Programação Dinâmica na próxima etapa.

## O que foi feito

### 1. Registros

Os dados foram organizados no formato:

`[meeting, locutor, texto]`

Também colocamos algumas falas do material do Challenge para usar como exemplo no programa.

### 2. Limpeza do texto

Criamos a função `limpar_texto(texto)`, que usa:

- `lower()` para deixar o texto em letras minúsculas;
- `strip()` para tirar espaços no começo e no final.

Depois da limpeza, os registros continuam com o meeting e o locutor, mas passam a ter o texto tratado.

### 3. Comparação exata

A função `comparar_exato(a, b)` limpa os dois termos antes de comparar.

Se o termo observado for igual a algum item do catálogo, ele recebe `EXATO`. Se não for igual, ele vai para a lista `pendentes_dp`.

Assim, termos como `Totos`, `Protheu` e `totvss` não são corrigidos automaticamente. Eles ficam para a etapa de comparação aproximada.

### 4. Preparação da matriz DP

A função `preparar_dp(a, b)` cria a matriz que será usada na próxima etapa.

O tamanho da matriz é calculado assim:

- linhas = `len(a) + 1`
- colunas = `len(b) + 1`

Esse `+1` é necessário para considerar também o caso em que estamos comparando com uma string vazia.

A primeira linha e a primeira coluna são preenchidas com `0, 1, 2, 3...`.

De forma simples, `dp[i][j]` indica a posição referente aos primeiros `i` caracteres de `a` e aos primeiros `j` caracteres de `b`. Neste checkpoint, não calculamos as células internas da matriz. Essa parte fica para a continuação da implementação de Programação Dinâmica.

## Testes

Foram feitos os testes pedidos no checkpoint:

- `limpar_texto(" TOTOS ")` retorna `"totos"`;
- `comparar_exato("TOTVS", " totvs ")` retorna `True`;
- `comparar_exato("Totos", "totvs")` retorna `False`;
- `preparar_dp("totos", "totvs")` cria uma matriz `6 x 6`;
- `preparar_dp("protheu", "protheus")` cria uma matriz `8 x 9`.

Também foram testados os seguintes pares:

- `totos` x `totvs`
- `protheu` x `protheus`
- `totvss` x `totvs`

No final da execução, a lista `pendentes_dp` contém os termos que não tiveram correspondência exata.

## Como executar

O projeto não precisa instalar nenhuma biblioteca externa.

### VS Code

Abra o arquivo `checkpoint_preprocessamento_totvs.py` no VS Code e execute pelo botão de execução do Python ou pelo terminal.

### PyCharm

Abra o arquivo `checkpoint_preprocessamento_totvs.py` no PyCharm e execute o arquivo.

### Google Colab

Também é possível copiar o código para uma célula do Google Colab e executar.

## Falas usadas do Challenge

Foram usadas 3 falas reais do material fornecido para o Challenge, retiradas da coluna `ANON_TRANSCRICAO` do CSV. No código, foram mantidos somente o meeting, o locutor e o texto da fala.
