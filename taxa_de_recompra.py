import pandas as pd

# Caminho do arquivo CSV
arquivo = r"C:\Users\Pichau\Desktop\Arquivos PY\Gerador\Parceiro - Export.csv"

# Carregar dados
df = pd.read_csv(arquivo)

# Converter datas
df["dt_doc"] = pd.to_datetime(df["dt_doc"], errors="coerce")

# Ordenar para garantir que cada cliente esteja organizado por data
df = df.sort_values(by=["cpf", "dt_doc"])

# Criar coluna de compra anterior do mesmo cliente
df["compra_anterior"] = df.groupby("cpf")["dt_doc"].shift(1)

# Calcular diferença em meses entre compras
df["diferenca_meses"] = (df["dt_doc"] - df["compra_anterior"]) / pd.Timedelta(days=30)

# Identificar recompras (menos de 12 meses desde a compra anterior)
df["recompra"] = df["diferenca_meses"].apply(lambda x: 1 if pd.notnull(x) and x < 12 else 0)

# Total de transações
total_transacoes = len(df)

# Total de recompras
total_recompras = df["recompra"].sum()

# Taxa de recompra
taxa_recompra = (total_recompras / total_transacoes) * 100

print("Total de transações:", total_transacoes)
print("Total de recompras:", total_recompras)
print(f"Taxa de recompra: {taxa_recompra:.2f}%")
