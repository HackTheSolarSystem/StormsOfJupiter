## Storms of Jupiter

### Addressing [Storms of Jupiter](https://github.com/amnh/HackTheSolarSystem/wiki/The-Storms-of-Jupiter)

### Created by Storms of Jupiter
* Joseph Spens [@josephspens](https://github.com/josephspens)
* Rebecca D'Agostino [@rd16395p](https://github.com/rd16395p)
* Russell Brown [@cmonkey03](https://github.com/cmonkey03)
* Rachel Cohen [@rachelfreya](https://github.com/rachelfreya)
* Mallory Feuer [@mfeuer23](https://github.com/mfeuer23)
* Victoria Levchenko [@vlevchenko](https://github.com/vlevchenko)

### Solution Description

The goal of our project is to **train a neural net on a sequence of raw Juno images to then generate the n+1 image in that sequence**.

1. Rebecca set up the neural network (GAN) and is working on a pipeline to feed the images into the cluster to train the model. This neural network will be able to **generate images to fill gaps within the sequence**, meaning if we take an image at _t=0_ and _t=1m_, we could provide an image for _a random point in the time series_. The stretch goal is to then have the neural net provide the n+1 image via using a CNN as a secondary classifier, or exploring other options as seen in publications. Along with this, we can try to measure where the location of the storms are to place it in the time line.

Thank you to this helpful post - https://medium.com/datadriveninvestor/generative-adversarial-network-gan-using-keras-ce1c05cfdfd3   

2. Victoria worked on another neural net (RNN with a LSTM twist) which will train on the behavior of the storm given the LBL files and predict the path of the storms and other characteristics.

#### Further Development
- Identify chemical composition of the different strata
- Write a script to convert IMG format to PNG

### File Structure and Description
enviroment.yml - creates the enviroment for anaconda 
rename.py - Renames the images in order to be read by the matlab files later.  
cnn.py - Mock example of a CNN that could be used with the GAN in future studies.  
gan.py - Basic structure and example of the GAN used in this project.  
README.md  
/smalljupiter - the first GAN created, generates images that (28*28) are supposed to be mimicking images found on the juno site of Jupiter.  
/smalljupiter - the second GAN created, generates images that (28*28) are supposed to be mimicking images from Hubble Telescope and images of Jupiter, found here https://tools.pds-rings.seti.org/opus/#/view=search&browse=gallery&colls_browse=gallery&page=1&gallery_data_viewer=true&limit=100&order=time1&cols=opusid,instrument,planet,target,time1,observationduration&widgets=planet,target&widgets2=&detail=  
/biggerstorms - the third GAN created, generates images that (84*84) are supposed to mimicking a single band of a storm found within a gif.  

All of the GAN folders have the same files to create the .csv and train them;  
Images must be labeled Image0-N in order for them to work, which rename.py is programmed to do.  
resize.m - Resizes images to the correct shape and converts them to grayscale.  
generateimages.m - Generates the .csv called 'images.csv' for use with the GAN.  
gan.py - Takes the generated .csv and outputs .png files every 20 epochs.  

### Installation Instructions

You must list by name all software packages, APIs, frameworks, databases, or any other tools or libraries you used.

You must also provide any step-by-step instructions for installation of your solution.  
* Step one - install package manager  
Anaconda is used to handle the python packages and run the python scripts.
Matlab is used to run the matlab scripts. Matlab needs to license to run that can either be recieved through purchase or a trial.    
* Step two - special config instructions  
conda env create -f environment.yml  once anaconda is installed, within the anaconda prompt/command line/terminal.   
* Step three - system administration notes
* Step four - command line how-to, listing descriptions of all optional arguments  
1. run rename.py.
2. run resize.m  
3. run generateimages.m  
4. gan.py  
