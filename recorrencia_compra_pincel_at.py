import pandas as pd

# Carregar o arquivo CSV
caminho_entrada = 'Files/MATRIZ RFM.csv'
df_alunos = pd.read_csv(caminho_entrada)

# Verificar se a coluna 'parcela' existe e quais valores ela contém
print("Colunas no arquivo CSV:", df_alunos.columns)
print("Valores únicos na coluna 'parcela':", df_alunos['parcela'].unique())

# Filtrar apenas as compras, onde 'parcela' é igual a 1
df_compras = df_alunos[df_alunos['parcela'] == 1]

# Verificar se há linhas após o filtro
print("Quantidade de linhas após o filtro de 'parcela == 1':", len(df_compras))

# Agrupar os dados por CPF e contar a quantidade de compras (recorrência)
recorrencia = df_compras.groupby(['cpf', 'nome', 'celular', 'endereco', 'uf']).size().reset_index(name='recorrencia')

# Exibir o DataFrame de recorrência com as colunas solicitadas
print("DataFrame de recorrência:")
print(recorrencia)

# Salvar o arquivo com as recorrências
caminho_saida = r'C:\Users\italo.marques\Desktop\Py\RFM_FINAL.csv'
recorrencia.to_csv(caminho_saida, index=False)
