# This code will create a two density plots using the expression levels of the DoGs in different conditions

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Cargar el archivo CSV en un DataFrame
data = pd.read_csv(r"C:\Users\Paco\Desktop\Pan_ARTDeco_ensGene\analisis_casero_de_expresion_diferencial\Matriz_de_expresion_THZ1yDMSO.txt", sep="\t", index_col=0)

# Extraer los nombres de las condiciones ('DMSOR' y 'TPLR')
conditions = ['DMSO', 'THZ1']

# Crear un DataFrame para almacenar los promedios de cada condición
data_combined = pd.DataFrame()

# Calcular el promedio de las réplicas para cada condición
for condition in conditions:
    condition_columns = [col for col in data.columns if condition in col]
    data_combined[condition] = data[condition_columns].mean(axis=1)

# Calcular el log1 de plegamiento entre las condiciones
data_log = np.log1p(data_combined)

# Crear un density plot para comparar las distribuciones de las dos condiciones
sns.set(style="white")  # Estilo del gráfico
plt.figure(figsize=(10, 6))  # Tamaño del gráfico

# Crear el density plot para la condición 'DMSO'
sns.kdeplot(data_log['DMSO'], label='DMSO', fill=True, color='blue')

# Crear el density plot para la condición 'TPL' en un color diferente
sns.kdeplot(data_log['THZ1'], label='THZ1', fill=True, color='red')

# Agregar etiquetas al gráfico
plt.xlabel('Ln(RPKM+1)')
plt.ylabel('Density')

# Agregar una leyenda
plt.legend()

# Mostrar el gráfico
plt.show()