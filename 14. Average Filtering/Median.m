img = imread('salt_pepper.tif');
%Adding noise to the image
imnoise(img, 'salt & pepper', 0.05);
%Adding noise is optional as there was already some salt & pepper noise in this image
img_median = medfilt2(img);
figure('Name', 'Original');
imshow(img);
figure('Name', 'Median Blur');
imshow(img_median);