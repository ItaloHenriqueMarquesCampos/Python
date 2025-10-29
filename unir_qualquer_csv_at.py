import pandas as pd
import os

# Caminho para a pasta com os arquivos CSV
caminho_pasta = 'C:\\Users\\italo.marques\\Desktop\\Py\\Files'

# Nome do arquivo CSV final
arquivo_saida = 'C:\\Users\\italo.marques\\Desktop\\Py\\Files\\CSV_UNIDO.csv'

# Listar todos os arquivos CSV na pasta
arquivos_csv = [os.path.join(caminho_pasta, f) 
                for f in os.listdir(caminho_pasta) 
                if f.endswith('.csv')]

# Lista para armazenar os DataFrames
dataframes = []

# Ler cada arquivo CSV e adicioná-lo à lista
for arquivo in arquivos_csv:
    try:
        df = pd.read_csv(arquivo)  # Lê o CSV
        dataframes.append(df)  # Adiciona o DataFrame à lista
        print(f'Arquivo {arquivo} carregado com sucesso.')
    except Exception as e:
        print(f'Erro ao carregar {arquivo}: {e}')

# Concatenar todos os DataFrames em um único
df_unido = pd.concat(dataframes, ignore_index=True)

# Salvar o DataFrame unificado em um novo arquivo CSV
df_unido.to_csv(arquivo_saida, index=False)
print(f'Arquivo CSV unificado salvo em: {arquivo_saida}')
