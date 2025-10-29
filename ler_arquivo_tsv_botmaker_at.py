import pandas as pd
import os

# Caminho da pasta onde estão os arquivos .tsv
caminho_pasta = r"C:\Users\italo.marques\Desktop\Py\Files"

# Lista todos os arquivos da pasta que terminam com .tsv
arquivos_tsv = [f for f in os.listdir(caminho_pasta) if f.endswith('.tsv')]

# Verifica se há arquivos .tsv
if not arquivos_tsv:
    print("Nenhum arquivo .tsv encontrado na pasta.")
else:
    for nome_arquivo in arquivos_tsv:
        caminho_arquivo = os.path.join(caminho_pasta, nome_arquivo)
        try:
            df = pd.read_csv(caminho_arquivo, sep='\t')  # Lê o arquivo .tsv
            print(f"\nArquivo: {nome_arquivo}")
            print(df.head())  # Exibe as 5 primeiras linhas
        except Exception as e:
            print(f"Erro ao ler {nome_arquivo}: {e}")

print("Concluído com sucesso")
