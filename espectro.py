import cv2
import numpy as np
import matplotlib.pyplot as plt

# Función para leer y normalizar una banda
def read_and_normalize_band(image_data, band_index):
    band = image_data[:, :, band_index].astype(np.float32)
    band_normalized = cv2.normalize(band, None, 0.0, 1.0, cv2.NORM_MINMAX)
    return band_normalized

# Cargar la imagen multiespectral con la ruta completa
image_path = r'planeta.png'
image_data = cv2.imread(image_path, cv2.IMREAD_UNCHANGED)

# Asumimos que la imagen multiespectral tiene al menos 4 bandas
red_band = read_and_normalize_band(image_data, 0)   # Banda roja (asignada al canal rojo en RGB)
green_band = read_and_normalize_band(image_data, 1) # Banda verde (asignada al canal verde en RGB)
blue_band = read_and_normalize_band(image_data, 2)  # Banda azul (asignada al canal azul en RGB)
nir_band = read_and_normalize_band(image_data, 3)   # Banda infrarroja cercana (asignada al canal rojo en RGB)

# Crear una cuadrícula de subplots para mostrar las bandas y las combinaciones
fig, axes = plt.subplots(2, 2, figsize=(10, 10))

# Mostrar las bandas individuales con sus respectivos colores
axes[0, 0].imshow(red_band, cmap='Reds')
axes[0, 0].set_title('Banda Roja')
axes[0, 0].axis('off')

axes[0, 1].imshow(green_band, cmap='Greens')
axes[0, 1].set_title('Banda Verde')
axes[0, 1].axis('off')

axes[1, 0].imshow(blue_band, cmap='Blues')
axes[1, 0].set_title('Banda Azul')
axes[1, 0].axis('off')

axes[1, 1].imshow(nir_band, cmap='Purples')
axes[1, 1].set_title('Banda Infrarroja Cercana (NIR)')
axes[1, 1].axis('off')

# Añadir los títulos y mostrar la figura
plt.suptitle('Visualización de Bandas Multiespectrales con Colores Respectivos', fontsize=16)
plt.tight_layout()
plt.show()
