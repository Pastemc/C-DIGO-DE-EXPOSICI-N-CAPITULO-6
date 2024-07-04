% Cargar la imagen RGB
image = imread('C:\Users\USER 2022\OneDrive\Escritorio\PDI\añia2.jpg');

% Verificar el número de bandas en la imagen
[numRows, numCols, numBands] = size(image);

% Simular una banda NIR si la imagen no tiene cuatro bandas
if numBands < 8
    NIR_band = 0.299 * double(image(:,:,1)) + 0.587 * double(image(:,:,2)) + 0.114 * double(image(:,:,3));
    NIR_band = uint8(255 * mat2gray(NIR_band)); % Normalizar la banda NIR a 8 bits
    image = cat(3, image, NIR_band);
end

% Crear una figura con subplots
figure;

% Composición de Color Natural (RGB)
subplot(2, 2, 1);
natural_color = cat(3, image(:,:,1), image(:,:,2), image(:,:,3));
imshow(natural_color);
title('Composición de Color Natural');

% Composición de Color Falso 1 (NIR, Red, Green)
subplot(2, 2, 2);
false_color1 = cat(3, image(:,:,4), image(:,:,1), image(:,:,2)); % NIR -> R, Red -> G, Green -> B
imshow(false_color1);
title('Falso Color (NIR, Red, Green)');

% Composición de Color Falso 2 (NIR, Green, Blue)
subplot(2, 2, 3);
false_color2 = cat(3, image(:,:,4), image(:,:,2), image(:,:,3)); % NIR -> R, Green -> G, Blue -> B
imshow(false_color2);
title('Falso Color (NIR, Green, Blue)');

% Composición de Color Falso 3 (Red, NIR, Blue)
subplot(2, 2, 4);
false_color3 = cat(3, image(:,:,1), image(:,:,4), image(:,:,3)); % Red -> R, NIR -> G, Blue -> B
imshow(false_color3);
title('Falso Color (Red, NIR, Blue)');


