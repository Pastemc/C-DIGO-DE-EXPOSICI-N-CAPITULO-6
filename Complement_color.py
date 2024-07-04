#Ejemplo 3: Complemento de Color
#Objetivo: Obtener el complemento de color de una imagen, útil para resaltar detalles.
#Descripción: En este ejemplo, se muestra la imagen original y la imagen con el complemento de color.

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Paso 1: Cargar la imagen
imagen = cv2.imread('image.jpg')

if imagen is None:
    print('Hubo un error al cargar la imagen')
else:
    print('La imagen se cargó exitosamente')

# Paso 2: Calcular el complemento de color
complemento = 255 - imagen

# Paso 3: Mostrar las imágenes original y con complemento
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(imagen, cv2.COLOR_BGR2RGB))
plt.title('Imagen Original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(complemento, cv2.COLOR_BGR2RGB))
plt.title('Complemento de Color')
plt.axis('off')

plt.show()
