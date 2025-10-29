import pandas as pd
import locale

# Definir o locale para o Brasil para formatação de moeda
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Carregar o arquivo CSV
caminho_entrada = 'Files/MATRIZ_RFM.csv'
df_alunos = pd.read_csv(caminho_entrada)

# Verificar as colunas do arquivo CSV
print("Colunas no arquivo CSV:", df_alunos.columns)

# --- FREQUÊNCIA (Quantidade de compras com parcela igual a 1) ---
# Filtrar as compras onde 'parcela' é igual a 1
df_compras = df_alunos[df_alunos['parcela'] == 1]

# Agrupar os dados pelo CPF e contar a frequência de compras onde parcela é igual a 1
frequencia = df_compras.groupby(['cpf', 'nome', 'celular', 'cidade', 'uf','email','sexo','nascimento']).size().reset_index(name='frequencia')

# --- MONETÁRIO (Valor total pago) ---
# Converter a coluna 'valor_pagto' para numérico, ignorando possíveis erros
df_alunos['valor_pagto'] = pd.to_numeric(df_alunos['valor_pagto'], errors='coerce')

# Somar o valor total pago
valor_monetario = df_alunos.groupby(['cpf', 'nome', 'celular', 'cidade', 'uf'])['valor_pagto'].sum().reset_index()

# Renomear a coluna de valor monetário
valor_monetario = valor_monetario.rename(columns={'valor_pagto': 'valor_monetario'})

# Formatar os valores como moeda brasileira
valor_monetario['valor_monetario'] = valor_monetario['valor_monetario'].apply(lambda x: locale.currency(x, grouping=True))

# --- RECÊNCIA (Data da última compra com parcela igual a 1) ---
# Converter a coluna 'data_pagto' para datetime
df_compras['data_pagto'] = pd.to_datetime(df_compras['data_pagto'], errors='coerce')

# Agrupar os dados por CPF e pegar a data da compra mais recente (último curso comprado onde parcela == 1)
recencia = df_compras.groupby(['cpf', 'nome', 'celular', 'cidade', 'uf'])['data_pagto'].max().reset_index()

# Renomear a coluna de data de pagamento para 'recencia'
recencia = recencia.rename(columns={'data_pagto': 'recencia'})

# --- Unir os dados de Frequência, Monetário e Recência ---
# Unir os DataFrames de frequencia, valor_monetario e recencia
rfm = pd.merge(frequencia, valor_monetario, on=['cpf', 'nome', 'celular', 'cidade', 'uf'])
rfm = pd.merge(rfm, recencia, on=['cpf', 'nome', 'celular', 'cidade', 'uf'])

# Exibir o DataFrame final de RFM
print("DataFrame RFM final:")
print(rfm)

# Salvar o arquivo CSV com os resultados de RFM
caminho_saida = r'C:\Users\italo.marques\Desktop\Py\RFM_FINAL.csv'
rfm.to_csv(caminho_saida, index=False)
