# Checkpoint - Pré-processamento de Transcrições TOTVS

## Integrantes

- Victor Alves - RM565723
- João Guilherme - RM565244
- Matheus Kitamura - RM563205
- Gustavo Barroso - RM565705

## Objetivo

Construir a etapa inicial de um pré-processador para transcrições do Challenge TOTVS.

O programa transforma falas brutas em registros estruturados, realiza uma limpeza básica do texto, separa os casos de igualdade exata dos casos que precisam de comparação aproximada e prepara a matriz de Programação Dinâmica para a próxima etapa.

Nesta etapa, a distância de edição completa não é calculada. As células internas da matriz permanecem com seus valores iniciais.

## Organização das funções

### `limpar_texto(texto)`

Recebe um texto e aplica:

- `lower()` para transformar as letras em minúsculas;
- `strip()` para remover espaços no início e no final.

A função recebe o texto por parâmetro e retorna o texto limpo.

### `comparar_exato(a, b)`

Utiliza `limpar_texto()` nos dois termos e verifica se eles são exatamente iguais.

Quando o termo observado corresponde ao catálogo, ele recebe o status `EXATO`. Caso contrário, entra na lista `pendentes_dp`.

### `preparar_dp(a, b)`

Prepara a matriz usada na comparação aproximada.

As dimensões são:

- linhas = `len(a) + 1`
- colunas = `len(b) + 1`

O `+1` existe porque a matriz também representa o caso-base relacionado à string vazia.

A primeira coluna recebe os valores `0, 1, 2, ...` e a primeira linha também recebe `0, 1, 2, ...`.

O estado `dp[i][j]` representa o subproblema associado aos primeiros `i` caracteres de `a` e aos primeiros `j` caracteres de `b`. Nesta etapa, somente a estrutura e os casos-base são preparados; a transição das células internas será feita posteriormente na disciplina.

## Fluxo do programa

```text
Registros brutos
       ↓
Limpeza básica
       ↓
Comparação exata
       ↓
EXATO / PENDENTE_DP
       ↓
Preparação da matriz DP
```

## Casos testados

O programa executa os testes mínimos solicitados:

- `limpar_texto(" TOTOS ")` → `"totos"`
- `comparar_exato("TOTVS", " totvs ")` → `True`
- `comparar_exato("Totos", "totvs")` → `False`
- `preparar_dp("totos", "totvs")` → matriz `6 × 6`
- `preparar_dp("protheu", "protheus")` → matriz `8 × 9`

Também são preparadas as comparações:

- `totos × totvs`
- `protheu × protheus`
- `totvss × totvs`

## Como executar

### Python / PyCharm

Abra o arquivo `checkpoint_preprocessamento_totvs.py` no PyCharm e execute normalmente.

### Google Colab

Também é possível copiar o conteúdo para uma célula do Colab e executar.

O programa não depende de bibliotecas externas.

## Falas adicionais do Challenge

Foram adicionadas 3 falas reais do material do Challenge, extraídas da coluna `ANON_TRANSCRICAO` do CSV fornecido pelo grupo. Foram mantidos apenas o `meeting`, o `locutor` e o texto da fala, sem dados pessoais desnecessários.
