img = im2double(imread("tissue.tif"));
shade = im2double(imread("shading.tif"));
new_img = img./shade;
subplot(131), imshow(img), subplot(132), imshow(shade), subplot(133), imshow(new_img);