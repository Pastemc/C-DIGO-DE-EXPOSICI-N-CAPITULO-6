% Nombre del archivo de la imagen de rayos X de una soldadura
filename = 'C:\Users\USER 2022\OneDrive\Escritorio\PDI\diente3.jpg';

if exist(filename, 'file') == 2
    % Cargar la imagen de rayos X de la soldadura
    soldadura_image = imread(filename);

    % Convertir la imagen a escala de grises si es necesario
    if size(soldadura_image, 3) == 3
        soldadura_gray = rgb2gray(soldadura_image);
    else
        soldadura_gray = soldadura_image;
    end

    % Mejorar el contraste de la imagen utilizando histogram equalization
    soldadura_gray_enhanced = histeq(soldadura_gray);

    % Aplicar un filtro de realce de la imagen
    soldadura_gray_enhanced = imsharpen(soldadura_gray_enhanced);

    % Realizar el corte de intensidad utilizando 8 colores
    % Obtener umbrales para dividir la imagen en 8 niveles
    thresholds = multithresh(soldadura_gray_enhanced, 5);
    % Quantizar la imagen basada en los umbrales
    soldadura_indexed = imquantize(soldadura_gray_enhanced, thresholds);
    % Convertir la imagen quantizada a una imagen colorida
    soldadura_colored = label2rgb(soldadura_indexed, jet(8), 'k', 'shuffle');

    % Crear la figura y los subplots
    figure;

    % Mostrar la imagen en escala de grises original
    subplot(1, 2, 1);
    imshow(soldadura_gray);
    title('Imagen Original en Escala de Grises');

    % Mostrar el resultado del corte de intensidad utilizando 8 colores
    subplot(1, 2, 2);
    imshow(soldadura_colored);
    title('Imagen Codificada por Colores');

else
    error('El archivo "%s" no existe. Verifica la ruta del archivo.', filename);
end


