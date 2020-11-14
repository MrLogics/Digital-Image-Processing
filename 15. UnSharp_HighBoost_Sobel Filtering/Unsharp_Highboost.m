img = imread('DIP.tif');
h = fspecial('gaussian', 7, 5);
blur = imfilter(img, h);
mask = img - blur;
unsh = img + mask;
hb = img + 3*mask;

figure('Name', 'Original');
imshow(img);
figure('Name', 'Blur');
imshow(blur);
figure('Name', 'Mask');
imshow(mask);
figure('Name', 'Unsharp Filter');
imshow(unsh);
figure('Name', 'High-boost Filter');
imshow(hb);


