import pandas as pd

# Carregar o arquivo CSV
caminho_entrada = 'Files/MATRIZ_RFM.csv'
df_alunos = pd.read_csv(caminho_entrada)

# Verificar as colunas do arquivo CSV
print("Colunas no arquivo CSV:", df_alunos.columns)

# Converter a coluna 'valor_pagto' para numérico, ignorando possíveis erros
df_alunos['valor_pagto'] = pd.to_numeric(df_alunos['valor_pagto'], errors='coerce')

# Agrupar os dados pelo CPF e nome do aluno, somando o valor dos pagamentos
valor_monetario = df_alunos.groupby(['cpf', 'nome', 'celular', 'cidade', 'uf'])['valor_pagto'].sum().reset_index()

# Renomear a coluna de valor monetário
valor_monetario = valor_monetario.rename(columns={'valor_pagto': 'valor_monetario'})

# Exibir o DataFrame de valor monetário para conferência
print("DataFrame de valor monetário:")
print(valor_monetario)

# Salvar o arquivo CSV com os resultados
caminho_saida = r'C:\Users\italo.marques\Desktop\Py\RFM_VALOR_MONETARIO.csv'
valor_monetario.to_csv(caminho_saida, index=False)
