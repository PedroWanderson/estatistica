import pandas as pd
from faker import Faker # pip install faker
import random

fake = Faker('en_US')
# fake = Faker('pt_BR')

# Função para gerar o dataframe
def gerar_dados_brutos(num_registros):
    dados_brutos = []
    lista_cidades = set() #SET não deixa se repetir registros iguais diferente do array ou do list

    while len(dados_brutos) < num_registros:
        nome_cidade = fake.city()
        if nome_cidade not in lista_cidades:
            lista_cidades.add(nome_cidade)
            # gerar populacao aleatória entre 10k e 5mi
            populacao = fake.random_int(min=10000, max=5000000)
            # gerar taxa de homicídios entre 1.0 e 15.0 arredondado e com uma casa decimal
            taxa_homocidios = round(random.uniform(1.0, 15.0), 1)
            dados_brutos.append({
                "Cidade": nome_cidade,
                "Populacao": populacao,
                "Taxa homicidios": taxa_homocidios
            })
    return pd.DataFrame(dados_brutos)



num_registros = 10
df = gerar_dados_brutos(num_registros)
# Exibir o data frame
print("DataFrame gerado:")
print(df)

output_csv_file = "taxa_homicidios.csv"
df.to_csv(output_csv_file, index=False)