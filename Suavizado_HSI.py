#Ejemplo 4: Suavizado de Imagen en Espacio HSI
#Objetivo: Suavizar una imagen en el espacio HSI para reducir el ruido mientras se preservan los colores.
#Descripción: En este ejemplo, se muestra cómo suavizar una imagen en el espacio HSI. Para ello, se carga una imagen, se convierte al espacio de color HSI, se aplica un suavizado Gaussiano al componente de intensidad (V), se convierte de nuevo a RGB y se muestran la imagen original y la imagen suavizada.

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Paso 1: Cargar la imagen
img = cv2.imread('cara.jpg')

if img is None:
    print('Hubo un error al cargar la imagen')
else:
    print('La imagen se cargó exitosamente')

# Paso 2: Convertir la imagen al espacio de color HSI (HSV en OpenCV)
hsi = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

# Paso 3: Aplicar suavizado Gaussiano al componente de intensidad (V)
hsi[..., 2] = cv2.GaussianBlur(hsi[..., 2], (5, 5), 0)

# Paso 4: Convertir la imagen de nuevo a RGB
smoothed_rgb = cv2.cvtColor(hsi, cv2.COLOR_HSV2BGR)

# Paso 5: Mostrar las imágenes original y suavizada
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Imagen Original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(smoothed_rgb, cv2.COLOR_BGR2RGB))
plt.title('Imagen Suavizada')
plt.axis('off')

plt.show()