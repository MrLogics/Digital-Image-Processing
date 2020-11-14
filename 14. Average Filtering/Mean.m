img = imread('a.tif');
avg = fspecial('average', 15);
img_mean = imfilter(img, avg);
figure('Name', 'Original');
imshow(img);
figure('Name', 'Mean Blur');
imshow(img_mean);