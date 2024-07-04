% Cargar la imagen RGB
image = imread('C:\Users\USER 2022\OneDrive\Escritorio\PDI\ciudad.jpg');

% Asumimos que la imagen tiene tres bandas.
% R = image(:,:,1)
% G = image(:,:,2)
% B = image(:,:,3)

% Crear una figura con subplots
figure;

% Composición de Color Natural
subplot(2, 2, 1);
natural_color = cat(3, image(:,:,1), image(:,:,2), image(:,:,3));
imshow(natural_color);
title('Imagen Original');

% Composición de Color Falso 1 (intercambiar R y B)
subplot(2, 2, 2);
false_color1 = cat(3, image(:,:,3), image(:,:,2), image(:,:,1)); % B -> R, G -> G, R -> B
imshow(false_color1);
title('Blue');

% Composición de Color Falso 2 (intercambiar R y G)
subplot(2, 2, 3);
false_color2 = cat(3, image(:,:,2), image(:,:,1), image(:,:,3)); % G -> R, R -> G, B -> B
imshow(false_color2);
title('Green');

% Composición de Color Falso 3 (intercambiar G y B)
subplot(2, 2, 4);
false_color3 = cat(3, image(:,:,1), image(:,:,3), image(:,:,2)); % R -> R, B -> G, G -> B
imshow(false_color3);
title('Red');
