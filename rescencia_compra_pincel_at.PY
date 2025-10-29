import pandas as pd

# Carregar o arquivo CSV
caminho_entrada = 'Files/MATRIZ_RFM.csv'
df_alunos = pd.read_csv(caminho_entrada)

# Verificar as colunas do arquivo CSV
print("Colunas no arquivo CSV:", df_alunos.columns)

# Filtrar apenas as compras onde 'parcela' é igual a 1
df_compras = df_alunos[df_alunos['parcela'] == 1]

# Verificar se há linhas após o filtro
print("Quantidade de linhas após o filtro de 'parcela == 1':", len(df_compras))

# Agrupar os dados por CPF e pegar a data da compra mais recente (último curso comprado)
df_compras['data_pagto'] = pd.to_datetime(df_compras['data_pagto'], errors='coerce')  # Converter a data de pagamento para o formato datetime
recencia = df_compras.groupby(['cpf', 'nome', 'celular', 'endereco', 'uf'])['data_pagto'].max().reset_index()

# Renomear a coluna de data de pagamento para 'recencia'
recencia = recencia.rename(columns={'data_pagto': 'recencia'})

# Exibir o DataFrame de recência com as colunas solicitadas
print("DataFrame de recência:")
print(recencia)

# Salvar o arquivo com as datas de recência
caminho_saida = r'C:\Users\italo.marques\Desktop\Py\RFM_RECENCIA.csv'
recencia.to_csv(caminho_saida, index=False)
