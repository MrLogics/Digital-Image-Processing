img = imread('galaxy.tif');
avg = fspecial('average', 15);
new = imfilter(img, avg);
figure1;
imshow(new);
new_th = im2bw(new, 0, 2);
figure2;
imshow(new_th);