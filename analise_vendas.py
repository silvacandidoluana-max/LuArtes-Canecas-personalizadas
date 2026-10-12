# ==========================================
# PROJETO: Análise de Vendas da LuArtes
# ==========================================

import matplotlib
matplotlib.use('Agg') # Força o Matplotlib a trabalhar apenas em modo de salvamento, sem abrir janelas
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns

from datetime import datetime, timedelta
import random

print("Ambiente carregado e bibliotecas prontas para uso!")

# Catálogo da LuArtes
produtos_luartes = [
    "Caneca Porcelana",
    "Caneca Polímero Infantil",
    "Caneca com Colher",
    "Caneca Mágica Térmica",
    "Caneca de Alumínio Chopp",
    "Garrafa squeeze"
]

precos = [45.0, 30.0, 50.0, 65.0, 55.0, 30.0]
print("Catálogo de produtos da LuArtes configurado com sucesso!")

# ==========================================
# 3. GERAÇÃO DE HISTÓRICO DE VENDAS
# ==========================================

# Vamos simular 100 vendas passadas da LuArtes
n_vendas = 100

dados_vendas = {
    "Data": [datetime.now() - timedelta(days=random.randint(0, 30)) for _ in range(n_vendas)],
    "Produto": [random.choice(produtos_luartes) for _ in range(n_vendas)],
    "Quantidade": [random.randint(1, 5) for _ in range(n_vendas)]
}

# Criando o nosso DataFrame (tabela de dados) com Pandas
df_vendas = pd.DataFrame(dados_vendas)

print("\n--- Primeiras vendas geradas com sucesso ---")
print(df_vendas.head())

# ==========================================
# 4. ADICIONANDO PREÇOS E CALCULANDO FATURAMENTO
# ==========================================

# Mapeando os preços correspondentes a cada produto vendido na tabela
mapeamento_precos = dict(zip(produtos_luartes, precos))
df_vendas["Preco_Unitario"] = df_vendas["Produto"].map(mapeamento_precos)

# Calculando o valor total da venda (Quantidade * Preço Unitário)
df_vendas["Faturamento_Total"] = df_vendas["Quantidade"] * df_vendas["Preco_Unitario"]

print("\n--- Tabela Completa de Vendas da LuArtes (Primeiras Linhas) ---")
print(df_vendas.head())

# ==========================================
# 5. RESUMO E MÉTRICAS DE NEGÓCIO DA LUARTES
# ==========================================

# Faturamento total somando toda a coluna de faturamento
faturamento_total = df_vendas["Faturamento_Total"].sum()

# Quantidade total de itens vendidos
total_itens_vendidos = df_vendas["Quantidade"].sum()

# Vendas agrupadas por tipo de produto
vendas_por_produto = df_vendas.groupby("Produto")[["Quantidade", "Faturamento_Total"]].sum()

print(f"\n==========================================")
print(f"       RELATÓRIO GERENCIAL - LUARTES      ")
print(f"==========================================")
print(f"💰 Faturamento Total: R$ {faturamento_total:.2f}")
print(f"📦 Total de Itens Vendidos: {total_itens_vendidos} unidades")
print(f"\n--- Desempenho por Produto ---")
print(vendas_por_produto)
print(f"==========================================")

# ==========================================
# 6. GERAÇÃO DE GRÁFICO DE VENDAS
# ==========================================

# Definindo o estilo visual do gráfico
sns.set_theme(style="whitegrid")

plt.figure(figsize=(10, 6))

# Criando um gráfico de barras com o faturamento por produto
# Resetamos o índice para transformar o Produto de volta em coluna para o gráfico
df_grafico = vendas_por_produto.reset_index()

ax = sns.barplot(
    data=df_grafico, 
    x="Produto", 
    y="Faturamento_Total", 
    palette="Blues_d"
)

# Adicionando títulos e rótulos profissionais
plt.title("Faturamento Total por Produto - LuArtes", fontsize=16, fontweight='bold', pad=15)
plt.xlabel("Produtos", fontsize=12)
plt.ylabel("Faturamento Total (R$)", fontsize=12)
plt.xticks(rotation=20, ha='right')
# Exibindo o gráfico na tela
plt.tight_layout()
plt.savefig("grafico_faturamento_luartes.png", dpi=300, bbox_inches='tight')
plt.savefig("grafico_faturamento_luartes.png", dpi=300, bbox_inches='tight')
print("\n📊 Gráfico gerado e salvo com sucesso como 'grafico_faturamento_luartes.png'!")
# ==========================================
# 7. EXPORTANDO DADOS PARA O EXCEL / CSV
# ==========================================

# Salvando o DataFrame completo num arquivo CSV
nome_arquivo = "relatorio_vendas_luartes.csv"
df_vendas.to_csv(nome_arquivo, index=False, encoding="utf-8-sig")

print(f"\n📁 Sucesso! Relatório de vendas exportado com o nome: '{nome_arquivo}'")