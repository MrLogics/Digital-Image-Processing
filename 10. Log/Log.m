img = imread('log.tif');
log_img = 0.1 * log(1 + double(img));
imshow(log_img);
log_img = 0.5 * log(1 + double(img));
imshow(log_img);
log_img = 0.05 * log(1 + double(img));
imshow(log_img);
figure;
imshow(img);
img = imread('gamma.tif')
new_img = imadjust(img, [], [], 3);
imshow(new_img);
figure;
imshow(img);
new_img = imadjust(img, [], [], 2);
imshow(new_img);