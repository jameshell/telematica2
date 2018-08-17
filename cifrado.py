import numpy as np
import matplotlib.pyplot as plt
from collections import Counter
with	open('textoprueba.txt',	'r')	as	archivo:
				datosleidos=archivo.read().replace('\n',	'')
print ("DATOS LEIDOS:")
print	(datosleidos)
boriginal=list("abcdefghijklmnopqrstuvwxyz	.,!0123456789ABCDEFGHIJLMNOPQRSTUVWXYZ")
#bcifrada = list("defghijklmnopqrstuvwxyzabc	.,!0123456789DEFGHIJLMNOPQRSTUVWXYZABC") PUNTO 3 (SOLO LETRAS)
#bcifrada=list ("ijklmnopqrstuvwxyz	.,!0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefgh") PUNTO 2
car=list(datosleidos)
cifrado=""
descifrado=""
print("----------------------------------------------------------------------------------------------------------------")
print("CIFRADO:")
for	i in	range(len(car)):
    for	posicion,	item	in	enumerate(boriginal):
        if	car[i]==item:
            cifrado+=bcifrada[posicion]

print	(cifrado)

print("---------------------------------------------------------------------------------------------------------------")
print("DESCIFRADO:")
for	i	in	range(len(car)):
    for	posicion,	item	in	enumerate(bcifrada):
        if	car[i]==item:
            descifrado+=bcifrada[posicion]
print	(descifrado)

ejercicio2 = cifrado.replace('\n',	'')
letras_histograma = Counter(ejercicio2.lower().replace('\n', ''))
contador = letras_histograma.values()
letras = letras_histograma.keys()
bar_x_locations = np.arange(len(contador))
plt.bar(bar_x_locations, contador, align='center')
plt.xticks(bar_x_locations, letras)
plt.grid()
plt.show()
archivo.close()
