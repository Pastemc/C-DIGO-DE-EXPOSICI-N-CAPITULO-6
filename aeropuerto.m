% Lee la imagen en escala de grises
grayImage = imread('C:\Users\USER 2022\OneDrive\Escritorio\PDI\añia.jpg');

% Verifica si la imagen es en escala de grises
if size(grayImage, 3) == 3
    grayImage = rgb2gray(grayImage);
end

% Aplica la transformación de pseudocolor
% Puedes usar la función ind2rgb con un mapa de colores predefinido
colormapName = 'jet'; % Puedes cambiar a otros como 'hsv', 'hot', 'parula', etc.
coloredImage = ind2rgb(gray2ind(grayImage, 256), colormap(colormapName));

% Muestra la imagen original y la imagen con pseudocolor
figure;
subplot(1, 2, 1);
imshow(grayImage);
title('Imagen en Escala de Grises');

subplot(1, 2, 2);
imshow(coloredImage);
title(['Imagen con Pseudocolor (' colormapName ')']);




