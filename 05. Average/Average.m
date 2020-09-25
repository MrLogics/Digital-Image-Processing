img = imread("Galaxy.tif");
img = im2double(img);
sum = zeros(size(img));
mean = 0;
sigma = 0.1;
for i = 1:100
	noise = normrnd(mean, sigma, size(img));
	noise = img + noise;
	sum = sum + noise;
end
avg = sum/i;
subplot(131), Imshow(img), subplot(132), imshow(noise), subplot(133), imshow(avg);
	
