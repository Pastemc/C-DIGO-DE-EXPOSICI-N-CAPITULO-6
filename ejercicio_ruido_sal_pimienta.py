#Ejemplo de Añadir Ruido Sal y Pimienta
import cv2
import numpy as np

# Leer la imagen
imagen_ruta = 'imagen.jpg'
image = cv2.imread(imagen_ruta)

# Parámetros del ruido sal y pimienta
sal_prob = 0.05
pimienta_prob = 0.05

# Copiar la imagen original
ruido_imagen = np.copy(image)

# Añadir ruido de sal
num_salt = np.ceil(sal_prob * image.size)
coords = [np.random.randint(0, i, int(num_salt)) for i in image.shape]
ruido_imagen[coords[0], coords[1], :] = 255

# Añadir ruido de pimienta
numero = np.ceil(pimienta_prob * image.size)
coords = [np.random.randint(0, i, int(numero)) for i in image.shape]
ruido_imagen[coords[0], coords[1], :] = 0

# Guardar y mostrar la imagen con ruido
cv2.imwrite('noisy_image_salt_and_pepper.jpg', ruido_imagen)
cv2.imshow('Noisy Image', ruido_imagen)
cv2.waitKey(0)
cv2.destroyAllWindows()
