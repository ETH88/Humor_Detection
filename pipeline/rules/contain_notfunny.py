from utils import Rule
import os

class Contain_NotFunny(Rule):
    """
    2nd rule - contains notfunny word?
    """
    def __init__(self):
        self._enabled = False
        self._weight = 0
        self._metadata = {}
    
    def __repr__(self):
        return self.__class__.__name__ 

    def execute(self, s):
        data = s._data
        rawdata = s._rawdata
        preprocess = s._preprocess

        nothumorwords = []
        stem = False
        lemmatize = False
        for stage in preprocess:
            if stage._enabled:
                if stage.__class__.__name__ == 'Stem':
                    stem = True
                elif stage.__class__.__name__ == 'Lemmatize':
                    lemmatize = True
        
        nothumorwords_file = f'{os.getcwd()}/data/nothumorwords' #make sure humorwords is stemmed/lemmatized/nothing
        if stem:
            nothumorwords_file += '_stemmed'
        elif lemmatize:
            nothumorwords_file += '_lemmatized'

        #print(nothumorwords_file)

        with open(f'{nothumorwords_file}.txt', 'r') as nothumor_file: #reading humor words
            nothumorwords = nothumor_file.read().split(", ") 

        while("" in nothumorwords): #remove empty str
            nothumorwords.remove("") 

        pred = []
        for i in range(len(data)):
            notfunny = False
            words = data[i][1].split(" ")
            for word in words:
                if word in nothumorwords and not words == "" and not notfunny: #if there's a notfunny word for the first time
                    #print(word)
                    pred.append(0) #0 = not funny
                    notfunny = True
            if not notfunny:
                pred.append(1)   #1 = funny
        
        return pred