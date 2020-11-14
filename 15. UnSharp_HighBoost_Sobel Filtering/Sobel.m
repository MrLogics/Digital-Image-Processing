x = fspecial('sobel');
y = x';
img = imread('house.tif');
imgx = imfilter(img, x);
imgy = imfilter(img, y);
x1 = double(imgx);
y1 = double(imgy);
z = sqrt(x1.*x1 + y1.*y1);
z=uint8(z);

figure('Name', 'Original');
imshow(img);
figure('Name', 'Horizontal');
imshow(imgx);
figure('Name', 'Vertical');
imshow(imgy);
figure('Name', 'Sobel');
imshow(z);

%Comparision with Laplacian Filter
lap = fspecial('laplacian');
imglap = imfilter(img, lap);
figure('Name', 'Laplacian Filter');
imshow(imglap, []);
