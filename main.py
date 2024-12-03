import numpy as np
import pandas as pd
import matplotlib.pyplot as plt




# 1. Criando um DataFrame fictício de vendas
data = {
    "Produto": ["A", "B", "C", "D", "E"],
    "Vendas": np.random.randint(50, 200, size=5),
    "Custo": np.random.randint(20, 100, size=5)
}
df = pd.DataFrame(data)

# 2. Calculando o lucro
df["Lucro"] = df["Vendas"] - df["Custo"]

# Exibindo os dados no console
print("Tabela de vendas:")
print(df)

# 3. Plotando os dados
plt.figure(figsize=(10, 6))

# Gráfico de barras para as vendas e lucros
bar_width = 0.4
indices = np.arange(len(df))

plt.bar(indices, df["Vendas"], bar_width, label="Vendas", color="blue")
plt.bar(indices + bar_width, df["Lucro"], bar_width, label="Lucro", color="green")

# Configurando o gráfico
plt.xlabel("Produtos")
plt.ylabel("Valores (em R$)")
plt.title("Análise de Vendas e Lucro por Produto")
plt.xticks(indices + bar_width / 2, df["Produto"])
plt.legend()

# Exibindo o gráfico
plt.tight_layout()
plt.show()