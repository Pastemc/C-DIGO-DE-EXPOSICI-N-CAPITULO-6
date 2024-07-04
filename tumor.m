% Nombre del archivo de la imagen
filename = 'C:\Users\USER 2022\OneDrive\Escritorio\PDI\cerebro2.jpg';
%cerebro2.jpg
%tumor2.gif
%craneo2.jpg
%cerebro.jpeg

% Verificar si el archivo existe
if exist(filename, 'file') == 2
    % Cargar la imagen del Picker Thyroid Phantom
    phantom_image = imread(filename);

    % Convertir la imagen a escala de grises si es necesario
    if size(phantom_image, 3) == 3
        phantom_gray = rgb2gray(phantom_image);
    else
        phantom_gray = phantom_image;
    end

    % Realizar el corte de intensidad utilizando 8 colores
    phantom_indexed = imquantize(phantom_gray, multithresh(phantom_gray, 7));
    phantom_colored = label2rgb(phantom_indexed, jet(8), 'k', 'shuffle');

    % Crear la figura y los subplots
    figure;

    % Mostrar la imagen en escala de grises
    subplot(1, 2, 1);
    imshow(phantom_gray);
    title('Imagen Original');

    % Mostrar el resultado del corte de intensidad utilizando 8 colores
    subplot(1, 2, 2);
    imshow(phantom_colored);
    title('Corte de intensidad utilizando ocho colores');
else
    error('El archivo "%s" no existe. Verifica la ruta del archivo.', filename);
end

title('Corte de intensidad utilizando ocho colores');
