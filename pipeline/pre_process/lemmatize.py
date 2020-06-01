import nltk
from utils import PreProcess
import os

class Lemmatize(PreProcess):
    """
    Pre-processing rule - lemmatizing
    """
    
    def __init__(self):
        self._enabled = False

    def __repr__(self):
        return self.__class__.__name__ #returns name of class

    def get_wordnet_pos(word: str):
        """Map POS tag to first character lemmatize() accepts"""
        from nltk.corpus import wordnet
        tag = nltk.pos_tag([word])[0][1][0].upper()
        tag_dict = {"J": wordnet.ADJ,
                    "N": wordnet.NOUN,
                    "V": wordnet.VERB,
                    "R": wordnet.ADV}

        return tag_dict.get(tag, wordnet.NOUN)

    def apply(self, data: list):
        nltk.download('averaged_perceptron_tagger')
        nltk.download('punkt')
        nltk.download('wordnet')
        from nltk.stem import WordNetLemmatizer 

        # 1. Init Lemmatizer
        lemmatizer = WordNetLemmatizer()
        
        for i in range(len(data)):
            review = [lemmatizer.lemmatize(word, Lemmatize.get_wordnet_pos(word)) for word in nltk.word_tokenize(data[i][1]) if not word == ""] #lemmatizes everything based on part-of-speech if word is not empty str
            data[i][1] = ' '.join(review)
    
        ##make sure humorwords are lemmmatized##
        humorwords = []
        with open(f'{os.getcwd()}/data/humorwords.txt', 'r') as humor_file: #reading humor words
            humorwords = humor_file.read().split(", ") 

        for index, word in enumerate(humorwords):
            humorwords[index] = lemmatizer.lemmatize(word, Lemmatize.get_wordnet_pos(word))
        
        with open(f'{os.getcwd()}/data/humorwords_lemmatized.txt', 'w') as humor_file:
            for word in humorwords:
                humor_file.write('%s, ' % word)

        ##make sure nothumorwords are stemmed##
        nothumorwords = []
        with open(f'{os.getcwd()}/data/nothumorwords.txt', 'r') as nothumor_file: #reading nothumor words
            nothumorwords = nothumor_file.read().split(", ") 

        for index, word in enumerate(nothumorwords):
            nothumorwords[index] = lemmatizer.lemmatize(word, Lemmatize.get_wordnet_pos(word))
        
        with open(f'{os.getcwd()}/data/nothumorwords_lemmatized.txt', 'w') as nothumor_file: 
            for word in nothumorwords:
                nothumor_file.write('%s, ' % word)
        
        #print('lemmatized data: ', data)
        return {'data': data}