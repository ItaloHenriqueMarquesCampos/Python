import pandas as pd

# Carregar o arquivo CSV
caminho_entrada = 'Files/MATRIZ_RFM.csv'
df_alunos = pd.read_csv(caminho_entrada)

# Verificar se as colunas necessárias existem no dataset
print("Colunas no arquivo CSV:", df_alunos.columns)

# Agrupar os dados pelo nome do aluno e contar a frequência de repetição (pagamentos)
frequencia = df_alunos.groupby(['cpf', 'nome', 'celular', 'endereco', 'uf']).size().reset_index(name='frequencia')

# Exibir o DataFrame de frequência com as colunas solicitadas
print("DataFrame de frequência:")
print(frequencia)

# Salvar o arquivo com as frequências
caminho_saida = r'C:\Users\italo.marques\Desktop\Py\RFM_FREQUENCIA.csv'
frequencia.to_csv(caminho_saida, index=False)
