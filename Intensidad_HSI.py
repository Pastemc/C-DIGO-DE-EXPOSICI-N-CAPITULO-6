#Ajuste de Intensidad en el Espacio HSI
#Objetivo: Ajustar la intensidad de una imagen en el espacio HSI (Hue, Saturation, Intensity).
#Descripción: En este ejemplo, se muestra cómo ajustar la intensidad de una imagen en el espacio HSI. Para ello, se carga una imagen, se convierte al espacio de color HSI, se ajusta la intensidad multiplicándola por un factor (0.7 en este caso), se asegura de que los valores estén en el rango [0, 255] y se convierte de nuevo a RGB. Finalmente, se muestran la imagen original y la imagen con la intensidad ajustada.

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Paso 1: Cargar la imagen
img = cv2.imread('fisi.jpg')

if img is None:
    print('Hubo un error al cargar la imagen')
else:
    print('La imagen se cargó exitosamente')

# Paso 2: Convertir la imagen al espacio de color HSI (HSV en OpenCV)
hsi = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype(float)

# Paso 3: Ajustar la intensidad multiplicándola por un factor (0.7 en este caso)
hsi[..., 2] *= 0.7

# Paso 4: Asegurarse de que los valores estén en el rango [0, 255] y convertir a enteros
hsi = np.clip(hsi, 0, 255).astype(np.uint8)

# Paso 5: Convertir la imagen de nuevo a RGB
adjusted_rgb = cv2.cvtColor(hsi, cv2.COLOR_HSV2BGR)

# Paso 6: Mostrar las imágenes original y ajustada
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Imagen Original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(adjusted_rgb, cv2.COLOR_BGR2RGB))
plt.title('Intensidad Ajustada')
plt.axis('off')

plt.show()
