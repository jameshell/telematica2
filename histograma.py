import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
frasedeprueba = """Este es un texto de prueba para hacer un histograma. """
with open('textoprueba.txt', 'r') as archivo:
 datosleidos=archivo.read().replace('\n', '')
print (datosleidos)
# generar histograma
#letras_histograma = Counter(frasedeprueba.lower().replace('\n', ''))
letras_histograma = Counter(datosleidos.lower().replace('\n', ''))
contador = letras_histograma.values()
letras = letras_histograma.keys()
print (contador)
print (letras)
# graficar
bar_x_locations = np.arange(len(contador))
plt.bar(bar_x_locations, contador, align = 'center')
plt.xticks(bar_x_locations, letras)
plt.grid()
plt.show()
archivo.close()
#Origen del codigo: http://codereview.stackexchange.com/questions/129412/histogram-of-a-string
