import nltk
from utils import PreProcess

class Remove_Stopwords(PreProcess):
    """
    Pre-processing rule - remove stop words
    """
    def __init__(self):
        self._enabled = False

    def __repr__(self):
        return self.__class__.__name__ #returns name of class

    def apply(self, data: list):
        nltk.download('stopwords')
        from nltk.corpus import stopwords
        
        for i in range(len(data)):
            review = [word for word in data[i][1].split(" ") if not word in set(stopwords.words('english')) and not word == ""] #everythings thats not empty string or stopword
            review = ' '.join(review) #makes it a str
            data[i][1] = review

        if 'show_effect' in self._metadata.keys():
            if self._metadata['show_effect'] == True:
                print ('data with stopwords removed: ', data)

        return {'data': data}
    