import pandas as pd
import numpy as np
import math

def analisar_dados_estatisticos(dados_brutos, nome_do_conjunto):
    print(f"--- Análise Estatística para: {nome_do_conjunto} ---")

    #1. Rol (Dados Ordenados)
    rol = sorted(dados_brutos)
    print("\n1. Rol (Dados Ordenados):")
    print(f" {rol}")

    #2. Tamanho da amostra (n)
    n = len(rol)
    print("\n2. Tamanho da Amostra (n):")
    print(f" n = {n}")

    #3. Valor máximo e mínimo
    x_min = rol[0]
    x_max = rol[-1]
    print("\n3. Valor máximo e mínimo:")
    print(f" valor min: {x_min}")
    print(f" valor máx: {x_max}")

    # 4. Amplitude total (AT)
    at = x_max - x_min
    print("\n4. Amplitude Total: (AT): ")
    print(f" AT = {at:.2f}")

    # 5. Número de Classes (K)
    k = math.ceil(math.sqrt(n))
    print("\n5. Número de Classes (K):")
    print(f" K = {k}")

    # 6. Amplitude de Classes (h)
    h = at / k
    print("\n6. Amplitude de Classes (h):")
    print(f" h = {h}")

    classes = []
    frequencias_absolutas = []
    pontos_medios = []
    frequencias_relativas_dec = []
    frequencias_relativas_dec_perc = []
    frequencias_absolutas_acum = []

    frequencia_abs_acum = 0
    limite_inferior = x_min
    for i in range(k): # k = 5 (número de classes)
        limite_superior = limite_inferior + h # h = 2
        # Classes
        classes.append(f"[{limite_inferior} |-- {limite_superior}]")
        # Frequência Absoluta
        frequencia_absoluta = len([x for x in rol if limite_inferior <= x < limite_superior])
        frequencias_absolutas.append(frequencia_absoluta)
        # Ponto médio da classe
        pontos_medios.append((limite_inferior + limite_superior) / 2)
        # Relativa Decimal
        frequencias_relativas_dec.append(frequencias_absolutas[i] / n)
        # Relativa Absoluta Acumulada
        frequencia_abs_acum = frequencia_abs_acum + frequencias_absolutas[i]
        frequencias_absolutas_acum.append(frequencia_abs_acum)
        # Relativa Percentual
        frequencias_relativas_dec_perc.append(frequencias_relativas_dec[i] * 100)
        limite_inferior = limite_superior

    df_frequencia = pd.DataFrame({
        'Classe': classes,
        'Ponto Médio': pontos_medios,
        'Frequência Absoluta': frequencias_absolutas,
        'Frequência Relativa Decimal': frequencias_relativas_dec,
        'Frequência Relativa Percentual (%)': frequencias_relativas_dec_perc,
        'Frequência Absoluta Acumulada': frequencias_absolutas_acum
    })

    df_frequencia.loc['Total'] = [
        'Total',
        np.nan,
        df_frequencia['Frequência Absoluta'].sum(),
        df_frequencia['Frequência Relativa Decimal'].sum(),
        df_frequencia['Frequência Relativa Percentual (%)'].sum(),
        np.nan
    ]
    return df_frequencia




    # print("\n6. Amplitude de Classes (h):")
    # print(f" h = {h}")
    # # Arredondar amplitude das classes
    # num_casas_decimais = 0
    # if at < k: # 0.1
    #     num_casas_decimais = 1
    #     if at * 10 < k: # 0.01
    #         num_casas_decimais = 2
    # h = np.ceil(h * (10**num_casas_decimais)) / (10**num_casas_decimais)
    
    # print("\n6. Amplitude de Classes (h):")
    # print(f" h = {int(h)}")

# ---- Estudo de caso 01: Idade dos alunos
dados_idades = [21, 21, 21, 22, 22, 22, 23, 23, 23, 23, 24, 24, 25, 25, 25, 26, 27, 27, 28, 28, 30, 30, 31, 31, 31]
def_idades = analisar_dados_estatisticos(dados_idades, "Idade dos alunos")
print(def_idades.to_string())