img = imread("cameraman.tif");
[m, n] = size(img);
new = zeros(m,n);
for i = 1:m
    for j = 1:n
        if img(i,j)>128
            new(i,j)=255;
        else
            new(i,j)=0;
        end
    end
end

subplot(1,2,1),imshow(img),subplot(1,2,2),imshow(new)