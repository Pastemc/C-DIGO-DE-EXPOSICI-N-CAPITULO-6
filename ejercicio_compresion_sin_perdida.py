#Ejemplo de Compresión sin Pérdida (PNG)

from PIL import Image
import cv2

# Leer imagen
imagen_ruta = 'imagen.jpg'
image = Image.open(imagen_ruta)

# Guardar imagen con compresión PNG
imagen_comprimida_ruta = 'prueba2.png'
image.save(imagen_comprimida_ruta, 'PNG', optimize=True)

# Mostrar imagen comprimida
imagen_comprimida = cv2.imread(imagen_comprimida_ruta)
cv2.imshow('Imagen Comprimida', imagen_comprimida)
cv2.waitKey(0)
cv2.destroyAllWindows()