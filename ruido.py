import cv2
import matplotlib.pyplot as plt

# Cargar la imagen
image = cv2.imread('ruido.png')
if image is None:
    print("No se pudo cargar la imagen")
    exit()
# Convertir la imagen de BGR a RGB
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
# Aplicar el filtro gaussiano para reducir el ruido
gaussian_blurred = cv2.GaussianBlur(image_rgb, (7, 7), 1.5)
# Aplicar el filtro bilateral para preservar bordes y reducir más el ruido
bilateral_filtered = cv2.bilateralFilter(gaussian_blurred, 9, 75, 75)
# Mostrar la imagen original y la filtrada
titles = ['Original', 'Sin ruido']
images = [image_rgb, bilateral_filtered]
plt.figure(figsize=(12, 6))
for i in range(2):
    plt.subplot(1, 2, i+1)
    plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
