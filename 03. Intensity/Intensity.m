img = imread("skull.tif");
x1=8;
x2=4;
x3=2;

step1=ceil(255/(x1-1));
step2=ceil(255/(x2-1));
step3=ceil(255/(x3-1));

new_img1 = ceil(img/step1)*step1;
new_img2 = ceil(img/step2)*step2;
new_img2 = ceil(img/step3)*step3;

subplot(221), imshow(img), title("256 Levels"), subplot(222), imshow(new_img1), title("8 Levels"), subplot(223), imshow(new_img2), title("4 Levels"), subplot(224), imshow(new_img3), title("2 Levels");