# Ejemplo 1: Transformación de RGB a CMYK
# Objetivo: Convertir una imagen del espacio de color RGB al espacio de color CMYK, que es comúnmente utilizado en la impresión.
# Descripción: En este ejemplo, se muestra cómo convertir una imagen del espacio de color RGB al espacio de color CMYK. Para ello, se carga una imagen, se normaliza a flotante, se calculan los componentes C (Cyan), M (Magenta), Y (Yellow) y K (Black) y se fusionan en una imagen CMYK. Finalmente, se muestran la imagen original y la imagen en CMYK.

import cv2
import numpy as np
import matplotlib.pyplot as plt

# Paso 1: Cargar la imagen
img = cv2.imread('familia.png')

if img is None:
    print('Hubo un error al cargar la imagen')
else:
    print('La imagen se cargó exitosamente')

# Paso 2: Convertir a flotante y normalizar
bgr = img.astype(float) / 255.0

# Paso 3: Calcular el componente K (Negro)
K = 1 - np.max(bgr, axis=2)

# Paso 4: Calcular los componentes C (Cian), M (Magenta) y Y (Amarillo)
C = (1 - bgr[..., 2] - K) / (1 - K + 1e-6)
M = (1 - bgr[..., 1] - K) / (1 - K + 1e-6)
Y = (1 - bgr[..., 0] - K) / (1 - K + 1e-6)

# Paso 5: Convertir los componentes de nuevo a escala de 0-255
C = (C * 255).astype(np.uint8)
M = (M * 255).astype(np.uint8)
Y = (Y * 255).astype(np.uint8)
K = (K * 255).astype(np.uint8)

# Paso 6: Fusionar los componentes en una imagen CMYK
cmyk_img = cv2.merge([C, M, Y, K])

# Paso 7: Mostrar las imágenes originales y en CMYK
plt.subplot(1, 2, 1)
plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.title('Imagen Original')
plt.axis('off')

plt.subplot(1, 2, 2)
plt.imshow(cv2.cvtColor(cmyk_img, cv2.COLOR_BGR2RGB))
plt.title('Imagen en CMYK')
plt.axis('off')

plt.show()