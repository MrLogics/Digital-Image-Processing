img = imread('pollen.tif');
imhist(img);
new = histeq(img);
imshow(img);
figrue;
imshow(new);
figrue;
imhist(new);
figrue;
imhist(img);