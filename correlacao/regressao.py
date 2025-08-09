import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
# Aprendizado de máquina pip install scikit-learn
from sklearn.linear_model import LinearRegression

EXPOSICAO_ALGODAO = 'data\LungDisease.csv'
dataframe = pd.read_csv(EXPOSICAO_ALGODAO)
print(dataframe.head())

dataframe.plot.scatter(x = 'Exposure', y = 'PEFR')
plt.show()