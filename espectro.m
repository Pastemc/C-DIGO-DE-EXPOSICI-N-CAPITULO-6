% Cargar la imagen de la ciudad
imagen = imread('C:\Users\USER 2022\OneDrive\Escritorio\PDI\planeta.png'); % Asegúrate de tener la imagen en el mismo directorio o especifica la ruta completa

% Separar los canales RGB
canal_rojo = imagen(:,:,1);   % Canal rojo
canal_verde = imagen(:,:,2);  % Canal verde
canal_azul = imagen(:,:,3);   % Canal azul

% Binarizar los canales para obtener las áreas ocupadas por cada color
umbral = 100; % Ajusta este umbral según la intensidad de cada canal

% Crear máscaras binarias
mascara_rojo = canal_rojo > umbral;
mascara_verde = canal_verde > umbral;
mascara_azul = canal_azul > umbral;

% Aplicar efecto de nebulosa
nebulosa_roja = double(mascara_rojo) .* 255;  % Amplificar el canal rojo
nebulosa_verde = double(mascara_verde) .* 255;  % Amplificar el canal verde
nebulosa_azul = double(mascara_azul) .* 255;  % Amplificar el canal azul

% Mostrar resultados
figure;
subplot(2, 2, 1), imshow(imagen), title('Imagen original');
subplot(2, 2, 2), imshow(cat(3, nebulosa_roja, zeros(size(imagen, 1), size(imagen, 2)), zeros(size(imagen, 1), size(imagen, 2)))), title('roja');
subplot(2, 2, 3), imshow(cat(3, zeros(size(imagen, 1), size(imagen, 2)), nebulosa_verde, zeros(size(imagen, 1), size(imagen, 2)))), title('verde');
subplot(2, 2, 4), imshow(cat(3, zeros(size(imagen, 1), size(imagen, 2)), zeros(size(imagen, 1), size(imagen, 2)), nebulosa_azul)), title('azul');
