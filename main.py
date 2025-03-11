import numpy as np
import pandas as pd

# Simulação dos dados da planilha
dados = {
    "Peso Medido": [3120, 3090, 3090, 3090, 3210, 3240, 3180, 3180, 3120, 3190,
                     3190, 3180, 3400, 3370, 3190, 3040, 3020, 2890, 2930, 2910,
                     3080, 2970, 2930, 2990, 3010, 3020, 3030, 2870, 2960, 3090,
                     2940, 2960, 3000, 3050, 3030, 3070, 3170, 3180, 3220, 3150,
                     3000, 3140, 3120, 3220, 3180, 3060, 3090, 3110, 3280, 3300,
                     3050, 3120, 3170, 3370, 3350, 3130, 3080, 3340, 3340, 3410,
                     3120, 3250, 3270, 3070, 3300, 3230, 3190, 3390, 3100, 3300,
                     3300, 3340, 3310, 3260, 3340, 3400, 3230, 3300, 3230, 3280, 3220],
    "Peso Real": [3500] * 81
}

# Criar DataFrame
df = pd.DataFrame(dados)

# Calcular erro percentual inicial
df["Erro %"] = (df["Peso Medido"] - df["Peso Real"]) / df["Peso Real"] * 100

# Intervalo de porcentagens de correção a serem testadas (0% a 20% com passos de 0.01%)
percentuais = np.arange(0, 20.01, 0.01) / 100  # De 0% a 20% com precisão de 0.01%

# Dicionário para armazenar os resultados
resultados = []

for p in percentuais:
    peso_corrigido = df["Peso Medido"] * (1 + p)
    erro_corrigido = (peso_corrigido - df["Peso Real"]) / df["Peso Real"] * 100
    erro_medio = erro_corrigido.abs().mean()  # Média do valor absoluto dos erros
    erro_maximo = erro_corrigido.abs().max()  # Máximo do valor absoluto dos erros
    resultados.append({"Percentual": round(p * 100, 2), "Erro Médio": round(erro_medio, 2), "Erro Máximo": round(erro_maximo, 2)})

# Criar DataFrame com os resultados
df_resultados = pd.DataFrame(resultados)

# Identificar o melhor percentual baseado no menor erro máximo e médio
melhor_percentual = df_resultados.sort_values(["Erro Máximo", "Erro Médio"]).iloc[0]

print("Melhor percentual de correção:")
print(melhor_percentual)

# Exibir os 5 melhores percentuais
print("\nTop 5 melhores percentuais de correção:")
print(df_resultados.sort_values(["Erro Máximo", "Erro Médio"]).head(5))
