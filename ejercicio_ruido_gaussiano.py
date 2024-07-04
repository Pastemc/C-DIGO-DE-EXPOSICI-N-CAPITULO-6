# Ejemplo de Añadir Ruido Gaussiano
import cv2
import numpy as np

# Leer la imagen
imagen_ruta = 'imagen.jpg'
image = cv2.imread(imagen_ruta)

# Parámetros del ruido gaussiano
mean = 0
std = 25

# Generar el ruido gaussiano
ruido_gaussiano = np.random.normal(mean, std, image.shape).astype(np.uint8)

# Añadir el ruido a la imagen
imagen_ruido = cv2.add(image, ruido_gaussiano)

# Guardar y mostrar la imagen con ruido
cv2.imwrite('imagen_gaussiano.jpg', imagen_ruido)
cv2.imshow('Imagen Ruido', imagen_ruido)
cv2.waitKey(0)
cv2.destroyAllWindows()
