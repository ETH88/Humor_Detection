import abc
from abc import ABCMeta, abstractmethod
import os

class PreProcess(): #abstract base class for pre-processing
    __metaclass__ = abc.ABCMeta

    @abstractmethod
    def __repr__(self):
        raise NotImplementedError()

    @abstractmethod
    def apply(self, data: list):
        """The core logic of the rule implementation"""
        raise NotImplementedError()

class Rule(): #abstract base class for running rules
    __metaclass__ = abc.ABCMeta

    @abstractmethod
    def __repr__(self):
        raise NotImplementedError()

    @abstractmethod
    def execute(self, s):
        """The core logic of the rule implementation"""
        raise NotImplementedError()

class PostProcess(): #abstract base class for post-processing
    __metaclass__ = abc.ABCMeta

    @abstractmethod
    def __repr__(self):
        raise NotImplementedError()

    @abstractmethod
    def apply(self, s):
        """The core logic of the rule implementation"""
        raise NotImplementedError()

class Essential_PreProcess(PreProcess):
    """
    Required pre-processing rule - noise removal/lowercase
    """
    def __init__(self):
        self._enabled = True

    def __repr__(self):
        return self.__class__.__name__ #returns name of class

    def apply(self, data: list):
        import re
        for i in range(len(data)):
            temp = data[i][1]
            temp = re.sub('[^a-zA-Z]',' ',temp) #noise removal #TODO: change to ' '??
            temp = ' '.join(temp.split()) #remove extra whitespace
            words = temp.split(" ")

            review = [word.lower() for word in words if not word == ""]
            review = ' '.join(review)
            data[i][1] = review

        #print('essential preprocess ', data)
        return data


class Pipeline:
    """
    Handles Preprocessing, Rules, and Postprocessing
    """

    def __init__(self, config):
        #DATA
        self._data = []
        self._datafile = config['datafile']
        self._interactive = config['interactive_mode']
        if self._interactive == False:
            with open(f"{os.getcwd()}/data/{config['datafile']}", 'r') as data_file:
                for line in data_file:
                    temp = line[:-1].split(",")
                    self._data.append([temp[0], temp[1]]) #IMPORTANT: use w testingdata_21c26804-96c8-11ea-9d84-acde48001122_copy.txt 
                    #IMPORTANT: if using 'traintest.txt', you must change line 81 to "self._data.append([temp[1], temp[3]])"           
            ###Preprocessing###
            self._data = Essential_PreProcess().apply(self._data)
            self._rawdata = [row[:] for row in self._data]

        self._preprocess = []
        #self._modelID = 0
        self._humorwords = []
        self._nothumorwords = []
        
        for i in range(len(config['preprocess'])):
            self._preprocess.append(config['preprocess'][i]['obj'])
            self._preprocess[i]._enabled = config['preprocess'][i]['enabled']
            if 'metadata' in config['preprocess'][i].keys(): #if there is metadata
                self._preprocess[i]._metadata = config['preprocess'][i]['metadata']

        ###Rules
        dependency = {}
        for rule in config['rules']:
            dependency[rule] = config['rules'][rule]['dependencies']
        self._rules = self.__order(dependency)  # list of str named rule objects, ordered

        for index, rule in enumerate(config['rules']):
            self._rules[index] = config['rules'][rule]['obj']
            self._rules[index]._enabled = config['rules'][rule]['enabled']
            self._rules[index]._weight = config['rules'][rule]['weight']
            if 'metadata' in config['rules'][rule].keys(): #if there is metadata
                self._rules[index]._metadata = config['rules'][rule]['metadata']

        self._pred = {}

        ###PostProcess
        self._postprocess = []
        for index, stage in enumerate(config['postprocess']):
            self._postprocess.append(config['postprocess'][stage]['obj'])
            self._postprocess[index]._enabled = config['postprocess'][stage]['enabled']
            self._postprocess[index]._metadata = config['postprocess'][stage]['metadata']

    def __order(self, arg):
        '''
        Simple Dependency resolver - Sandesh Gade
        "arg" is a dependency dictionary in which
        the values are the dependencies of their respective keys.
        '''
        d = dict((k, set(arg[k])) for k in arg) #makes sure all values are unique
        r = []
        while d:
            # values not in keys 
            t = set(i for v in d.values() for i in v) - set(d.keys())
            # and keys without value (rules wout dependencies)
            t.update(k for k, v in d.items() if not v)
            # can be done right away
            if not list(t):
                print("Dependency resolution failed.")
                break
            for rule in t:
                if rule is not None:
                    r.append(rule) #values not in keys and rules wout dependencies must be done first
            # and cleaned up
            d = dict(((k, v - t) for k, v in d.items() if v)) #removes rules wout dependencies from d AND other rules' dependencies on values not in keys and rules wout dependencies from d
        return r
    
    def __read_sentence(self): #interactive mode
        sentence = input("Type sentence (to stop, type EXIT): ")
        self._data = [['0',sentence]]

        if not self._data[0][1] == 'EXIT':
            self._data = Essential_PreProcess().apply(self._data)
            self._rawdata = [row[:] for row in self._data]

    def run(self): 
        if not self._interactive:
            #PREPROCESS
            self.__pre_process()
            
            #CORE: run rules
            self.__execute_rules()
            #return self.__execute_rules(self._data)

            #return self.__post_process()
            print(self.__post_process())

        else: #interactive mode
            while True:
                self.__read_sentence()

                if self._data[0][1] == 'EXIT':
                    break #user typed exit in interactive mode

                #PREPROCESS
                self.__pre_process()
                
                #CORE: run rules
                self.__execute_rules()
                #return self.__execute_rules(self._data)

                #return self.__post_process()
                print(self.__post_process())

    def __pre_process(self):
        for stage in self._preprocess: 
            if stage._enabled: 
                print(stage)
                #if stage.__class__.__name__ == 'Train_RandomForest': #works w docker flask app
                    #self._modelID = str(stage.apply(self._data))
                    
                output = stage.apply(self._data)
                if 'data' in output.keys():
                    self._data = output['data']   
                #print(self._data)

        #print(self._data) 

    def __execute_rules(self):
        for rule in self._rules:
            if rule._enabled: 
                print(rule)
                self._pred[f'{rule}'] = rule.execute(self) #just pass self object
                #all except random forest needs rawdata
                #only negators need pred
                #only RandomForest needs modelID
                #only contain_funny and contain_notfunny need preprocess

    def __post_process(self):
        output = {}
        for stage in self._postprocess:
            if stage._enabled:
                output[stage] = stage.apply(self)
                #just pass self object
        return output
