import nltk
from utils import PreProcess
import os

class Stem(PreProcess):
    """
    Pre-processing rule - stemming
    """
    def __init__(self):
        self._enabled = False

    def __repr__(self):
        return self.__class__.__name__ #returns name of class

    def apply(self, data: list):
        from nltk.stem import PorterStemmer

        ps = PorterStemmer()
        for i in range(len(data)):
            words = data[i][1].split(" ")
            review  = []
            for word in words:
                if not word == "":
                    review.append(ps.stem(word)) #stems word if it is not empty string
            review = ' '.join(review)
            data[i][1] = review

        ##make sure humorwords are stemmed##
        humorwords = []
        with open(f'{os.getcwd()}/data/humorwords.txt', 'r') as humor_file: #reading humor words
            humorwords = humor_file.read().split(", ") 

        for index, word in enumerate(humorwords):
            humorwords[index] = ps.stem(word)
        
        with open(f'{os.getcwd()}/data/humorwords_stemmed.txt', 'w') as humor_file: #reading humor words
            for word in humorwords:
                humor_file.write('%s, ' % word)

        ##make sure nothumorwords are stemmed##
        nothumorwords = []
        with open(f'{os.getcwd()}/data/nothumorwords.txt', 'r') as nothumor_file: #reading humor words
            nothumorwords = nothumor_file.read().split(", ") 

        for index, word in enumerate(nothumorwords):
            nothumorwords[index] = ps.stem(word)
        
        with open(f'{os.getcwd()}/data/nothumorwords_stemmed.txt', 'w') as nothumor_file: #reading humor words
            for word in nothumorwords:
                nothumor_file.write('%s, ' % word)

        if 'show_effect' in self._metadata.keys():
            if self._metadata['show_effect'] == True:
                print ('stemmed data: ', data[0][1])
                
        return {'data': data}