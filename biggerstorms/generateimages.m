p = 1;

for imageN = 0:120
    name = ['Image',num2str(imageN),'.jpg'];
    %normImage = im2double(name);
    I = imread(name);%I = imread('~/Desktop/StormsOf/Jupiter/Image%.jpg');
    %I =
    %Im = imadjust(I);
    data(p,:) = reshape(I,1,84*84);
    %data(p,:) = I;
    p = p + 1;
    csvwrite('images.csv',data)

end
