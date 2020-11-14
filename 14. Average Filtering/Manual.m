img = imread('a.tif');
%Manual Average Filter with low values
h = ones(5, 5)/25;
img_manual = imfilter(img, h);
%Manual Average Filter with high values
h = ones(15, 15)/225;
img_manual2 = imfilter(img, h);
figure('Name', 'Original');
imshow(img);
figure('Name', 'Manual Average Blur1');
imshow(img_manual);
figure('Name', 'Manual Average Blur2');
imshow(img_manual2);