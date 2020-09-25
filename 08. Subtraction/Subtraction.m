img = im2double(imread("Angio.tif"));
shade = im2double(imread("Mask.tif"));
new_img = img.-shade;
subplot(131), imshow(img), subplot(132), imshow(shade), subplot(133), imshow(new_img);