p = 1;

for imageN = 0:120
    name = ['Image',num2str(imageN),'.jpg'];
    I1=imread(name);
    I2 = imresize(I1,[84 84]); 
    %In=rgb2gray(I2); % use if the image containing RGB value 3
    %figure;imshow(In);
    %imwrite(In,name) ;
    %name = ['Image',num2str(imageN),'.jpg'];
    %I1=imread(name);
    %I2 = imresize(I1,[84 84]); 
       % Get the number of rows and columns, 
% and, most importantly, the number of color channels.
    [rows, columns, numberOfColorChannels] = size(I2);
    	if numberOfColorChannels > 1
    % It's a true color RGB image.  We need to convert to gray scale.
        In = rgb2gray(I2);
    else
    % It's already gray scale.  No need to convert.
        In = I2;
    end
    %In=rgb2gray(I2); % use if the image containing RGB value 3
    %figure;imshow(In);
    imwrite(In,name) ;
end 
