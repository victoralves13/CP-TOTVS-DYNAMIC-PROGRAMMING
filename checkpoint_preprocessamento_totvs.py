# Checkpoint - Pré-processamento de Transcrições TOTVS
# Dynamic Programming - Engenharia de Software

# ============================================================
# ETAPA 1 - REGISTROS
# ============================================================

registros = [
    ["1247082", "LOCUTOR 54", " Perguntar se era o novo uniforme da Totos. "],
    ["1247082", "LOCUTOR 49", "A sua e da TOTVS, nao e?"],
    ["1247082", "LOCUTOR 72", "O time usa Protheu no processo."],
    ["1247082", "LOCUTOR 49", "Podemos revisar a proposta do Protheus."],
    ["1247082", "LOCUTOR 83", "O modulo Datasul esta funcionando."],
    ["1247082", "LOCUTOR 72", "A migracao para totvss ainda esta em analise."],

    # 3 falas reais extraídas do material do Challenge (CSV)
    ["1000000", "LOCUTOR 1", "A nossa solução conecta todas as lojas em uma plataforma."],
    ["1000000", "LOCUTOR 2", "Como funciona?"],
    ["1000000", "LOCUTOR 1", "A gente oferece uma plataforma integrada."]
]

print("=" * 60)
print("ETAPA 1 - REGISTROS BRUTOS")
print("=" * 60)

for registro in registros:
    print("Meeting:", registro[0])
    print("Locutor:", registro[1])
    print("Texto:", registro[2])
    print("-" * 40)

print("Quantidade total processada:", len(registros))


# ============================================================
# ETAPA 2 - LIMPEZA BÁSICA
# ============================================================

def limpar_texto(texto):
    return texto.lower().strip()


registros_limpos = []

for registro in registros:
    meeting = registro[0]
    locutor = registro[1]
    texto = registro[2]

    texto_limpo = limpar_texto(texto)

    registros_limpos.append([meeting, locutor, texto_limpo])


print()
print("=" * 60)
print("ETAPA 2 - REGISTROS LIMPOS")
print("=" * 60)

for i in range(len(registros)):
    print("Antes :", registros[i][2])
    print("Depois:", registros_limpos[i][2])
    print("-" * 40)


# ============================================================
# ETAPA 3 - COMPARAÇÃO EXATA
# ============================================================

catalogo = ["totvs", "protheus", "datasul", "rm", "fluig", "senior"]

termos_observados = [
    "Totos",
    "TOTVS",
    "Protheu",
    "Protheus",
    "Datasul",
    "totvss"
]


def comparar_exato(a, b):
    return limpar_texto(a) == limpar_texto(b)


pendentes_dp = []
relatorio = []

for termo in termos_observados:
    encontrado = False

    for item in catalogo:
        if comparar_exato(termo, item):
            encontrado = True
            break

    if encontrado:
        relatorio.append([termo, "EXATO"])
    else:
        relatorio.append([termo, "PENDENTE_DP"])
        pendentes_dp.append(termo)


print()
print("=" * 60)
print("ETAPA 3 - TRIAGEM POR IGUALDADE EXATA")
print("=" * 60)

for item in relatorio:
    print("Termo:", item[0], "| Status:", item[1])

print()
print("Lista de pendentes para DP:", pendentes_dp)


# ============================================================
# ETAPA 4 - PREPARAÇÃO DA MATRIZ DP
# ============================================================

def preparar_dp(a, b):
    a = limpar_texto(a)
    b = limpar_texto(b)

    linhas = len(a) + 1
    colunas = len(b) + 1

    matriz = []

    for i in range(linhas):
        linha = []

        for j in range(colunas):
            linha.append(0)

        matriz.append(linha)

    for i in range(linhas):
        matriz[i][0] = i

    for j in range(colunas):
        matriz[0][j] = j

    return matriz


# ============================================================
# ETAPA 5 - CONEXÃO DOS PENDENTES AO PIPELINE
# ============================================================

pares_teste = [
    ["totos", "totvs"],
    ["protheu", "protheus"],
    ["totvss", "totvs"]
]

print()
print("=" * 60)
print("ETAPA 5 - MATRIZES DP PREPARADAS")
print("=" * 60)

for par in pares_teste:
    a = par[0]
    b = par[1]

    dp = preparar_dp(a, b)

    print()
    print("Comparação:", a, "x", b)
    print("Número de linhas:", len(dp))
    print("Número de colunas:", len(dp[0]))
    print("Primeira linha:", dp[0])

    primeira_coluna = []

    for i in range(len(dp)):
        primeira_coluna.append(dp[i][0])

    print("Primeira coluna:", primeira_coluna)

    print("Matriz preparada:")
    for linha in dp:
        print(linha)


# ============================================================
# TESTES MÍNIMOS DE ACEITAÇÃO
# ============================================================

print()
print("=" * 60)
print("TESTES MÍNIMOS DE ACEITAÇÃO")
print("=" * 60)

print('limpar_texto(" TOTOS ") =', limpar_texto(" TOTOS "))
print('comparar_exato("TOTVS", " totvs ") =',
      comparar_exato("TOTVS", " totvs "))
print('comparar_exato("Totos", "totvs") =',
      comparar_exato("Totos", "totvs"))

dp_totos = preparar_dp("totos", "totvs")
print('preparar_dp("totos", "totvs") =', len(dp_totos), "x", len(dp_totos[0]))

dp_protheu = preparar_dp("protheu", "protheus")
print('preparar_dp("protheu", "protheus") =',
      len(dp_protheu), "x", len(dp_protheu[0]))

print("pendentes_dp =", pendentes_dp)

print()
print("Execução concluída.")
