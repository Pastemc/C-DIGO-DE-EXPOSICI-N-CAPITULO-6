# Ejemplo de Compresión con Pérdida (JPEG)

from PIL import Image
import cv2

# Leer imagen
imagen_ruta = 'imagen.jpg'
imagen = Image.open(imagen_ruta)

# Guardar imagen con compresión JPEG
compresion_imagen = 'prueba.jpg'
imagen.save(compresion_imagen, 'JPEG', quality=85)  # calidad puede ser ajustada del (1-100)

# Mostrar imagen comprimida
imagen_comprimida = cv2.imread(compresion_imagen)
cv2.imshow('Imagen Comprimida', imagen_comprimida)
cv2.waitKey(0)
cv2.destroyAllWindows()
