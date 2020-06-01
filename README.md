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

4. Check if you have python3 installed on your computer. Type the command:
```
which python3
```
   If something like "/usr/bin/python3" is returned, python3 has been installed and you can skip this step. If not, download the latest version of python3 at python's official website: https://www.python.org/downloads/.

5. Create a virtual environment, which will be a separate place where all the dependencies can be installed. On macOS and Linux, type the following command:
```
python3 -m venv venv
```
  On Windows, type the following command instead:
```
py -m venv venv
```

6. Enter the virtual environment you just created. On macOS and Linux, type the following command.
```
source venv/bin/activate
```
   On Windows, type the following command instead: 
```
.\venv\Scripts\activate
```
You should see "(venv)" pop up on the left side of the terminal. To confirm the virtual environment works, on macOS and Linus type the following command, and the path returned should look like ".../venv/bin/python3", NOT "usr/bin/python3":
```
which python3
```
   On Windows:
```
where python3
```

7. Install the dependencies for this project by typing the following command into the terminal. This should take around five minutes. If the pop-up window "The 'gcc' command requires the command line developer tools" appears when you run the following command, click "Install."
```
pip3 install nltk pandas matplotlib sklearn
```

8. Install fasttext. Follow the commands for installing fasttext (they can also be found on Fasttext's website: https://fasttext.cc/docs/en/support.html). The third line has the command "sudo," so after you type the third command into the terminal, you will have to enter the password you use to login to your computer.
```
git clone https://github.com/facebookresearch/fastText.git
cd fastText
sudo pip3 install .
cd ..
```

9. Now the code is ready to be run! Type the following command into your terminal, and watch the Fasttext model go to work!
```
python3 main.py
```

# Playing Around with the Code

If you want to play around with the hyperparameters, enable/disable preprocessing stages/rules/postprocessing stages, or even create your own or test out different datasets and combination of rules, I highly recommend downloading the text editor VSCode - you can install it here: https://code.visualstudio.com/download.
The main code I recommend playing around with is "main.py," which contains the "config" dictionary, where all the properties and metadata are specified.
