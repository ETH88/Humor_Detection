from utils import Rule
import os

class Contain_Funny_Negator(Rule):
    """
    3rd rule - contains funny word? + negator?
    """
    def __init__(self):
        self._enabled = False
        self._weight = 0
        self._metadata = {}
    
    def __repr__(self):
        return self.__class__.__name__ 

    def execute(self, s):
        rawdata = s._rawdata
        pred = s._pred

        pred = pred['Contain_Funny'][:]

        with open(f'{os.getcwd()}/data/negators.txt', 'r') as negators_file:
            negators = negators_file.read().split(" ")
        
        for i in range(len(rawdata)):
            words = rawdata[i][1].split(" ")
            for word in words:
                if not words == "" and word in negators and pred[i]==1: #if there's a negator
                    pred[i] = 0
                    
        return pred