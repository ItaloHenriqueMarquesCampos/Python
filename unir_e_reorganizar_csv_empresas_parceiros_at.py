
import pandas as pd
import os

# Caminho da pasta onde estão os arquivos CSV
pasta = r"C:\Users\italo.marques\Desktop\Py\Files"

# Lista de arquivos CSV para unir
arquivos = [os.path.join(pasta, f) for f in os.listdir(pasta) if f.endswith('.csv')]

# Lista para armazenar os DataFrames
dfs = []

# Carregar os arquivos CSV
for arquivo in arquivos:
    try:
        df = pd.read_csv(arquivo)
        dfs.append(df)
        print(f"{arquivo} carregado com sucesso.")
    except Exception as e:
        print(f"Erro ao carregar {arquivo}: {e}")

# Unir os arquivos CSV em um único DataFrame
df_unido = pd.concat(dfs, ignore_index=True)

# Ordem correta das colunas
ordem_colunas = [
    "createdAt",
    "leadId",
    "telefone",
    "email",
    "nomeDoLead",
    "modalidade",
    "dataVenda",
    "etapaDoLead",
    "nomeDoColaborador",
    "timeDoColaborador",
    "motivoDePerda",
    "origem",
    "dataNovosLeads",
    "dataNegociando",
    "certificadora",
    "utmSource",
    "nomeDaEmpresa",
    "cnpjDaEmpresa"
]

# Verificar se todas as colunas existem no DataFrame
colunas_faltando = [col for col in ordem_colunas if col not in df_unido.columns]
if colunas_faltando:
    print("As seguintes colunas estão ausentes no arquivo unido:", colunas_faltando)
else:
    # Reorganizar as colunas
    df_organizado = df_unido[ordem_colunas]

    # Salvar o novo arquivo CSV
    caminho_saida = os.path.join(pasta, "arquivo_gerado.csv")
    df_organizado.to_csv(caminho_saida, index=False)
    print("arquivo_gerado.csv criado com sucesso.")
