# This code will extract the length of the DoGs from a file and make a box-plot

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

dogs_file = r"C:\Users\Paco\Desktop\Pan_ARTDeco_ensGene\analisis_casero_de_expresion_diferencial\RPKM_THZ1yDMSO.txt"

with open(dogs_file, "r") as dogs:
    dogs_length = []
    dogs.readline()
    for dog in dogs:
        dlength = (int(dog.strip().split("\t")[1]))/1000
        dogs_length.append(dlength)

c = 0
for i in dogs_length:
    if i >= 3.999 and i <= 5.000:
        c += 1
print(c)
maximo = np.max(dogs_length)
minimo = np.min(dogs_length)
mediana = np.median(dogs_length)
promedio = np.mean(dogs_length)
print(maximo,minimo,mediana,promedio)

# Crear un boxplot con Seaborn
sns.set(style="whitegrid")  # Establece el estilo de la cuadrícula
plt.figure(figsize=(8, 6))  # Tamaño del gráfico

# Utiliza la función boxplot de Seaborn
sns.boxplot(y=dogs_length)

# Personaliza el eje y
plt.ylim(0, 90)  # Establece los límites en el eje y (ajusta según tus datos)
plt.yticks(np.arange(0, 91, 10))  # Establece los valores de los ticks en el eje y (ajusta según tus datos)

# Personaliza el gráfico (opcional)
plt.title('DoGs length in pancreatic cancer cells with THZ1')
plt.ylabel('Length (KB)')
plt.xlabel(f'n={len(dogs_length)}')
plt.grid(axis='y')  # Agrega una cuadrícula en el eje y

# Mostrar el gráfico
plt.show()
