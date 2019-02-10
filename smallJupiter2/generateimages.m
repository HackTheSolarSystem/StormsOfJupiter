p = 1;

for imageN = 1:61
    name = ['Image',num2str(imageN),'.jpg'];
    %normImage = im2double(name);
    I = imread(name);%I = imread('~/Developer/hack-the-solar-system/HubbleJupiter/Image%.jpg');
    %I =
    %Im = imadjust(I);
    data(p,:) = reshape(I,1,28*28);
    %data(p,:) = I;
    p = p + 1;
    csvwrite('images.csv',data)

end
