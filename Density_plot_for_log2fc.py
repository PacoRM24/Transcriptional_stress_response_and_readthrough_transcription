# This code will create a two density plots using the expression levels of the DoGs in different conditions

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Cargar el archivo CSV en un DataFrame
data_TPL = pd.read_csv(r"C:\Users\Paco\Desktop\Pan_ARTDeco_ensGene\analisis_casero_de_expresion_diferencial\Matriz_de_expresion_TPLyDMSO.txt", sep="\t", index_col=0)
data_THZ1 = pd.read_csv(r"C:\Users\Paco\Desktop\Pan_ARTDeco_ensGene\analisis_casero_de_expresion_diferencial\Matriz_de_expresion_THZ1yDMSO.txt", sep="\t", index_col=0)

# Extraer los nombres de las condiciones ('DMSOR' y 'TPLR')
conditions_TPL = ['DMSO', 'TPL']
conditions_THZ1 = ['DMSO', 'THZ1']

# Crear un DataFrame para almacenar los promedios de cada condición
data_combined_TPL = pd.DataFrame()
data_combined_THZ1 = pd.DataFrame()

# Calcular el promedio de las réplicas para cada condición
for condition in conditions_TPL:
    condition_columns = [col for col in data_TPL.columns if condition in col]
    data_combined_TPL[condition] = data_TPL[condition_columns].mean(axis=1)

for condition2 in conditions_THZ1:
    condition_columns = [col for col in data_THZ1.columns if condition2 in col]
    data_combined_THZ1[condition2] = data_THZ1[condition_columns].mean(axis=1)

# Calcular el log2 del fold change y agregarlo como una columna tomando en cuenta un valor para ajustar los valores iguales a cero
adj_value = 0.001
data_combined_TPL['TPLvsDMSO'] = np.log2((data_combined_TPL["TPL"] + adj_value) / (data_combined_TPL["DMSO"] + adj_value))
data_combined_THZ1['THZ1vsDMSO'] = np.log2((data_combined_THZ1["THZ1"] + adj_value) / (data_combined_THZ1["DMSO"] + adj_value))


# Crear un density plot para comparar las distribuciones de las dos condiciones
sns.set(style="white")  # Estilo del gráfico
plt.figure(figsize=(10, 6))  # Tamaño del gráfico

# Crear el density plot para la condición 'DMSO'
sns.kdeplot(data_combined_TPL['TPLvsDMSO'], label='TPLvsDMSO', fill=True, color='orange')

# Crear el density plot para la condición 'TPL' en un color diferente
sns.kdeplot(data_combined_THZ1['THZ1vsDMSO'], label='THZ1vsDMSO', fill=True, color='purple')

# Agregar etiquetas al gráfico
plt.xlabel('Log2 Fold Change')
plt.ylabel('Density')

# Agregar una leyenda
plt.legend()

# Mostrar el gráfico
plt.show()