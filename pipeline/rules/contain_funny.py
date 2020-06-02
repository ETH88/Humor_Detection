from utils import Rule, Pipeline

import os

class Contain_Funny(Rule): 
    """
    1st rule - contains funny word?
    """
    def __init__(self):
        self._enabled = False
        self._weight = 0
        self._metadata = {}

    def __repr__(self):
        return self.__class__.__name__ #returns name of class

    def execute(self, s):
        data = s._data
        rawdata = s._rawdata
        preprocess = s._preprocess

        humorwords = []
        humorphrases = []

        if self._metadata['humorwords']:
            stem = False
            lemmatize = False
            for stage in preprocess:
                if stage._enabled:
                    if stage.__class__.__name__ == 'Stem':
                        stem = True
                    elif stage.__class__.__name__ == 'Lemmatize':
                        lemmatize = True
            
            humorwords_file = 'data/humorwords' #make sure humorwords is stemmed/lemmatized/nothing
            if stem:
                humorwords_file += '_stemmed'
            elif lemmatize:
                humorwords_file += '_lemmatized'
        
            #print(humorwords_file)
            
            with open(f'{humorwords_file}.txt', 'r') as humor_file: #reading humor words
                humorwords = humor_file.read().split(", ") 

            while("" in humorwords): #remove empty str
                humorwords.remove("") 
        
        if self._metadata['humorphrases']['enabled']:
            humorphrases = []
            if self._metadata['humorphrases']['strict']:
                with open('data/humorphrases.txt', 'r') as humor_file:
                    for line in humor_file:
                        humorphrases.append(line[:-1])
            else:
                with open('data/humorphrasesextra.txt', 'r') as humor_file:
                    for line in humor_file:
                        humorphrases.append(line[:-1])

        rawdata = [row[1] for row in rawdata] #only essential preprocessing, so phrases preserved

        pred = [] #
        for i in range(len(data)):
            words = data[i][1].split(" ")
            funny = False
            
            if self._metadata['humorwords']:
                for word in words:
                    if word in humorwords and not words == "" and not funny: #if there's a funny word for first time
                        if 'show_humorword_or_humorphrase' in self._metadata.keys():
                            if self._metadata['show_humorword_or_humorphrase'] == True:
                                print('funny word:', word)
                        pred.append(1)
                        funny = True
            
            if self._metadata['humorphrases']['enabled']:
                if not funny: #no funny word
                    for phrase in humorphrases:
                        if phrase in rawdata[i] and not funny:
                            if 'show_humorword_or_humorphrase' in self._metadata.keys():
                                if self._metadata['show_humorword_or_humorphrase'] == True:
                                    print('funny phrase: ', phrase)
                            
                            pred.append(1)
                            funny = True
            
            if not funny: #no funny word or phrase
                pred.append(0) #0 = not funny
        
        return pred