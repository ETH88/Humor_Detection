# Humor Detection

Humor Detection Model - Senior Research Project at Clarabridge

Welcome to my Humor Detection GitHub! All the code you need to run a humor detection model is above. Follow a few simple instructions below, and you can run it and play around with it on your own computer!


# Pipeline Architecture/Senior Project Presentation

[Link to pipeline architecture](https://docs.google.com/presentation/d/1ovGGWBDW6Nw_IOQBciTxk3PVscZcIRLUf1f7ZEpDcZk/edit?usp=sharing)

[Link to 20 minute presentation of my Humor Detection project](https://www.youtube.com/watch?v=eiJ8as6wXRE)

[Link to my powerpoint presentation](https://docs.google.com/presentation/d/1HfwDTGgdVPj8wd_e3G8CPgZqNBk8H3Hlw95FfidmcT0/edit?usp=sharing)

[Link to my senior project blog] (https://mclean.basisindependent.com/author/ethanh/?_ga=2.150583678.995056995.1591321133-237266007.1582138476)


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
pip install --upgrade pip
pip3 install nltk pandas matplotlib sklearn
```

8. Install fasttext. Follow the commands for installing fasttext by typing the following commands one at a time (they can also be found on Fasttext's website: https://fasttext.cc/docs/en/support.html). The third line has the command "sudo," so after you type the third command into the terminal, you will have to enter the password you use to login to your computer.
```
git clone https://github.com/facebookresearch/fastText.git
cd fastText
sudo pip3 install .
cd ..
```

9. Download a pre-trained randomforest and fasttext model. These were too big to put in this GitHub, but they can be found here: https://drive.google.com/file/d/1ejE6XG0fnM5gFODRRah8wUPsdhgMAmID/view?usp=sharing. Download the zip file and use the pre-trained models by replacing the "randomforest" folder inside the zip file with the "randomforest" folder inside the "Humor_Detection-master" directory. Also replace the "fasttext" folder inside the zip file with the "fasttext" folder inside the "Humor_Detection-master" directory.

10. Now the code is ready to be run! Type the following command into your terminal, and now you can type in any sentence you want, and my program will output if it thinks it is funny or not (1 - funny, 0 - not funny)!
```
python3 main.py
```

# Playing Around with the Code

If you want to play around with the hyperparameters, enable/disable preprocessing stages/rules/postprocessing stages, or even create your own or test out different datasets and combination of rules, I highly recommend downloading the text editor VSCode - you can install it here: https://code.visualstudio.com/download.

The main code I recommend playing around with is "main.py," which contains the "config" dictionary, where all the properties and metadata are specified. Take note of all the comments, especially ones labeled "IMPORTANT". 

After playing around with interactive mode, I highly recommend switching modes. This can easily be done in "main.py" by setting "interactive mode" to False. If you are not in interactive mode, there are some things you must change for the model to work well. Under 'postprocess' and 'report', I recommend setting "metrics" to ['accuracy', 'precision', 'recall', 'f1', 'cm'] and "return_pred" to False. In addition, turn all "show_effect" for the preprocessing stages to False, and set 'show_humorword_or_humorphrase' under 'r1' to False as well. For a faster runtime, I recommend setting "enabled" to False for all preprocessing stages, including "remove_stopwords" and "lemmatize."

After changing these variables, run "python3 main.py" again and watch my model go to work and return the results of my rules being tested on 80,000 labeled sentences in "testingdata_copy.txt".

You can also play around with the weights (how much each rule is taken into consideration) by changing what "weight" is equal to for each enabled rule. If you want to save the results or the confusion matrices, set "save" to True in "postprocessing". In addition, feel free to disable/enable any pre-processing stage/rule/post-processing stage you want to see what effect they have on the model's performance.

The last thing I recommend doing is training your own Fasttext model (Random Forest takes too long). To train your own Fasttext model, enable the "train_fasttext" preprocessing stage by setting "enabled" to True for that stage. Do not change "test_size," but feel free to adjust and tune the other hyperparameters, including learning rate (between 0 and 1), number of epochs (number of generations it trains), and wordNgrams (right now set to 2, so model takes into account phrases of length 2 - increasing wordNgrams increases context window but may lead to overfitting and a drop in performance). You MUST change "datafile" to "traintest.txt." When training a new fasttext model, I recommend setting "enabled" to False for all other rules. You must set "enabled" to False for 'r1'. Lastly, comment out line 122 in "main.py" by adding a # in front - commenting this out makes sure the results returned are from the fasttext model you just trained, not a pretrained fasttext model. Then run the program with "python3 main.py" and watch the magic of Fasttext training.

Feel free to ask me if you are unable to run my code or if you come across any issues. My email is ethanbmode@gmail.com. Have fun!
