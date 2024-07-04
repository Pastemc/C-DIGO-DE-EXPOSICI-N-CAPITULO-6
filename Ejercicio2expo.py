2) #Ejercicio 2
import cv2
import numpy as np

def rgb_to_cmyk(image):
    # Escalamos los valores de los píxeles de 0 a 1
    image = image.astype(np.float32) / 255.0
    
    # Extraemos los canales RGB
    r, g, b = image[:,:,0], image[:,:,1], image[:,:,2]
    
    # Calculamos los canales CMYK
    k = 1 - np.max(image, axis=2)
    c = (1 - r - k) / (1 - k)
    m = (1 - g - k) / (1 - k)
    y = (1 - b - k) / (1 - k)
    
    # Ajustamos para valores fuera del rango [0, 1]
    c[c < 0] = 0
    m[m < 0] = 0
    y[y < 0] = 0
    k[k < 0] = 0
    
    # Convertimos de vuelta a valores de 0 a 255
    c = (c * 255).astype(np.uint8)
    m = (m * 255).astype(np.uint8)
    y = (y * 255).astype(np.uint8)
    k = (k * 255).astype(np.uint8)
    
    # Devolvemos la imagen CMYK
    return cv2.merge((c, m, y, k))

# Cargar imagen RGB
image_rgb = cv2.imread(r'C:\Users\Alberd\Pictures\Mario.png')

# Convertir a CMYK
image_cmyk = rgb_to_cmyk(image_rgb)

# Mostrar y guardar la imagen CMYK (opcional)
cv2.imshow('CMYK Image', image_cmyk)
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite('imagen_cmyk.jpg', image_cmyk)