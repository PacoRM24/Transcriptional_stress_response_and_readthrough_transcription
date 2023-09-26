# This code will extract the length of the DoGs from a file and make a box-plot

import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# Save the file that has the length of the DoGs at a variable
dogs_file = #Put here the path from the file

# Open the file and iterate through it to extract the lengths from the file
with open(dogs_file, "r") as dogs:
    dogs_length = []
    dogs.readline()
    for dog in dogs:
        dlength = (int(dog.strip().split("\t")[1]))/1000
        dogs_length.append(dlength)

# Count how may DoGs have a length between 3999 and 5000
c = 0
for i in dogs_length:
    if i >= 3.999 and i <= 5.000:
        c += 1
print(c)

# Imprimir los valores máximo, mínimo, mediana y el promedio
maximo = np.max(dogs_length)
minimo = np.min(dogs_length)
mediana = np.median(dogs_length)
promedio = np.mean(dogs_length)
print(maximo,minimo,mediana,promedio)

# Use seaborn to create the box-plot
sns.set(style="whitegrid")  # Graph style
plt.figure(figsize=(8, 6))  # Graph size
sns.boxplot(y=dogs_length)

# Personalize y axix
plt.ylim(0, 90)  # Establish the y axis limits
plt.yticks(np.arange(0, 91, 10))  # Establish the values for y axis ticks

# Personalize the graph
plt.title('DoGs length in pancreatic cancer cells with THZ1') # Add a tittle
plt.ylabel('Length (KB)') # Add y axis label
plt.xlabel(f'n={len(dogs_length)}') #Add x axis label
plt.grid(axis='y')  

# Show the graph
plt.show()
