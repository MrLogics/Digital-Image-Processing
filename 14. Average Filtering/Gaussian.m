img = imread('a.tif');
gaus = fspecial('gaussian', 7, 5);
img_gaussian = imfilter(img, gaus);
figure('Name', 'Original');
imshow(img);
figure('Name', 'Gaussian Blur');
imshow(img_gaussian);