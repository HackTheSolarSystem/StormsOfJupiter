p = 1;

for imageN = 2:1401
    name = ['Image',num2str(imageN),'.jpg'];
    %normImage = im2double(name);
    I = imread(name);%I = imread('~/Desktop/StormsOf/Jupiter/Image%.jpg');
    %I =
    %Im = imadjust(I);
    data(p,:) = reshape(I,1,256*256);
    %data(p,:) = I;
    p = p + 1;

end
