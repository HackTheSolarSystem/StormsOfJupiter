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

1. Rebecca set up the neural net cluster a (GAN) and is working on a pipeline to feed the images into the cluster to train the model. This neural net will be able to **generate images to fill gaps within the sequence**, meaning if we take an image at _t=0_ and _t=1m_, we could provide an image for _t=0.5m_. The stretch goal is to then have the neural net provide the n+1 image.

2. Victoria worked on another neural net (RNN with a LSTM twist) which will train on the behavior of the storm given the LBL files and predict the path of the storms and other characteristics.

#### Further Development
- Identify chemical composition of the different strata
- Write a script to convert IMG format to PNG

### Installation Instructions

You must list by name all software packages, APIs, frameworks, databases, or any other tools or libraries you used.

You must also provide any step-by-step instructions for installation of your solution.
* Step one - install package manager
* Step two - special config instructions
* Step three - system administration notes
* Step four - command line how-to, listing descriptions of all optional arguments
