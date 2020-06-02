from utils import PostProcess
import pandas as pd
import os
import matplotlib.pyplot as plt
import numpy as np
#import requests

class Report(PostProcess): 
    """
    Return how well rules do
    """
    def __init__(self):
        self._enabled = False
        self._output = {}
        self._metadata = {}
        self._metrics = []
        self._average = False
        self._save = False

    def __repr__(self):
        return self.__class__.__name__ 
    
    def apply(self, s):
        data = s._data
        d = s._pred
        rules = s._rules
        datafile = s._datafile

        self._metrics = self._metadata['metrics']
        self._average = self._metadata['average']
        self._save = self._metadata['save']

        y = [int(row[0]) for row in data]

        str_rules = [f'{item}' for item in rules]

        self._output = {}
        if self._average:
            self._output['average'] = {}
            for item in self._metrics:
                self._output['average'][item] = 0 #initialize to 0 

        metrics_dict = {'accuracy': self.accuracy, 'precision': self.precision, 'recall': self.recall, 'f1': self.f1, 'cm': self.cm} 

        if self._average:
            d['average'] = self.weighted_average(rules, str_rules, d)
        
        rule_pred = {} #for interactive mode, returning predictions

        for rule in d:
            self._output[rule] = {}

            if rule == 'RandomForest' or rule == 'Fasttext': 
                pred = [int(item) for item in d[rule][0]]
                y = [int(item) for item in d[rule][1]]
            else:
                pred = d[rule]
            
            if self._metadata['return_pred']:
                rule_pred[rule] = pred
            
            for metric in self._metrics:
                if metric in metrics_dict:
                    self._output[rule][metric] = metrics_dict[metric](y, pred)

        if self._metadata['return_pred']: #interactive mode
            return rule_pred

        if self._save:   
            import time
            ts = time.gmtime()

            df = pd.DataFrame.from_dict(self._output)

            df.T.to_csv(f'report/{datafile}_{time.strftime("%Y-%m-%d %H:%M:%S", ts)}-report.csv', index = True, header=True) #saves as datafile_timestamp-report.csv

        return self._output

    def accuracy(self, y: list, pred: list):
        # accuracy: (tp + tn) / (p + n)
        from sklearn.metrics import accuracy_score
        accuracy = accuracy_score(y, pred)    
        return accuracy

    def precision(self, y: list, pred: list):
        # precision tp / (tp + fp)
        from sklearn.metrics import precision_score
        precision = precision_score(y, pred)  
        return precision

    def recall(self, y: list, pred: list):
        # precision tp / (tp + fp)
        from sklearn.metrics import recall_score
        recall = recall_score(y, pred)  
        return recall

    def f1(self, y: list, pred: list):
        # f1: 2 tp / (2 tp + fp + fn)
        from sklearn.metrics import f1_score
        f1 = f1_score(y, pred)   
        return f1
                
    def cm(self, y: list, pred: list):
        from sklearn.metrics import confusion_matrix
        return confusion_matrix(y, pred, labels=[1,0])  

    def weighted_average(self, rules: list, str_rules: list, d: list):
        average = [] #initialize
        for rule in d:
            if not rule == 'average':
                if average == []:
                    if rule == 'RandomForest' or rule == 'Fasttext':
                        average = [0]*len(d[rule][0])
                    else:
                        average = [0]*len(d[rule])

                if rule == 'RandomForest' or rule == 'Fasttext': 
                    pred = d[rule][0]
                else:
                    pred = d[rule]
                
                for index, item in enumerate(pred):
                    average[index] += item * rules[str_rules.index(rule)]._weight

        average = [round(average[index]+0.0001) for index, item in enumerate(average)] #round() rounds 0.5 to 0, so this makes sure rounding up occurs

        return average