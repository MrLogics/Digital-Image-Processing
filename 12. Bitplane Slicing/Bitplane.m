img = imread("bitplane.tif");
i1 = bitget(img, 1);
i2 = bitget(img, 2);
i3 = bitget(img, 3);
i4 = bitget(img, 4);
i5 = bitget(img, 5);
i6 = bitget(img, 6);
i7 = bitget(img, 7);
i8 = bitget(img, 8);
imshow(i1);
imshow(i1*255);
imshow(i5*255);
imshow(i6*255);
imshow(i7*255);
imshow(i8*255);
new = i8*128 + i7*64 + i6*32;
imshow(img);
figure;
imshow(new);