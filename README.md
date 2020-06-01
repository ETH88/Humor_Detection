# Humor Detection

Humor Detection Model - Senior Research Project at Clarabridge

Welcome to my Humor Detection GitHub! All the code you need to run a humor detection model is above. Follow a few simple instructions below, and you can run it and play around with it on your own computer!


# Pipeline Architecture/Senior Project Presentation

[Link to pipeline architecture](https://docs.google.com/presentation/d/1ovGGWBDW6Nw_IOQBciTxk3PVscZcIRLUf1f7ZEpDcZk/edit?usp=sharing)

[Link to 20 minute presentation of my Humor Detection project](https://www.youtube.com/watch?v=eiJ8as6wXRE)

[Link to my presentation](https://docs.google.com/presentation/d/1HfwDTGgdVPj8wd_e3G8CPgZqNBk8H3Hlw95FfidmcT0/edit?usp=sharing)


# Running the Code

Follow the steps below to run the code above and test my humor detection model!
 
1. Click the "Clone or Download" green button on the top right, then click "Download ZIP." This will download the GitHub repository.
2. Open the terminal (for Mac: Applications --> Utilities --> Terminal)
3. Type the code below into your terminal. If my code has successfully finished downloading into your Downloads folder, this will navigate you to the correct directory.
```
cd Downloads/Humor_Detection-master
```
4. Create a virtual environment, which will be a separate place where all the dependencies can be installed:
```
python3 -m venv venv
```
5. Enter the virtual environment you just created. After typing the following command, you should see "(venv)" pop up on the left side of the terminal.
```
source venv/bin/activate
```
6. Install the dependencies for this project by typing the following command into the terminal. This should take around five minutes.
```
pip3 install nltk pandas matplotlib sklearn
```
7. Install fasttext. Follow the commands for installing fasttext (they can also be found on Fasttext's website: https://fasttext.cc/docs/en/support.html):
```
git clone https://github.com/facebookresearch/fastText.git
cd fastText
sudo pip3 install .
cd ..
```
6. Now the code is ready to be run! Type the following command into your terminal, and watch the model go to work!
```
python3 main.py
```

# Playing Around with the Code

Open "main.py" in your preferred text editor. I highly recommend VSCode - you can install it here: https://code.visualstudio.com/download.
