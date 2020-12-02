function out = butterWorthLowpass(img, d, x)
	[m, n] = size(img);
	[p, q] = meshgrid(-floor(m/2):floor((m-1)/2), -floor(n/2):floor((n-1)/2));
	D = sqrt(p.^2 + q.^2);
	out = 1./(1+(D./d).^(2*x));
end