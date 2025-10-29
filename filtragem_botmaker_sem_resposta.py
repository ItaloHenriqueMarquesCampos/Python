import pandas as pd
import os

# Caminho da pasta onde estão os arquivos CSV
pasta = r"C:\Users\italo.marques\Desktop\Py\Files"

# Lista de arquivos CSV na pasta
arquivos = [os.path.join(pasta, f) for f in os.listdir(pasta) if f.endswith('.csv')]

# Lista para armazenar os DataFrames processados
dfs_filtrados = []

# Valores que queremos filtrar na coluna "Mensagens do usuário"
valores_validos = [0, 1, 2, 3]

for arquivo in arquivos:
    try:
        df = pd.read_csv(arquivo, encoding='utf-8')
        
        # Converter a coluna "Mensagens do usuário" para numérica (ignorando erros)
        df["Mensagens do usuário"] = pd.to_numeric(df["Mensagens do usuário"], errors='coerce')
        
        # Filtrar os valores desejados
        df_filtrado = df[df["Mensagens do usuário"].isin(valores_validos)]
        
        # Selecionar as colunas desejadas
        df_reduzido = df_filtrado[[
            "Link da conversa",
            "ID do contato/Telefone",
            "Mensagens do usuário"
        ]]
        
        # Adicionar ao conjunto final
        dfs_filtrados.append(df_reduzido)
        print(f"{arquivo} processado com sucesso.")
        
    except Exception as e:
        print(f"Erro ao processar {arquivo}: {e}")

# Unir todos os DataFrames
df_final = pd.concat(dfs_filtrados, ignore_index=True)

# Remover duplicatas com base no "ID do contato/Telefone"
df_final_unico = df_final.drop_duplicates(subset="ID do contato/Telefone")

# Caminho de saída
saida = os.path.join(pasta, "resumo_filtrado.csv")
df_final_unico.to_csv(saida, index=False, encoding='utf-8-sig')

print(f"Arquivo salvo com sucesso em: {saida}")
