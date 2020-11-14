img = imread('cameraman.tif');
f2 = fftshift(fft2(img));
figure;
imshow(0.5*log(1+abs(f2)), []);
x = 3;
d = 15;
[m, n] = size(img);
[p, q] = meshgrid(-floor(m/2):floor((m-1)/2), -floor(n/2):floor((n-1)/2));
D = sqrt(p.^2 + q.^2);
C = 1./(1+(D./d).^(2*x));
hp = f2.*C;
hpi = ifft2(ifftshift(hp));
f = abs(hpi);
fm = max(f(:));
figure;
imshow(f/fm, []);