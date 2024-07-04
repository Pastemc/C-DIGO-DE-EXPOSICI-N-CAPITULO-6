% Asegúrate de especificar la ruta correcta a la imagen multiespectral
imagenMultiespectral = imread('C:\Users\USER 2022\OneDrive\Escritorio\PDI\salas3.jpg'); % Reemplaza con la ruta completa

% Verifica el tamaño de la imagen
[filas, columnas, numCanales] = size(imagenMultiespectral);

% Si la imagen no tiene 4 canales, simula un canal IR
if numCanales < 4
    % Simula el canal IR como el promedio de los canales RGB si no está presente
    canalIR = uint8(mean(imagenMultiespectral, 3));
else
    % Si tiene 4 canales, separa el canal IR
    canalIR = imagenMultiespectral(:, :, 4);
end

% Separa los canales rojo, verde y azul
canalRojo = imagenMultiespectral(:, :, 1);
canalVerde = imagenMultiespectral(:, :, 2);
canalAzul = imagenMultiespectral(:, :, 3);

% Crear una imagen compuesta en color natural (RGB)
compuestaRGB = cat(3, canalRojo, canalVerde, canalAzul);

% Mejorar la imagen compuesta en color natural con estiramiento de contraste
compuestaRGB_contrast = imadjust(compuestaRGB, stretchlim(compuestaRGB), []);

% Mejorar la imagen compuesta en color natural con estiramiento de decorrelación
compuestaRGB_decor = decorrstretch(compuestaRGB);

% Crear una imagen compuesta en falso color usando IR, R y G
compuestaFalsoColor = cat(3, canalIR, canalRojo, canalVerde);

% Mejorar la imagen compuesta en falso color con estiramiento de contraste
compuestaFalsoColor_contrast = imadjust(compuestaFalsoColor, stretchlim(compuestaFalsoColor), []);

% Mejorar la imagen compuesta en falso color con estiramiento de decorrelación
compuestaFalsoColor_decor = decorrstretch(compuestaFalsoColor);

% Muestra las imágenes
figure;

subplot(3, 2, 1);
imshow(compuestaRGB);
title('Compuesta Natural Original (RGB)');

subplot(3, 2, 2);
imshow(compuestaRGB_contrast);
title('Compuesta Natural con Estiramiento de Contraste');

subplot(3, 2, 3);
imshow(compuestaRGB_decor);
title('Compuesta Natural con Estiramiento de Decorrelación');

subplot(3, 2, 4);
imshow(compuestaFalsoColor);
title('Compuesta Falso Color Original (IR, R, G)');

subplot(3, 2, 5);
imshow(compuestaFalsoColor_contrast);
title('Compuesta Falso Color con Estiramiento de Contraste');

subplot(3, 2, 6);
imshow(compuestaFalsoColor_decor);
title('Compuesta Falso Color con Estiramiento de Decorrelación');
