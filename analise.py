import pandas as pd
import numpy as np
import seaborn as sns

df = pd.read_csv('C:\\Users\\yurif\\OneDrive\\Área de Trabalho\\Git Folders\\Projeto_SCTEC\\query_01.csv')

df.info()
print(df.head())

print(df.groupby(['SALARY', 'DEPARTMENT_NAME']).size())