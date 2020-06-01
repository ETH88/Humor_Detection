# Humor Detection

Humor Detection Model - Senior Research Project at Clarabridge

Welcome to my Humor Detection GitHub! All the code you need to run a humor detection model is above. Follow a few simple instructions below, and you can run it and play around with it on your own computer!


# Pipeline Architecture/Senior Project Presentation

[Link to pipeline architecture](https://docs.google.com/presentation/d/1ovGGWBDW6Nw_IOQBciTxk3PVscZcIRLUf1f7ZEpDcZk/edit?usp=sharing)

[Link to 20 minute presentation of my Humor Detection project](https://www.youtube.com/watch?v=eiJ8as6wXRE)

[Link to my presentation](https://docs.google.com/presentation/d/1HfwDTGgdVPj8wd_e3G8CPgZqNBk8H3Hlw95FfidmcT0/edit?usp=sharing)


# Running the Code

Running the code above and testing my humor detection model is pretty simple. 
 
1. Click the "Clone or Download" green button on the top right. This will download the GitHub repository.
2. Open "main.py" in your preferred text editor. I highly recommend VSCode - you can install it here: https://code.visualstudio.com/download.
3. Type the code below into your terminal or VSCode. This will navigate you to the "Humor" directory, whether in your terminal or VSCode, using ls and cd commands.
```
cd Downloads
ls
cd Humor
```
4. Enter the virtual environment, which has many of the dependencies already installed, including Python and libraries like nltk, pandas, matplotlib, sklearn, numpy, etc., using the following code. You should see (venv) pop up on the left side if this is done correctly.
```
source venv/bin/activate
```
5. Once you are inside the virtual environment, there is one more step you must do before you can run my code. You must install fasttext. Follow the steps for installing fasttext on Fasttext's website: https://fasttext.cc/docs/en/support.html.
```
git clone https://github.com/facebookresearch/fastText.git
cd fastText
sudo pip3 install .
```
6. Now the code is ready to be run! Type the following command into VSCode or your terminal, and watch the model go to work!
```
python3 main.py
```
