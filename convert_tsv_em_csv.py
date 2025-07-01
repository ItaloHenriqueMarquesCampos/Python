import pandas as pd
import os
caminho_tsv = r"C:\Users\Pichau\Downloads\sessionStartingCauses-2025.07.01-05.41.tsv"

caminho_csv = os.path.splitext(caminho_tsv)[0] + ".csv"

df = pd.read_csv(caminho_tsv, sep="\t")

df.to_csv(caminho_csv, sep=",", index=False)

print("Conversão concluída com sucesso! Arquivo CSV salvo em:")
print(caminho_csv)