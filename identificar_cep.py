# pip install pandas requests
# Crie um arquivo CSV com a primeira coluna preenchida de CEP e vazio nas demais colunas.
# Serão identificados os endereços e gerado um novo arquivo

import pandas as pd
import requests
import time

# Caminho do arquivo CSV com a coluna de CEP
entrada = r"C:\Users\Pichau\Desktop\Arquivos PY\Gerador\ceps.csv"
saida = r"C:\Users\Pichau\Desktop\Arquivos PY\Gerador\resultado_ceps.csv"

# Lê o arquivo (tenta , e ;)
try:
    df = pd.read_csv(entrada)
except:
    df = pd.read_csv(entrada, delimiter=';')

print("Colunas encontradas:", df.columns.tolist())

# Normaliza nomes das colunas (remove espaços e deixa minúsculo)
df.columns = df.columns.str.strip().str.lower()

# Tenta achar automaticamente a coluna que contém CEP
possiveis_nomes = ["cep", "ceps", "codigo postal", "código postal"]

coluna_cep = None
for col in df.columns:
    if any(nome in col for nome in possiveis_nomes):
        coluna_cep = col
        break

if not coluna_cep:
    raise Exception("❌ Nenhuma coluna com CEP encontrada no arquivo!")

print(f"✔ Coluna de CEP identificada: {coluna_cep}")

# Limpa o CEP
df[coluna_cep] = df[coluna_cep].astype(str).str.replace(r"\D", "", regex=True)

# Função para consultar ViaCEP
def consultar_cep(cep):
    try:
        url = f"https://viacep.com.br/ws/{cep}/json/"
        response = requests.get(url, timeout=10)

        if response.status_code == 200:
            dados = response.json()

            if "erro" in dados:
                return None

            return {
                "cep": cep,
                "logradouro": dados.get("logradouro", ""),
                "numero": "",
                "complemento": dados.get("complemento", ""),
                "bairro": dados.get("bairro", ""),
                "cidade": dados.get("localidade", ""),
                "estado": dados.get("uf", "")
            }
    except:
        return None

# Lista de resultados
resultados = []

print("\nConsultando CEPs...\n")

for cep in df[coluna_cep]:
    dados = consultar_cep(cep)
    if dados:
        resultados.append(dados)
    else:
        resultados.append({
            "cep": cep,
            "logradouro": "",
            "numero": "",
            "complemento": "",
            "bairro": "",
            "cidade": "",
            "estado": ""
        })

    time.sleep(0.3)

# Converte em DataFrame
df_resultado = pd.DataFrame(resultados)

# Salva CSV
df_resultado.to_csv(saida, index=False, encoding="utf-8-sig")

print("✔ Arquivo gerado com sucesso!")
print(f"📁 Local: {saida}")
