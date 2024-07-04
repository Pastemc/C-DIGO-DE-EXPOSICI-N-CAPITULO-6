% Asegúrate de especificar la ruta correcta a la imagen
imagenRGB = imread('C:\Users\USER 2022\OneDrive\Escritorio\PDI\raya.jpg'); % Reemplaza con la ruta completa

% Separa los canales rojo, verde y azul
canalRojo = imagenRGB(:, :, 1);
canalVerde = imagenRGB(:, :, 2);
canalAzul = imagenRGB(:, :, 3);

% Crear imágenes en color para cada canal
imagenRoja = cat(3, canalRojo, zeros(size(canalRojo), 'uint8'), zeros(size(canalRojo), 'uint8'));
imagenVerde = cat(3, zeros(size(canalVerde), 'uint8'), canalVerde, zeros(size(canalVerde), 'uint8'));
imagenAzul = cat(3, zeros(size(canalAzul), 'uint8'), zeros(size(canalAzul), 'uint8'), canalAzul);

% Muestra los canales por separado
figure;

subplot(2, 2, 1);
imshow(imagenRGB);
title('Imagen Original');

subplot(2, 2, 2);
imshow(imagenRoja);
title('Canal Rojo');

subplot(2, 2, 3);
imshow(imagenVerde);
title('Canal Verde');

subplot(2, 2, 4);
imshow(imagenAzul);
title('Canal Azul');


