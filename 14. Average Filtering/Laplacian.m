img = imread('moon.tif');
lap = fspecial('laplacian');
img_lap = imfilter(img, lap);
figure('Name', 'Original');
imshow(img);
figure('Name', 'Laplacian Blur');
imshow(img_lap, []);
figure('Name', 'Sharp');
imshow(img - img_lap);